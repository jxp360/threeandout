from django.conf.urls import patterns, include, url


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'threeandout.views.home', name='home'),
    # url(r'^threeandout/', include('threeandout.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^threeandout/', include('test_stats.urls', namespace="threeandout")),
    url(r'^threeandout/', include('test_stats.urls',namespace="threeandout")),
    
)
