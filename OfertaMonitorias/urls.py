from django.urls import path

from OfertaMonitorias.views import *
from django.conf.urls import url, include

urlpatterns = [
    path('ofertas/registrar/', RegistrarOferta.as_view(), name='registrar_oferta'),
    path('ofertas/listar/', ListarOfertas.as_view(), name='listar_ofertas'),
    path('ofertas/detalle/<int:pk>/', DetalleOferta.as_view(), name='detalle_oferta'),
    path('ofertas/editar/<int:pk>/', EditarOferta.as_view(), name="editar_oferta"),

    path('aplicaciones/listar/', ListarAplicaciones.as_view(), name='listar_aplicaciones'),
    path('aplicaciones/detalle/<int:pk>/', DetalleAplicacion.as_view(), name='detalle_aplicacion'),
    path('aplicaciones-oferta/<int:id_oferta>/', listar_aplicaciones_oferta, name='aplicaciones_oferta'),
    path('aplicar-a-oferta/<int:pk>/', AplicarOferta, name="aplicar_oferta"),
    path('cancelar-apliacion/<int:id_oferta>/', cancelar_aplicacion, name="cancelar_aplicacion"),
    path('estudiantes-con-d10/', listar_estudiantes_d10, name='estudiantes_con_d10'),
]