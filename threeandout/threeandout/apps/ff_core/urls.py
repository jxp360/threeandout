from django.conf.urls import patterns, url
from django.contrib.auth import views as authviews
from apps.ff_core import views

urlpatterns = patterns('',

    # ex: /threeandout/
    url(r'^$', views.index, name='index'),
    
    # ex: /threeandout/registerUser
    url(r'^registerUser/$', views.registerUser, name='registerUser'),
    
    # ex: /threeandout/editPreferences
    url(r'^editPreferences/$', views.editPreferences, name='editPreferences'),
    
    # ex: /threeandout/picks
    url(r'picks/$', views.picks, name='picks'),

    # ex: /threeandout/rules
    url(r'rules/$', views.rules, name='rules'),
    
    # ex: /threeandout/currentstandings
    url(r'currentstandings/$', views.currentstandings, name='currentstandings'),

    # ex: /threeandout/playoffstandings
    url(r'playoffstandings/$', views.playoffstandings, name='playoffstandings'),

    # ex: /threeandout/weeklyresultssummary
    url(r'weeklyresultssummary/$', views.weeklyresultssummary, name='weeklyresultssummary'),

    # ex: /threeandout/personalresults
    url(r'personalresults/$', views.personalresults, name='personalresults'),

    # ex: /threeandout/weeklyresults/5/
    url(r'^weeklyresults/(?P<week>\d+)/$', views.weeklyresults, name='weeklyresults'),

    
    # ex: /threeandout/picks/5/
    url(r'^picks/(?P<week>\d+)/$', views.pickweek, name='pickweek'),

    # ex: /threeandout/picks/5/submit
    url(r'^picks/(?P<week>\d+)/submit/$', views.submit, name='submit'),    
    
    # ex: /threeandout/picks/5/picksummary
    url(r'^picks/(?P<week>\d+)/picksummary/$', views.picksummary, name='picksummary'), 
    #url(r'^login/$', authviews.login, name='login'),
    
    # ex: /threeandout/selected/1
    url(r'^selected/(?P<user>\d+)/$', views.selected, name='selected'),

)
