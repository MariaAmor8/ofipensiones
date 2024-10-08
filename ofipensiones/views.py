from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from pago.logic.pago_logic import pagos_pendientess
from estudiante.models import Estudiante
from cuenta.logic.cuenta_logic import estado_de_cuentaa
from datetime import date

def home(request):
    return HttpResponse("Hello world! django views")

def index(request):
    return render(request, "index.html")

def pagos_pendientes(request, codigo_estudiante):
    return pagos_pendientess(request, codigo_estudiante)
    
def estado_de_cuenta(request, num_id_estudiante):
   return estado_de_cuentaa(request, num_id_estudiante)

def healthCheck(request):
    return HttpResponse('ok')