"""tracer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from tracer1 import views

urlpatterns = [
    url(r'^$', views.welcome),
    url(r'^facebook/$', views.facebook_list),
    url(r'^linkedin/$', views.linkedIn_list),
    url(r'^twitter/$', views.twitter_list),
    url(r'^pinterest/$', views.pinterest_list),
    url(r'^googleplus/$', views.gplus_list),
    url(r'^bing/$', views.bing_list),
    url(r'^all/$', views.all_list),
]

urlpatterns = format_suffix_patterns(urlpatterns)
