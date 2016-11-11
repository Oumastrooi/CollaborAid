from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
]

#urlpatterns = patterns('',
#    url(r'^register$', 'collaboraidWebsite.views.register', name='register'),
#    url(r'^login$', 'collaboraidWebsite.views.login', name='login'),
#    url(r'^logout$', 'collaboraidWebsite.views.logout', name='logout'),
#)