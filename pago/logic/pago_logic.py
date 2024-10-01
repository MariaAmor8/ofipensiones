from django.shortcuts import render, get_object_or_404
from pago.models import Pago
from estudiante.models import Estudiante
from cuenta.models import Cuenta
from datetime import date

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