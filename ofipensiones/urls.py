"""
URL configuration for ofipensiones project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from . import views
from .views import pagos_pendientes, agregar_estudiante, crear_cuenta, crear_pago

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('index/', views.index),
    path('pagos_pendientes/<str:codigo_estudiante>/', pagos_pendientes, name='pagos_pendientes'),
    path('health-check/', views.healthCheck),
    path('agregar-estudiante/', agregar_estudiante, name='agregar_estudiante'),
    path('crear-cuenta/', crear_cuenta, name='crear_cuenta'),
    path('crear-pago/', crear_pago, name='crear_pago'),
    path('reporte-estudiante/<int:numId>/', views.generar_reporte_estudiante, name='reporte_estudiante'),
]
