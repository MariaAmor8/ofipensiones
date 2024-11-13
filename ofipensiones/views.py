#from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from pago.logic.pago_logic import pagos_pendientess
from estudiante.logic.logic_estudiante import agregar_estudiantee, asociar_pagos_a_cuenta
from cuenta.logic.cuenta_logic import crear_cuentaa
from pago.logic.pago_logic import crear_pagoo, modificar_pago
from reporte.logic.reporte_logic import generar_reporte_estudiantee
from django.http import JsonResponse
from ofipensiones.auth0backend import getRole
from estudiante.models import Estudiante
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "home.html")

def index(request):
    return render(request, "index.html")

@login_required
def pagos_pendientes(request, codigo_estudiante):
    role = getRole(request)
    if role == "Padre familia":
        return pagos_pendientess(request, codigo_estudiante)
    else:
        return HttpResponse("Unauthorized User")
      
def healthCheck(request):
    return JsonResponse({'message': 'OK'}, status=200)

def agregar_estudiante(request):
    return agregar_estudiantee(request)


def crear_cuenta(request):
    return crear_cuentaa(request)


def crear_pago(request):
    return crear_pagoo(request)

def generar_reporte_estudiante(request, numId):
   return generar_reporte_estudiantee(request,numId)

@login_required
def asociar_pago_a_cuenta(request, numId):
    return asociar_pagos_a_cuenta(request, numId)

@login_required
def modificar_pagos(request, pago_id, codigo_estudiante):
    role = getRole(request)
    if role == "Administrador":
        return modificar_pago(request, pago_id, codigo_estudiante)
    else:
        return HttpResponse("Unauthorized User")
 
@login_required       
def homePagosPendientes(request):
    return render(request, "homePagosPendientes.html")

@login_required
def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'listaEstudiantes.html', {'estudiantes': estudiantes})