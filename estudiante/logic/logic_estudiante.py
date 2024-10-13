from ..models import Estudiante
from estudiante.forms import EstudianteForm
from django.shortcuts import render, redirect

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