from django.conf.urls import patterns, url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

urlpatterns = patterns('',
    url(r'^register$', 'collaboraidWebsite.views.register', name='register'),
    url(r'^login$', 'collaboraidWebsite.views.login', name='login'),
    url(r'^logout$', 'collaboraidWebsite.views.logout', name='logout'),
)