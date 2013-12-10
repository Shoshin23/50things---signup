from django.conf.urls import patterns, include, url


urlpatterns = patterns('launch.views',
        url(r'^success/$', 'success', name='launch_app_success'),
        url(r'^(?P<code>.+)/?$', 'home'),
        url(r'^$', 'home', name='launch_app_home'),
)
