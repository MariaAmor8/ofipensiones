from django.shortcuts import render, get_object_or_404
from pago.logic.pago_logic import pagos_pendientess
from estudiante.models import Estudiante
from cuenta.models import Cuenta
from datetime import date


def estado_de_cuentaa(request, num_id_estudiante):
    # Obtener el estudiante por su numId
    estudiante = get_object_or_404(Estudiante, numId=num_id_estudiante)
    
    # Obtener la cuenta asociada al estudiante
    cuenta = get_object_or_404(Cuenta, estudiante=estudiante)
    
    # Obtener todos los pagos asociados a la cuenta
    pagos = cuenta.pagos.all()

    # Obtener la fecha actual
    fecha_actual = date.today()
    
    # Renderizar en el template 'estadoDeCuenta.html' con los datos del estudiante, la cuenta, los pagos y la fecha
    return render(request, 'estadoDeCuenta.html', {
        'estudiante': estudiante,
        'cuenta': cuenta,
        'pagos': pagos,
        'fecha_actual': fecha_actual
    })
