from django.contrib import admin
from django.urls import path
from ToolsApp import views

urlpatterns = [
    path("", views.index, name='home'),
    path("tools", views.tools, name='tools'),
]