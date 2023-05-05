from django.urls import path
from . import views

urlpatterns = [
    path('', views.properties, name='properties'),
    path('<str:property_type>/', views.properties, name='properties_filtered'),
]