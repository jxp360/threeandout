from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'threeandout.views.home', name='home'),
    # url(r'^threeandout/', include('threeandout.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^$', RedirectView.as_view(url=reverse_lazy('threeandout:index'))),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^threeandout/', include('test_stats.urls', namespace="threeandout")),
    url(r'^threeandout/', include('test_stats.urls',namespace="threeandout")),
    url(r'^threeandout/login/$', 'django.contrib.auth.views.login',{'template_name':"picks/login.html"}),
    #url(r'^threeandout/login/$', 'django.contrib.auth.views.login'),
    url(r'^threeandout/logout/$', 'django.contrib.auth.views.logout',{'next_page': '/threeandout/login/'})
)
