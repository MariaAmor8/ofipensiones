from ..models import Estudiante

def get_estudiantes():
    queryset = Estudiante.objects.all()
    return (queryset)


def create_estudiante(form):
    estudiante = form.save()
    estudiante.save()
    return ()