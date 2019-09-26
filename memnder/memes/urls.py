from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
	path('api/create/', views.create_mem),
	path('api/get/', views.get_mem),
	path('api/like/', views.like_mem),
]