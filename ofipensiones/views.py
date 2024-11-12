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

def home(request):
    return render(request, "home.html")

def index(request):
    return render(request, "index.html")

#@login_required
def pagos_pendientes(request, codigo_estudiante):
    #role = getRole(request)
    #if role == "Padre familia":
    return pagos_pendientess(request, codigo_estudiante)
    #else:
        #return HttpResponse("Unauthorized User")
      
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

def asociar_pago_a_cuenta(request, numId):
    return asociar_pagos_a_cuenta(request, numId)

def modificar_pagos(request, pago_id, codigo_estudiante):
    return modificar_pago(request, pago_id, codigo_estudiante)