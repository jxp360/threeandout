# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,render_to_response,RequestContext
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

def index(request):
    return render(request, 'picks/index.html', {})

@login_required
def picks(request):
    weeks = range(1,18)
    return render(request, 'picks/pick.html', {'weeks':weeks})
    
@login_required
def submit(request,week):
    dir(User)
    # TODO: Change to grab player from current logged in session
    player = FFLPlayer.objects.get(user=request.user)
    
    try:
        pick = Picks.objects.get(week=week, fflPlayer=player)
    except ObjectDoesNotExist:
        pick = Picks(week=week, fflPlayer=player)
    
    pick.qb = NFLPlayer.objects.get(pk=request.POST["QB"])
    pick.rb = NFLPlayer.objects.get(pk=request.POST["RB"])
    pick.wr = NFLPlayer.objects.get(pk=request.POST["WR"])
    pick.te = NFLPlayer.objects.get(pk=request.POST["TE"])
    #pick.score = 0.0
    pick.mod_time=timezone.now()
    
    if validatePick(week,pick):
        pick.save()    
    else:
        return HttpResponse("Invalid Pick")
    
    return HttpResponseRedirect(reverse('threeandout:picksummary', args=(week)))

@login_required
def picksummary(request,week):
    # TODO: Change to grab player from current logged in session
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

    return render(request, 'picks/pickweek.html', {'week':week,'QBs': QBs,'RBs': RBs,'WRs': WRs,'TEs': TEs,
                                                   'qb':qb,'rb':rb,'wr':wr,'te':te,'currentpicks':currentpicks})
@login_required    
def weeklyresultssummary(request):
    weeks = range(1,18)
    return render(request, 'picks/weeklyresultssummary.html', {'weeks':weeks})

@login_required
def weeklyresults(request,week):
    player = FFLPlayer.objects.get(user=request.user)
    try:
        picks = Picks.objects.get(week=week, fflPlayer=player)
    except ObjectDoesNotExist:
        currentpicks = False
        picks=None
    else:
        currentpicks = True
 
    return render(request, 'picks/weeklyresults.html', {'week':week, 'currentpicks':currentpicks,picks:picks})

@login_required
def personalresults(request):
    player = FFLPlayer.objects.get(user=request.user)
    picks = Picks.objects.filter(fflPlayer=player)
    print "picks", picks
    pickData= []
    for pick in picks:
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

      d={'week':pick.week, 
         'score':pick.score, 
         'qbName':pick.qb.name,
         'qbScore':qbScore, 
         'rbName':pick.rb.name, 
         'rbScore':rbScore, 
         'teName':pick.te.name, 
         'teScore':teScore,
         'wrName':pick.wr.name, 
         'wrScore':wrScore}
      pickData.append(d)  
    return render(request, 'picks/personalresults.html', {'picks':pickData})

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
    now = datetime.utcnow().replace(tzinfo=pytz.timezone('utc'))
    return (game.kickoff.astimezone(pytz.timezone('US/Eastern')) > (now +timedelta(minutes=PICK_LOCKOUT_MINUTES)))
                           
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
