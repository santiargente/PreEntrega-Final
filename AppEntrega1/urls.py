"""Entrega1Argente URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from . views import vista_inicio, vista_referencias, registro_profesores, registro_alumnos, registro_tutores, busqueda_alumnos, busqueda_profesores, busqueda_tutores

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', vista_inicio, name="Inicio"),
    path('referencias/', vista_referencias, name="Referencias"),
    path('registroprofesores/', registro_profesores, name="Registro_Profesores"),
    path('regsitrotutores/', registro_tutores, name="Registro_Tutores"),
    path('registroalumnos/', registro_alumnos, name="Registro_Alumnos"),
    path('busquedaalumnos/', busqueda_alumnos, name="Busqueda_Alumnos"),
    path('busquedaprofesores/', busqueda_profesores, name="Busqueda_Profesores"),
    path('busquedatutores/', busqueda_tutores, name="Busqueda_Tutores")
    
]
