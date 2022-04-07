from django.urls import path
from Familia import views

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('papa/', views.papa, name='Papa'),
    path('mama/', views.mama, name='Mama'),
    path('hija/', views.hija, name='Hija'),
]


