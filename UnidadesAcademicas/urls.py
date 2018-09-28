from django.urls import path

from UnidadesAcademicas.views import *

urlpatterns = [
    path('registrar/', RegistrarUnidad.as_view(), name='registrar_unidad'),
    path('listar/', ListarUnidades.as_view(), name='listar_unidades'),
    path('editar/<int:pk>/', EditarUnidad.as_view(), name="editar_unidad"),
]