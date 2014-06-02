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
    url(r'^threeandout/', include('apps.ff_core.urls',namespace="threeandout")),
    url(r'^threeandout/login/$', 'django.contrib.auth.views.login',{'template_name':"picks/login.html"}),
    url(r'^threeandout/logout/$', 'django.contrib.auth.views.logout',{'next_page': '/threeandout/login/'}),
    url(r'^threeandout/password/reset/$', 'django.contrib.auth.views.password_reset', {'template_name': "registration/password_reset_form.html", 'post_reset_redirect' : '/threeandout/password/reset/done/'}, name="password_reset"),
    url(r'^threeandout/password/reset/done/$', 'django.contrib.auth.views.password_reset_done'),
    url(r'^threeandout/password/reset/(?P<uidb36>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 'django.contrib.auth.views.password_reset_confirm', {'post_reset_redirect' : '/threeandout/password/done/'}, name="password_reset_confirm"),
    url(r'^threeandout/password/done/$', 'django.contrib.auth.views.password_reset_complete'),
    url(r'^threeandout/password/change/$', 'django.contrib.auth.views.password_change',{'template_name':"registration/password_change_form.html"}),
    url(r'^threeandout/password/change/done/$', 'django.contrib.auth.views.password_change_done', {'template_name':"registration/password_change_done.html"}),

)
