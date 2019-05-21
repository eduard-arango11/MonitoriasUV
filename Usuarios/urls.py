from django.urls import path

from Usuarios.views import *

urlpatterns = [
    path('estudiantes/registrar/', RegistrarEstudiante.as_view(), name='registrar_estudiante'),
    path('estudiantes/listar/', ListarEstudiantes.as_view(), name='listar_estudiantes'),
    path('estudiantes/editar/<int:pk>/', EditarEstudiante.as_view(), name="editar_estudiante"),
    path('estudiantes/detalle/<int:pk>/', DetalleEstudiante.as_view(), name="detalle_estudiante"),
    path('estudiantes/eliminar_estudiante/', eliminar_estudiante, name="eliminar_estudiante"),
    
    path('directores/registrar/', RegistrarDirector.as_view(), name='registrar_director'),
    path('directores/listar/', ListarDirectores.as_view(), name='listar_directores'),
    path('directores/editar/<int:pk>/', EditarDirector.as_view(), name="editar_director"),
    path('directores/detalle/<int:pk>/', DetalleDirector.as_view(), name='detalle_director'),
    path('directores/eliminar_director/', eliminar_director, name="eliminar_director"),
    
    path('operarios/registrar/', RegistrarOperario.as_view(), name='registrar_operario'),
    path('operarios/listar/', ListarOperarios.as_view(), name='listar_operarios'),
    path('operarios/editar/<int:pk>/', EditarOperario.as_view(), name="editar_operario"),
    path('operarios/detalle/<int:pk>/', DetalleOperario.as_view(), name='detalle_operario'),
    path('operarios/eliminar_operario/', eliminar_operario, name="eliminar_operario"),

    path('administradores/registrar/', RegistrarAdministrador.as_view(), name='registrar_administrador'),
    path('administradores/listar/', ListarAdministradores.as_view(), name='listar_administradores'),
    path('administradores/editar/<int:pk>/', EditarAdministrador.as_view(), name="editar_administrador"),
    path('administradores/detalle/<int:pk>/', DetalleAdministrador.as_view(), name='detalle_administrador'),
    path('administradores/eliminar_administrador/', eliminar_administrador, name="eliminar_administrador"),

    path('registrar-d10/', RegistrarD10, name='registrar_d10'),
    path('listar-solicitudes-d10/', listarSolitudesAprobacionD10.as_view(), name='listar_solicitudes_d10'),
    path('revisar-solicitud-aprobacion-d10/<int:id_d10>/', revisarSolicitudAprobacionD10, name='revisar_solicitud_aprobacion_d10'),
]