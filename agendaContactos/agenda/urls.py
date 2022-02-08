from unicodedata import name
from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('prueba/', views.inicio, name='inicio'),
    path('', views.index, name='index'),
    path('crea/', views.crea, name='crea'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('busqueda/', views.busqueda, name='busqueda'),
    path('buscar/', views.buscar, name='buscar'),
    path('mostrarbusqueda/', views.buscar, name='mostrarbusqueda')
]