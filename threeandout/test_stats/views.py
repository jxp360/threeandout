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

from test_stats.models import NFLPlayer, Picks,FFLPlayer

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
    pick.save()
    player.picks.add(pick)
    player.save()
    
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
    
    # TODO: Change to grab player from current logged in session
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
    
    #week = get_object_or_404(Schedule, pk=week)
    QBs = NFLPlayer.objects.filter(position='QB')
    RBs = NFLPlayer.objects.filter(position='RB')
    WRs = NFLPlayer.objects.filter(position='WR')
    TEs = NFLPlayer.objects.filter(position='TE')
    
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
        
@login_required
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


# def registerUser(self, request, *args, **kwargs):
#         user_form = UserCreateForm(request.POST)
#         if user_form.is_valid():
#             username = user_form.clean_username()
#             password = user_form.clean_password2()
#             user_form.save()
#             user = authenticate(username=username,
#                                 password=password)
#             login(request, user)
#             return HttpResponseRedirect("threeandout")
#         return render(request,
#                       self.template_name,
#                       { 'user_form' : user_form })
    
    

