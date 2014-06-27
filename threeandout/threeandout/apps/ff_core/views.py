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
from threeandout.apps.ff_core.models import NFLPlayer, Picks,FFLPlayer,NFLSchedule, NFLWeeklyStat,Standing,PlayoffStanding
from threeandout.apps.ff_core.forms import FFLPlayerForm


def index(request):
    return render(request, 'ff_core/index.html', {})

def rules(request):
    return render(request, 'ff_core/rules.html', {})

@login_required
def picks(request):
    weeks = range(1,18)
    return render(request, 'ff_core/pick.html', {'weeks':weeks})
    
@login_required
def submit(request,week,season_type="Regular"):
    player = FFLPlayer.objects.get(user=request.user)
    
    pickexists = False
    try:
        # A Pick that that user and week already exists
        pick = Picks.objects.get(week=week,season_type=season_type, fflPlayer=player)
        pickexists = True
    except ObjectDoesNotExist:
        pickexists = False
        
    
    if pickexists: 
        # If the  current pick.player is valid then ok to change it
        if validatePlayer(week,season_type,pick.qb):
            pick.qb = NFLPlayer.objects.get(pk=request.POST["QB"])
            if not(validatePlayer(week,season_type,pick.qb)) or not(validateTwoOrLessPicks(player,pick.qb,"QB",week)):
                return HttpResponse("Invalid Pick")
        if validatePlayer(week,season_type,pick.rb):
            pick.rb = NFLPlayer.objects.get(pk=request.POST["RB"])
            if not(validatePlayer(week,season_type,pick.rb))  or not(validateTwoOrLessPicks(player,pick.rb,"RB",week)):
                return HttpResponse("Invalid Pick")
        if validatePlayer(week,season_type,pick.wr):
            pick.wr = NFLPlayer.objects.get(pk=request.POST["WR"])
            if not(validatePlayer(week,season_type,pick.wr)) or not(validateTwoOrLessPicks(player,pick.wr,"WR",week)):
                return HttpResponse("Invalid Pick")
        if validatePlayer(week,season_type,pick.te):
            pick.te = NFLPlayer.objects.get(pk=request.POST["TE"])
            if not(validatePlayer(week,season_type,pick.te)) or not(validateTwoOrLessPicks(player,pick.te,"TE",week)):
                return HttpResponse("Invalid Pick")
        pick.mod_time=timezone.now()
        pick.save()      
           
    else:
        #Make Totally New Pick
        pick = Picks(week=week,season_type=season_type, fflPlayer=player)
        pick.qb = NFLPlayer.objects.get(pk=request.POST["QB"])
        pick.rb = NFLPlayer.objects.get(pk=request.POST["RB"])
        pick.wr = NFLPlayer.objects.get(pk=request.POST["WR"])
        pick.te = NFLPlayer.objects.get(pk=request.POST["TE"])
        if validatePick(week,season_type,pick) and validateTwoOrLessPicksAll(player,pick,week):
            pick.mod_time=timezone.now()
            pick.save()    
        else:
            return HttpResponse("Invalid Pick")
    
    return HttpResponseRedirect(reverse('threeandout:picksummary', args=(week,season_type)))

@login_required
def picksummary(request,week,season_type="Regular"):
    player = FFLPlayer.objects.get(user=request.user)
    pick =  Picks.objects.get(week=week,season_type=season_type,fflPlayer=player)
    qb = pick.qb.name
    rb = pick.rb.name
    wr = pick.wr.name
    te = pick.te.name

    return render(request, 'ff_core/picksummary.html', {'week':week,'qb':qb,'rb':rb,'wr':wr,'te':te})

@login_required
def pickcurrentweek(request):
    now = datetime.utcnow().replace(tzinfo=pytz.timezone('utc'))
    bufferTime = timedelta(minutes=-240)
    # The closest game that hasn't started is the "current" week
    # It is delayed by 4 hours so that if you go to check who you picked in the final game of the week it won't move to the next week yet
    game = NFLSchedule.objects.filter(kickoff__gt=now+bufferTime).order_by("kickoff").first()
    week = game.week
    season_type = game.season_type
    print week,season_type
    return HttpResponseRedirect(reverse('threeandout:pickweek',args=(week,season_type)))

@login_required
def pickweek(request, week,season_type="Regular"):
    player = FFLPlayer.objects.get(user=request.user)
    try:
        pick = Picks.objects.get(week=week, fflPlayer=player,season_type=season_type)
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

    QBs = ValidPlayers(week,season_type,'QB',request.user)
    RBs = ValidPlayers(week,season_type,'RB',request.user)
    WRs = ValidPlayers(week,season_type,'WR',request.user)   
    TEs = ValidPlayers(week,season_type,'TE',request.user) 

    
    # If they already have picks and that pick is not valid then it cannot be changed
    if qb !=None:
        if not (validatePlayer(week,season_type,pick.qb)): QBs = []
    if rb !=None:
        if not (validatePlayer(week,season_type,pick.rb)): RBs = []
    if wr !=None:
        if not (validatePlayer(week,season_type,pick.wr)): WRs = []
    if te !=None:
        if not (validatePlayer(week,season_type,pick.te)): TEs = []            
    
    return render(request, 'ff_core/pickweek.html', {'week':week,'QBs': QBs,'RBs': RBs,'WRs': WRs,'TEs': TEs,
                                                   'qb':qb,'rb':rb,'wr':wr,'te':te,
                                                   'currentpicks':currentpicks})
