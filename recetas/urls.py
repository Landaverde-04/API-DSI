from django.urls import path
from . import views

urlpatterns = [
    path('registrar_receta/', views.registrar_receta, name='registrar_receta'),
    path('lista_recetas/', views.lista_recetas, name='lista_recetas'),
    path("recetas/eliminar/<int:id>/", views.eliminar_receta, name="eliminar_receta"),
]
