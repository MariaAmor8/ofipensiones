from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from pago.logic.pago_logic import pagos_pendientess
from estudiante.models import Estudiante
from estudiante.forms import EstudianteForm
from cuenta.forms import CuentaForm
from pago.forms import PagoForm
from cuenta.logic.cuenta_logic import estado_de_cuentaa
from datetime import date
from django.shortcuts import render, redirect

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

def agregar_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirigir a una página de éxito o lista de estudiantes
    else:
        form = EstudianteForm()
    return render(request, 'agregar_estudiante.html', {'form': form})


def crear_cuenta(request):
    if request.method == 'POST':
        form = CuentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cuentas')  # Redirigir a una página de éxito o lista de cuentas
    else:
        form = CuentaForm()
    return render(request, 'crear_cuenta.html', {'form': form})


def crear_pago(request):
    if request.method == 'POST':
        form = PagoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pagos')  # Redirigir a una página de éxito o lista de pagos
    else:
        form = PagoForm()
    return render(request, 'crear_pago.html', {'form': form})