@login_required    
def currentstandings(request):
    standings = Standing.objects.all().order_by("-scoretodate")
    return render(request, 'ff_core/currentstandings.html', {'scores':standings})

@login_required    
def playoffstandings(request):
    standings = PlayoffStanding.objects.all().order_by("-scoretodate")
    return render(request, 'ff_core/playoffstandings.html', {'scores':standings})

@login_required    
def weeklyresultssummary(request):
    weeks = range(1,18)
    players = FFLPlayer.objects.all()
    tmp = [(x.scoretodate, x.teamname, x.user.id) for x in players]
    tmp.sort(reverse=True)
    leaders = [{'user':x[1],'score':x[0], 'id':x[2], 'rank': idx} for idx,x in enumerate(tmp)]
    return render(request, 'ff_core/weeklyresultssummary.html', {'weeks':weeks, 'scores':leaders})

@login_required
def weeklyresults(request,week,season_type="Regular"):
    lastGame = getLastGame(week) 
    #you've got to love the double negative here -- its like coding with a 6 year old!
    okToDisplay = not hasNotStarted(lastGame)
    #for debugging --
    if okToDisplay:
        picks = Picks.objects.filter(week=week,season_type=season_type)
        tmpList = [(x.score,x) for x in picks]
        tmpList.sort(reverse=True)
        pickData = [getPickData(x,season_type) for x in picks]
    else:
        pickData = []
    
    return render(request, 'ff_core/weeklyresults.html', {'week':week, 'picks':pickData, 'ok':okToDisplay})

@login_required
def personalresults(request):
    #TODO Currently only shows regular season
    player = FFLPlayer.objects.get(user=request.user)
    picks = Picks.objects.filter(fflPlayer=player).filter(season_type="Regular").order_by('week')
    pickData= [getPickData(pick,season_type="Regular") for pick in picks]
    return render(request, 'ff_core/personalresults.html', {'picks':pickData})

@login_required
def selected(request, user):
    player = FFLPlayer.objects.get(id=user)
    picks = Picks.objects.filter(fflPlayer=player)
    qbs={}
    rbs={}
    wrs={}
    tes={}
    #only if the user requested his own data will we show them the pending stuff
    showPending = request.user == player.user

    for pick in picks:
        week = pick.week
        season_type = pick.season_type
        updateDict(qbs,pick.qb, week,season_type, showPending)
        updateDict(rbs,pick.rb, week,season_type, showPending)
        updateDict(wrs,pick.wr, week,season_type, showPending)
        updateDict(tes,pick.te, week,season_type, showPending)
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
    return render(request, 'ff_core/selected.html', {'qb':qbList,'wr':wrList,'te':teList,'rb':rbList, 'fflplayer':player.teamname})

def updateDict(positionDict, player, week,season_type, showPending):
    playerPending = validatePlayer(week,season_type, player)
    if showPending or not playerPending:
      name = player.name
      try:
          d=positionDict[name]
      except KeyError:
          d ={'name':name, 'pending':0, 'locked':0}
          positionDict[name]=d
      if showPending and playerPending:
         d['pending']+=1
      else:
          d['locked']+=1
      
def getPickData(pick,season_type="Regular"):
      try:
        qbScore = NFLWeeklyStat.objects.get(player=pick.qb, game__week=pick.week,game__season_type=season_type).score
      except ObjectDoesNotExist:
        qbScore = '-'
      try:
        rbScore = NFLWeeklyStat.objects.get(player=pick.rb, game__week=pick.week,game__season_type=season_type).score
      except ObjectDoesNotExist:
        rbScore = '-'
      try:
        wrScore = NFLWeeklyStat.objects.get(player=pick.wr, game__week=pick.week,game__season_type=season_type).score
      except ObjectDoesNotExist:
        wrScore = '-'
      try:
        teScore = NFLWeeklyStat.objects.get(player=pick.te, game__week=pick.week,game__season_type=season_type).score
      except ObjectDoesNotExist:
        teScore = '-'
      d={'user':pick.fflPlayer.teamname,
         'week':pick.week,
         'season_type':season_type,
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
    return render_to_response('ff_core/preferences.html', {
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
    
    return render_to_response('ff_core/register.html', {
        'form': form,
    },context_instance=RequestContext(request))

def findOpponent(player,week):
        try:
            opp = NFLSchedule.objects.get(Q(week=week)&(Q(home=player.team.short_name))).away
        except ObjectDoesNotExist:
            try:
                opp = NFLSchedule.objects.get(Q(week=week)&(Q(away=player.team.short_name))).home
            except ObjectDoesNotExist:
                opp=""
        return opp

