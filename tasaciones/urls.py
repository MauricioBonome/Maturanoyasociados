from django.urls import path
from . import views

urlpatterns = [
    path('solicitar-tasacion/', views.solicitar_tasacion, name='solicitar_tasacion'),
]