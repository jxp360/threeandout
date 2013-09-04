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
import pytz

PICK_LOCKOUT_MINUTES = 10

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
            if not(validatePlayer(week,pick.qb)):
                return HttpResponse("Invalid Pick")
        if validatePlayer(week,pick.rb):
            pick.rb = NFLPlayer.objects.get(pk=request.POST["RB"])
            if not(validatePlayer(week,pick.rb)):
                return HttpResponse("Invalid Pick")
        if validatePlayer(week,pick.wr):
            pick.wr = NFLPlayer.objects.get(pk=request.POST["WR"])
            if not(validatePlayer(week,pick.wr)):
                return HttpResponse("Invalid Pick")
        if validatePlayer(week,pick.te):
            pick.te = NFLPlayer.objects.get(pk=request.POST["TE"])
            if not(validatePlayer(week,pick.te)):
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
        if validatePick(week,pick):
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
        qb = pick.qb.name
        rb = pick.rb.name
        wr = pick.wr.name
        te = pick.te.name
        currentpicks = True

    QBs = ValidPlayers(week,'QB')
    RBs = ValidPlayers(week,'RB')
    WRs = ValidPlayers(week,'WR')
    TEs = ValidPlayers(week,'TE') 
    
    # If they already have picks and that pick is not valid then it cannot be changed
    if qb !=None:
        if not (validatePlayer(week,pick.qb)): QBs = []
    if rb !=None:
        if not (validatePlayer(week,pick.rb)): RBs = []
    if wr !=None:
        if not (validatePlayer(week,pick.wr)): WRs = []
    if te !=None:
        if not (validatePlayer(week,pick.te)): TEs = []            


    return render(request, 'picks/pickweek.html', {'week':week,'QBs': QBs,'RBs': RBs,'WRs': WRs,'TEs': TEs,
                                                   'qb':qb,'rb':rb,'wr':wr,'te':te,'currentpicks':currentpicks})
@login_required    
def weeklyresultssummary(request):
    weeks = range(1,18)
    players = FFLPlayer.objects.all()
    tmp = [(x.scoretodate, x.teamname) for x in players]
    tmp.sort(reverse=True)
    leaders = [{'user':x[1],'score':x[0]} for x in tmp]
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

def hasNotStarted(game, buffer=timedelta(0)):
    now = datetime.utcnow().replace(tzinfo=pytz.timezone('utc'))
    return game.kickoff.astimezone(pytz.timezone('US/Eastern')) > (now +buffer)

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

    
def validatePlayer(week,player):
    try:
        game = NFLSchedule.objects.get(week=week,home=player.team)
    except:
        try:
            game = NFLSchedule.objects.get(week=week,away=player.team)
        except:
            return False
    return hasNotStarted(game, timedelta(minutes=PICK_LOCKOUT_MINUTES))
#    now = datetime.utcnow().replace(tzinfo=pytz.timezone('utc'))
#    return (game.kickoff.astimezone(pytz.timezone('US/Eastern')) > (now +timedelta(minutes=PICK_LOCKOUT_MINUTES)))
                           
def ValidPlayers(week,position):
    players= NFLPlayer.objects.filter(position=position)
    validplayers = []
    for player in players:
        if validatePlayer(week,player):
            validplayers.append(player)
            
    return validplayers

def validatePick(week,pick):
    
    valid = (validatePlayer(week,pick.qb) and 
             validatePlayer(week,pick.rb) and 
             validatePlayer(week,pick.wr) and 
             validatePlayer(week,pick.te))
    return valid
