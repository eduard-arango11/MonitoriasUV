"""monitorias URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views
from Usuarios.forms import IniciarSesionForm

urlpatterns = [
    path('usuarios/', include('Usuarios.urls')),
    path('facultades/', include('Facultades.urls')),
    path('programas/', include('ProgramasAcademicos.urls')),
    path('dependencias/', include('Dependencias.urls')),
    path('unidades/', include('UnidadesAcademicas.urls')),
    path('monitorias/', include('OfertaMonitorias.urls')),
    path('reportes/', include('Reportes.urls')),
    path('admin/', admin.site.urls),
    path('login/', views.login, {'template_name': 'login.html', 'authentication_form': IniciarSesionForm}, name='login'),
    path('logout/', views.logout, name='logout'),
]
