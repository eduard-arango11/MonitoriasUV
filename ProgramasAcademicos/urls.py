from django.urls import path

from ProgramasAcademicos.views import *

urlpatterns = [
    path('registrar/', RegistrarPrograma.as_view(), name='registrar_programa'),
    path('listar/', ListarProgramas.as_view(), name='listar_programas'),
    path('editar/<int:pk>/', EditarPrograma.as_view(), name="editar_programa"),
    path('eliminar_programa/', eliminar_programa, name="eliminar_programa"),
]