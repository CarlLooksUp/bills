from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^billentry/', include('billentry.urls')),
    # url(r'^bills/', include('bills.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'login/?$', 'django.contrib.auth.views.login', 
                {'template_name': 'user/login.html'}), 
    (r'logout/?$', 'django.contrib.auth.views.logout', 
                {'template_name': 'user/logout.html'}),
)

#unsafe version of static file serving for development purposes
urlpatterns += staticfiles_urlpatterns()
