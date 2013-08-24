from django.conf.urls import patterns, url

from test_stats import views

urlpatterns = patterns('',
    # ex: /threeandout/
    url(r'^$', views.index, name='index'),
    # ex: /threeandout/picks
    url(r'picks/$', views.picks, name='picks'),
    
    # ex: /polls/5/
    #url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
    
    )