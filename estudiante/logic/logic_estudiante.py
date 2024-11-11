from ..models import Estudiante
from estudiante.forms import EstudianteForm
from django.shortcuts import render, redirect, get_object_or_404
from cuenta.models import Cuenta
from pago.models import Pago


def get_estudiantes():
    queryset = Estudiante.objects.all()
    return (queryset)


def create_estudiante(form):
    estudiante = form.save()
    estudiante.save()
    return ()


def agregar_estudiantee(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/index')  # Redirigir a una página de éxito o lista de estudiantes
    else:
        form = EstudianteForm()
    return render(request, 'agregar_estudiante.html', {'form': form})


def asociar_pagos_a_cuenta(request, numId):
    # Obtiene el estudiante por numId
    estudiante = get_object_or_404(Estudiante, numId=numId)
    
    # Obtiene la cuenta asociada al estudiante
    cuenta = get_object_or_404(Cuenta, estudiante=estudiante)
    
    # Obtiene todos los pagos disponibles
    pagos_disponibles = Pago.objects.all()

    if request.method == 'POST':
        # Obtiene los pagos seleccionados del formulario
        pagos_seleccionados = request.POST.getlist('pagos')
        
        # Asocia cada pago a la cuenta
        for pago_id in pagos_seleccionados:
            pago = get_object_or_404(Pago, id=pago_id)
            cuenta.pagos.add(pago)
        
        return redirect('index/')  # Redirige a una página de éxito tras asociar los pagos

    return render(request, 'asociar_pagos_estudiante.html', {
        'estudiante': estudiante,
        'cuenta': cuenta,
        'pagos_disponibles': pagos_disponibles
    })