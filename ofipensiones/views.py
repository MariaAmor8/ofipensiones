#from django.http import HttpResponse
from django.shortcuts import render
from pago.logic.pago_logic import pagos_pendientess
from estudiante.logic.logic_estudiante import agregar_estudiantee
from cuenta.logic.cuenta_logic import crear_cuentaa
from pago.logic.pago_logic import crear_pagoo
from reporte.logic.reporte_logic import generar_reporte_estudiantee
from django.http import JsonResponse

def home(request):
    return render(request, "home.html")

def index(request):
    return render(request, "index.html")

def pagos_pendientes(request, codigo_estudiante):
    return pagos_pendientess(request, codigo_estudiante)
      
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