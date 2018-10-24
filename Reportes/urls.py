from django.urls import path

from Reportes.views import *

urlpatterns = [
    path('estudiantes-registrados/', EstudiantesRegistrados.as_view(), name='estudiantes_registrados'),
    path('ofertas-registradas/', OfertasRegistradas.as_view(), name='ofertas_registradas'),
]