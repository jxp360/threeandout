# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to Three and Out Fantasy Football!!!")



def picks(request):
    return HttpResponse("Let's Make some Picks")