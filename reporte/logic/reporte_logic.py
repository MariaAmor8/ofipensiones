from django.shortcuts import render, get_object_or_404
from estudiante.models import Estudiante
from cuenta.models import Cuenta
from reporte.models import EstadoCuenta

def generar_reporte_estudiantee(request, numId):
    # Obtener el estudiante por ID
    estudiante = get_object_or_404(Estudiante, numId=numId)
    
    # Obtener la cuenta asociada al estudiante
    cuenta = get_object_or_404(Cuenta, estudiante=estudiante)
    
    # Obtener los pagos relacionados con la cuenta
    pagos = cuenta.pagos.all()  # Relación ManyToMany con Pago
    
    # Crear un nuevo reporte para el estudiante
    reporte = EstadoCuenta.objects.create(
        estudiante=estudiante,
        emisor="Administrador",  # Puedes cambiar esto según el contexto del emisor
    )
    
    # Preparar el contexto con los datos del estudiante, pagos, cuenta y reporte
    context = {
        'estudiante': estudiante,
        'cuenta': cuenta,
        'pagos': pagos,
        'reporte': reporte,
    }
    
    # Renderizar el template HTML
    return render(request, 'reporte_estudiante.html', context)