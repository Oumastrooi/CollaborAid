#!python
# website/urls.py
from django.conf.urls import url, include
from . import views
from django.contrib import admin


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
	#url(r'^admin/', include(admin.site.urls)),
]
