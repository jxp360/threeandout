# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.utils import timezone
#from django.core.exceptions import DoesNotExist

from test_stats.models import NFLPlayer, Picks,FFLPlayer

def index(request):
    return HttpResponse("Welcome to Three and Out Fantasy Football!!!")


def picks(request):
    return HttpResponse("Let's Make some Picks")

def submit(request,week):
    
    # Need to understand how to use login user information
    player = FFLPlayer.objects.get(name="Grant")
    
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

def picksummary(request,week):
    return HttpResponse("Thanks for making your picks for week %s" % week)

def pickweek(request, week):
    
    #week = get_object_or_404(Schedule, pk=week)
    QBs = NFLPlayer.objects.filter(position='QB')
    RBs = NFLPlayer.objects.filter(position='RB')
    WRs = NFLPlayer.objects.filter(position='WR')
    TEs = NFLPlayer.objects.filter(position='TE')
    
    return render(request, 'picks/pickweek.html', {'week':week,'QBs': QBs,'RBs': RBs,'WRs': WRs,'TEs': TEs})
    
