from django.conf.urls import patterns, include, url


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(
    '',
    #url(r'^$', include('kpWebApp.urls')),
    url(r'^accounts/', include('registration.urls')),
    # Examples:
    # url(r'^$', 'kharchapaani.views.home', name='home'),
    # url(r'^kharchapaani/', include('kharchapaani.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
