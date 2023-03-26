from django.urls import path
from myapi import views

urlpatterns = [
    path('myapi/', views.movies_list),
    path('myapi/<int:pk>/', views.movies_details),
]