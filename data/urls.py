from django.urls import path
from . import views

urlpatterns = [
    path('page/', views.index),
    path('collect/<str:patient>/', views.collect, name='collect'),
    path('send/', views.send),
    path('barcode/', views.barcode, name='barcode')
]