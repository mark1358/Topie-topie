"""Topie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from ast import pattern
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from hw import views



urlpatterns = [
    path('admin/', admin.site.urls),
    url('^$', views.index),
    url('^chassis/$', views.Chassis),
    url('^cpu/$', views.CPU),
    url('^hdd/$', views.HDD),
    url('^ssd/$', views.SSD),
    url('^login/$', views.Login),
    url('^logout/$', views.Logout),
    url('^signup/$', views.Signup),
    url('^MB/$', views.MB1),
    url('^Memory/$', views.Memory1),
    url('^Power/$', views.Power1),
    url('^display/$', views.Display),
    url('^listone/$', views.Listone),
]
