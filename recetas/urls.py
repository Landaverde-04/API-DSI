from django.urls import path
from . import views

urlpatterns = [
    path('registrar_receta/', views.registrar_receta, name='registrar_receta'),
]
