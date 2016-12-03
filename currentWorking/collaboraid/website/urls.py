from django.conf.urls import url
from website import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'about/$', views.about, name='about'),
    url(r'^register_profile/$', views.register_profile, name='register_profile'),
    url(r'^profile/(?P<username>[\w\-]+)/$', views.profile, name='profile'),
    url(r'^profiles/$', views.list_profiles, name='list_profiles'),
    url(r'^events/$', views.list_events, name='list_events'),
    url(r'^create_event/$', views.register_event, name = 'create_event'),
    url(r'^create_complete/$', views.event_complete, name = 'created_event'),
    url(r'^events/(?P<id>\d+)/$', views.detail, name='event_detail'),
    url(r'^events/join/(?P<event_id>\d+)/$', views.join, name='event_join'),
    url(r'^events/cancel/(?P<event_id>\d+)/$', views.cancel, name='event_cancel'),

]
