from django.shortcuts import render, get_object_or_404, redirect
from estudiante.models import Estudiante
from cuenta.models import Cuenta
from pago.forms import PagoForm

def pagos_pendientess(request, codigo_estudiante):
    # Obtener el estudiante por su código
    estudiante = get_object_or_404(Estudiante, numId=codigo_estudiante)
    
    # Obtener la cuenta asociada al estudiante
    cuenta = get_object_or_404(Cuenta, estudiante=estudiante)
    
    # Obtener todos los pagos no pagados (estado='NOP') asociados a la cuenta
    pagos_pendientes = cuenta.pagos.filter(estado='NOP')
    
    # Renderizar en el template 'pagosPendientes.html' con los datos del estudiante y los pagos
    return render(request, 'pagosPendientes.html', {
        'estudiante': estudiante,
        'cuenta': cuenta,
        'pagos_pendientes': pagos_pendientes
    })
    
def crear_pagoo(request):
    if request.method == 'POST':
        form = PagoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/index')  # Redirigir a una página de éxito o lista de pagos
    else:
        form = PagoForm()
    return render(request, 'crear_pago.html', {'form': form})