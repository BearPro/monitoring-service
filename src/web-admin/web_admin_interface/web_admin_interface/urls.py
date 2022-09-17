from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from api_for_admin.models import Users, Tokens
    
urlpatterns = [
    path('', include('api_for_admin.urls')),
]
