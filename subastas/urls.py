from django.urls import path
from . import views

urlpatterns = [
    path('subastas/', views.subastas, name='subastas'),
]