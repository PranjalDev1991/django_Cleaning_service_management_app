"""Relcleancom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path('',views.index, name='Home'),
    #path('home1',views.home1, name='home1'),
    path('about',views.about, name='AboutUs'),
    path('apart',views.apart, name='apart'),
    path('window',views.window, name='window'),
    path('resid',views.resid, name='resid'),
    path('commer',views.commer, name='commer'),
    path('renov',views.renov, name='renov'),
    path('services',views.services, name='Services'),
    path('pricing',views.pricing, name='Our Prices'),
    path('contact',views.contact, name='Contact'),
    path('login',views.login, name='Login'),
    path('register',views.Register,name='register'),
    path('home1', views.home1, name='home1'),
    path('logout', views.logout, name='logout'),
    path('clean_search', views.clean_search, name='clean_search')

]
