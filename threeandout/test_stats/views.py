# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.template import Context
from django.shortcuts import render,render_to_response,RequestContext, get_object_or_404
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm,forms
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
#from django.core.exceptions import DoesNotExist
from datetime import datetime, timedelta
import time
import pytz
from django.db.models import Q
from validate import *
from test_stats.models import NFLPlayer, Picks,FFLPlayer,NFLSchedule, NFLWeeklyStat
from test_stats.forms import FFLPlayerForm


def index(request):
    return render(request, 'picks/index.html', {})

def rules(request):
    return render(request, 'picks/rules.html', {})

@login_required
def picks(request):
    weeks = range(1,18)
    return render(request, 'picks/pick.html', {'weeks':weeks})
    
@login_required
def submit(request,week):
    print "POST" , request.POST
    player = FFLPlayer.objects.get(user=request.user)
    
    pickexists = False
    try:
        # A Pick that that user and week already exists
        pick = Picks.objects.get(week=week, fflPlayer=player)
        pickexists = True
    except ObjectDoesNotExist:
        pickexists = False
        
    
    if pickexists: 
        # If the  current pick.player is valid then ok to change it
        if validatePlayer(week,pick.qb):
            pick.qb = NFLPlayer.objects.get(pk=request.POST["QB"])
            if not(validatePlayer(week,pick.qb)) or not(validateTwoOrLessPicks(player,pick.qb,"QB",week)):
                return HttpResponse("Invalid Pick")
        if validatePlayer(week,pick.rb):
            pick.rb = NFLPlayer.objects.get(pk=request.POST["RB"])
            if not(validatePlayer(week,pick.rb))  or not(validateTwoOrLessPicks(player,pick.rb,"RB",week)):
                return HttpResponse("Invalid Pick")
        if validatePlayer(week,pick.wr):
            pick.wr = NFLPlayer.objects.get(pk=request.POST["WR"])
            if not(validatePlayer(week,pick.wr)) or not(validateTwoOrLessPicks(player,pick.wr,"WR",week)):
                return HttpResponse("Invalid Pick")
        if validatePlayer(week,pick.te):
            pick.te = NFLPlayer.objects.get(pk=request.POST["TE"])
            if not(validatePlayer(week,pick.te)) or not(validateTwoOrLessPicks(player,pick.te,"TE",week)):
                return HttpResponse("Invalid Pick")
        pick.mod_time=timezone.now()
        pick.save()      
           
    else:
        #Make Totally New Pick
        pick = Picks(week=week, fflPlayer=player)
        pick.qb = NFLPlayer.objects.get(pk=request.POST["QB"])
        pick.rb = NFLPlayer.objects.get(pk=request.POST["RB"])
        pick.wr = NFLPlayer.objects.get(pk=request.POST["WR"])
        pick.te = NFLPlayer.objects.get(pk=request.POST["TE"])
        if validatePick(week,pick) and validateTwoOrLessPicksAll(player,pick,week):
            pick.mod_time=timezone.now()
            pick.save()    
        else:
            return HttpResponse("Invalid Pick")
    
    return HttpResponseRedirect(reverse('threeandout:picksummary', args=(week)))

@login_required
def picksummary(request,week):
    player = FFLPlayer.objects.get(user=request.user)
    pick =  Picks.objects.get(week=week, fflPlayer=player)
    qb = pick.qb.name
    rb = pick.rb.name
    wr = pick.wr.name
    te = pick.te.name

    return render(request, 'picks/picksummary.html', {'week':week,'qb':qb,'rb':rb,'wr':wr,'te':te})

@login_required
def pickweek(request, week):
    time0 = time.time()
    player = FFLPlayer.objects.get(user=request.user)
    try:
        pick = Picks.objects.get(week=week, fflPlayer=player)
    except ObjectDoesNotExist:
        qb = None
        rb = None
        wr = None
        te = None    
        currentpicks = False
    else:
        qb = pick.qb
        rb = pick.rb
        wr = pick.wr
        te = pick.te
        currentpicks = True

    QBs = ValidPlayers(week,'QB',request.user)
    RBs = ValidPlayers(week,'RB',request.user)
    WRs = ValidPlayers(week,'WR',request.user)   
    TEs = ValidPlayers(week,'TE',request.user) 
    # If they already have picks and that pick is not valid then it cannot be changed
    if qb !=None:
        if not (validatePlayer(week,pick.qb)): QBs = []
    if rb !=None:
        if not (validatePlayer(week,pick.rb)): RBs = []
    if wr !=None:
        if not (validatePlayer(week,pick.wr)): WRs = []
    if te !=None:
        if not (validatePlayer(week,pick.te)): TEs = []            


    time1 = time.time()
    print "Delta" , time1-time0
    return render(request, 'picks/pickweek.html', {'week':week,'QBs': QBs,'RBs': RBs,'WRs': WRs,'TEs': TEs,
                                                   'qb':qb,'rb':rb,'wr':wr,'te':te,'currentpicks':currentpicks})
@login_required    
def weeklyresultssummary(request):
    weeks = range(1,18)
    players = FFLPlayer.objects.all()
    tmp = [(x.scoretodate, x.teamname, x.user.id) for x in players]
    tmp.sort(reverse=True)
    leaders = [{'user':x[1],'score':x[0], 'id':x[2] } for x in tmp]
    return render(request, 'picks/weeklyresultssummary.html', {'weeks':weeks, 'scores':leaders})

