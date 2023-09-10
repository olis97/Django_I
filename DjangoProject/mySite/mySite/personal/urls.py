from django.urls import path

from . import views

urlpatterns = [
    path("", views.biography),
    path("token", views.token),
    path("token1", views.token1),
    
]