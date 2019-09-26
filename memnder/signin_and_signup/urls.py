from django.contrib import admin
from django.urls import path,include
from . import views

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
	path('api/login/', obtain_auth_token),
	path('api/signup/', views.signup),
]