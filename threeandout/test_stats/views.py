# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,render_to_response,RequestContext
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm,forms
from django.contrib.auth.decorators import login_required
#from django.core.exceptions import DoesNotExist
from datetime import datetime, timedelta
import pytz

PICK_LOCKOUT_MINUTES = 10


from test_stats.models import NFLPlayer, Picks,FFLPlayer,NFLSchedule

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
    
    #pick = player.picks.get_or_create(week=week) # I don't know why this doesn't work
    try:
        pick = player.picks.get(week=week)
    #except FFLPlayer.DoesNotExist:  # I don't know why this doesn't work
    except:
        pick = Picks(week=week)
    
    pick.qb = NFLPlayer.objects.get(pk=request.POST["QB"])
    pick.rb = NFLPlayer.objects.get(pk=request.POST["RB"])
    pick.wr = NFLPlayer.objects.get(pk=request.POST["WR"])
    pick.te = NFLPlayer.objects.get(pk=request.POST["TE"])
    pick.score = 0.0
    pick.mod_time=timezone.now()
    
    if validatePick(week,pick):
        pick.save()
        player.picks.add(pick)
        player.save()    
    else:
        return HttpResponse("Invalid Pick")
    
    return HttpResponseRedirect(reverse('threeandout:picksummary', args=(week)))

@login_required
def picksummary(request,week):
    # TODO: Change to grab player from current logged in session
    player = FFLPlayer.objects.get(user=request.user)
    qb = player.picks.get(week=week).qb.name
    rb = player.picks.get(week=week).rb.name
    wr = player.picks.get(week=week).wr.name
    te = player.picks.get(week=week).te.name

    return render(request, 'picks/picksummary.html', {'week':week,'qb':qb,'rb':rb,'wr':wr,'te':te})

@login_required
def pickweek(request, week):

    player = FFLPlayer.objects.get(user=request.user)
    try:
        qb = player.picks.get(week=week).qb.name
        rb = player.picks.get(week=week).rb.name
        wr = player.picks.get(week=week).wr.name
        te = player.picks.get(week=week).te.name
        currentpicks = True
    except:
        currentpicks = False
        qb = None
        rb = None
        wr = None
        te = None    
    
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
    return render(request, 'picks/weeklyresults.html', {'week':week})

@login_required
def personalresults(request):
    return render(request, 'picks/personalresults.html', {})

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ( "username", "email" )
        
def registerUser(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            newplayer = FFLPlayer(user=user,league=0)
            newplayer.save()
            #user = User.objects.create_user(form.cleaned_data['username'], None, form.cleaned_data['password1'])
            #user.save()
            return HttpResponseRedirect('/threeandout/login/') # Redirect after POST
    else:
        form = UserCreationForm() # An unbound form
    
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
