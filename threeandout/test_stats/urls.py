from django.conf.urls import patterns, url

from test_stats import views

urlpatterns = patterns('',
    # ex: /threeandout/
    url(r'^$', views.index, name='index'),
    # ex: /threeandout/picks
    url(r'picks/$', views.picks, name='picks'),
    
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
    )