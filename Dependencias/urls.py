from django.urls import path

from Dependencias.views import *

urlpatterns = [
    path('registrar/', RegistrarDependencia.as_view(), name='registrar_dependencia'),
    path('listar/', ListarDependencias.as_view(), name='listar_dependencias'),
    path('editar/<int:pk>/', EditarDependencia.as_view(), name="editar_dependencia"),
]