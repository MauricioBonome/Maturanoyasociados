from django.urls import path
from . import views

urlpatterns = [
    path('', views.properties, name='properties'),
    path('<str:property_type>/', views.properties, name='properties_filtered'),
    path('search/', views.search, name='nombre_de_la_vista_de_busqueda'),
    path('properties/search/', views.search, name='search'),
    path('property/<int:property_id>/', views.property_detail, name='property_detail'),
    path('venta/', views.venta, name='venta'),
    path('venta/success/', views.venta_success, name='venta_success'),
]
