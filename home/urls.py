"""personal_page URL Configuration


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
from django.conf.urls import url
# from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^wip/', views.wip_page, name='wip'),
    url(r'^coding/', views.coding_page, name='coding'),
    url(r'^music/', views.music_page, name='music'),
    url(r'^gaming/', views.gaming_page, name='gaming'),
    url(r'^contact/', views.contact_page, name='contact'),
    url(r'^login/', views.wd2_page, name='wd2'),
]
