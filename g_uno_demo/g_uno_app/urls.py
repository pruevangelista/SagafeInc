"""
URL configuration for g_uno_demo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.urls import path 
from . import views

urlpatterns = [ 
    path('', views.tries, name = 'tries'),
    path('dr_home', views.dr_home, name = 'dr_home'),
    path('add_dr', views.add_dr, name='add_dr'), 
    path('new_dr', views.new_dr, name='new_dr'), #implement pk 
]
