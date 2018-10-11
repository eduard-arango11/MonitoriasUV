from django.urls import path

from Usuarios.views import *

urlpatterns = [
    path('estudiantes/registrar/', RegistrarEstudiante.as_view(), name='registrar_estudiante'),
    path('estudiantes/listar/', ListarEstudiantes.as_view(), name='listar_estudiantes'),
    path('estudiantes/editar/<int:pk>/', EditarEstudiante.as_view(), name="editar_estudiante"),
    
    path('directores/registrar/', RegistrarDirector.as_view(), name='registrar_director'),
    path('directores/listar/', ListarDirectores.as_view(), name='listar_directores'),
    path('directores/editar/<int:pk>/', EditarDirector.as_view(), name="editar_director"),
    path('directores/detalle/<int:pk>/', DetalleDirector.as_view(), name='detalle_director'),
    
    path('operarios/registrar/', RegistrarOperario.as_view(), name='registrar_operario'),
    path('operarios/listar/', ListarOperarios.as_view(), name='listar_operarios'),
    path('operarios/editar/<int:pk>/', EditarOperario.as_view(), name="editar_operario"),
    path('operarios/detalle/<int:pk>/', DetalleOperario.as_view(), name='detalle_operario'),

    path('administradores/registrar/', RegistrarAdministrador.as_view(), name='registrar_administrador'),
    path('administradores/listar/', ListarAdministradores.as_view(), name='listar_administradores'),
    path('administradores/editar/<int:pk>/', EditarAdministrador.as_view(), name="editar_administrador"),
    path('administradores/detalle/<int:pk>/', DetalleAdministrador.as_view(), name='detalle_administrador'),
]