from django.urls import path
from . import views

urlpatterns = [
    path('tasacion/', views.tasacion, name='tasacion'),
]