@login_required
def weeklyresults(request,week):
    lastGame = getLastGame(week) 
    #you've got to love the double negative here -- its like coding with a 6 year old!
    okToDisplay = not hasNotStarted(lastGame)
    #for debugging --
    if okToDisplay:
        picks = Picks.objects.filter(week=week)
        tmpList = [(x.score,x) for x in picks]
        tmpList.sort(reverse=True)
        sortedPicks = [x[1] for x in tmpList]
        pickData = [getPickData(x) for x in picks]
    else:
        pickData = []
    
    return render(request, 'picks/weeklyresults.html', {'week':week, 'picks':pickData, 'ok':okToDisplay})

@login_required
def personalresults(request):
    player = FFLPlayer.objects.get(user=request.user)
    picks = Picks.objects.filter(fflPlayer=player).order_by('week')
    pickData= [getPickData(pick) for pick in picks]
    return render(request, 'picks/personalresults.html', {'picks':pickData})

@login_required
def selected(request, user):
    try:
        userObj = User.objects.get(id=user)
    except ObjectDoesNotExist:
        return HttpResponse('Invalid User "%s"' %user)
    #try:
    #    player = FFLPlayer.objects.get(teamname=user)
    #except ObjectDoesNotExist:
    #    return HttpResponse('Invalid User "%s"' %user)
    player = FFLPlayer.objects.get(user=userObj)
    picks = Picks.objects.filter(fflPlayer=player)
    qbs={}
    rbs={}
    wrs={}
    tes={}
    #only if the user requested his own data will we show them the pending stuff
    showPending = request.user == player.user

    for pick in picks:
        week = pick.week
        updateDict(qbs,pick.qb, week, showPending)
        updateDict(rbs,pick.rb, week, showPending)
        updateDict(wrs,pick.wr, week, showPending)
        updateDict(tes,pick.te, week, showPending)
    qbTmp = [x for x in qbs.items()]
    wrTmp = [x for x in wrs.items()]
    teTmp = [x for x in tes.items()]
    rbTmp = [x for x in rbs.items()]
    qbTmp.sort()
    wrTmp.sort()
    teTmp.sort()
    rbTmp.sort()
    qbList = [x[1] for x in qbTmp]
    wrList = [x[1] for x in wrTmp]
    teList = [x[1] for x in teTmp]
    rbList = [x[1] for x in rbTmp]
    return render(request, 'picks/selected.html', {'qb':qbList,'wr':wrList,'te':teList,'rb':rbList, user:user})

def updateDict(positionDict, player, week, showPending):
    playerPending = validatePlayer(week, player)
    if showPending or not playerPending:
      name = player.name
      try:
          d=positionDict[name]
      except KeyError:
          d ={'name':name, 'pending':0, 'locked':0}
          positionDict[name]=d
      if showPending:
          d['pending']+=1
      else:
          d['locked']+=1
      
def getPickData(pick):
      try:
        qbScore = NFLWeeklyStat.objects.get(player=pick.qb, week=pick.week).score
      except ObjectDoesNotExist:
        qbScore = '-'
      try:
        rbScore = NFLWeeklyStat.objects.get(player=pick.rb, week=pick.week).score
      except ObjectDoesNotExist:
        rbScore = '-'
      try:
        wrScore = NFLWeeklyStat.objects.get(player=pick.wr, week=pick.week).score
      except ObjectDoesNotExist:
        wrScore = '-'
      try:
        teScore = NFLWeeklyStat.objects.get(player=pick.te, week=pick.week).score
      except ObjectDoesNotExist:
        teScore = '-'

      d={'user':pick.fflPlayer.teamname,
         'week':pick.week,
         'score':pick.score,
         'qbName':pick.qb.name,
         'qbScore':qbScore,
         'rbName':pick.rb.name,
         'rbScore':rbScore,
         'teName':pick.te.name,
         'teScore':teScore,
         'wrName':pick.wr.name,
         'wrScore':wrScore}
      return d



def getLastGame(week):
    return NFLSchedule.objects.filter(week=week).order_by('-kickoff')[0]

@login_required
def editPreferences(request):
    ffl = get_object_or_404(FFLPlayer, user=request.user)
    if request.method == "POST":
        form = FFLPlayerForm(request.POST, instance=ffl)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/threeandout/picks/')
    else:
        form = FFLPlayerForm(instance=ffl)
    return render_to_response('picks/preferences.html', {
                                  'form': form,
                                  'title': 'Edit Preferences' },
                                  context_instance=RequestContext(request))

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    teamname = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ( "username", "email", "teamname" )
    
    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("Can't create User and FFLPlayer without database save")
        user = super(UserCreateForm, self).save(commit=True)
        newplayer = FFLPlayer(user=user,league=0, email=self.cleaned_data['email'], teamname=self.cleaned_data['teamname'])
        newplayer.save()
        return user, newplayer
   
def registerUser(request):
    if request.method =='POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user, newplayer = form.save()
            #newplayer.save()
            #user = User.objects.create_user(form.cleaned_data['username'], None, form.cleaned_data['password1'])
            #user.save()
            return HttpResponseRedirect('/threeandout/login/') # Redirect after POST
    else:
        form = UserCreateForm() # An unbound form
    
    return render_to_response('picks/register.html', {
        'form': form,
    },context_instance=RequestContext(request))

