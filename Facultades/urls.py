from django.urls import path

from Facultades.views import *

urlpatterns = [
    path('registrar/', RegistrarFacultad.as_view(), name='registrar_facultad'),
    path('listar/', ListarFacultades.as_view(), name='listar_facultades'),
    path('editar/<int:pk>/', EditarFacultad.as_view(), name="editar_facultad"),
]