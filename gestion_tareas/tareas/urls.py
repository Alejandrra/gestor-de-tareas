# tareas/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tareas, name='lista_tareas'),
    path('completar/<int:tarea_id>/', views.completar_tarea, name='completar_tarea'),
    path('eliminar/<int:tarea_id>/', views.eliminar_tarea, name='eliminar_tarea'),
    path('registro/', views.registro, name='registro'),  # Agregar esta línea
]
