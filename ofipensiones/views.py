#from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from pago.logic.pago_logic import pagos_pendientess
from estudiante.logic.logic_estudiante import agregar_estudiantee, asociar_pagos_a_cuenta
from cuenta.logic.cuenta_logic import crear_cuentaa
from pago.logic.pago_logic import crear_pagoo, modificar_pago
from reporte.logic.reporte_logic import generar_reporte_estudiantee
from django.http import JsonResponse
from ofipensiones.auth0backend import getRole, getEmail
from estudiante.models import Estudiante
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "home.html")

def index(request):
    return render(request, "index.html")

@login_required
def pagos_pendientes(request):
    role = getRole(request)
    if role == "Padre familia":
        emailUsuario = getEmail(request)
        codigo_estudiante = request.GET.get('codigo_estudiante')  # Obtener el código desde GET
        try:
            estudiante = Estudiante.objects.get(numId=codigo_estudiante)
            emailPadreFam = estudiante.emailPadreFamilia
            if emailUsuario == emailPadreFam:
                return pagos_pendientess(request, codigo_estudiante)
            else:
                return render(request, 'error.html')
        except Estudiante.DoesNotExist:
            return render(request, 'error.html', {'mensaje': 'Estudiante no encontrado'})
    else:
        return render(request, 'error.html', {'mensaje': 'No autorizado'})
      
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

@login_required 
def asociar_pago_a_cuenta(request, numId):
    role = getRole(request)
    #solo el administrador puede asociar un pago a una cuenta de un estudiante - funciona
    if role == "Administrador": 
        return asociar_pagos_a_cuenta(request, numId)
    else:
        return render(request, 'error.html')

@login_required
def modificar_pagos(request, pago_id, codigo_estudiante):
    role = getRole(request)
    #solo el administrador modificar un pago - no funciona
    if role == "Administrador":
        return modificar_pago(request, pago_id, codigo_estudiante)
    else:
        return render(request, 'error.html')
 
@login_required       
def homePagosPendientes(request):
    role = getRole(request)
    #solo el administrador modificar un pago - funciona
    if role == "Padre familia":
        return render(request, "homePagosPendientes.html")
    else:
        return render(request, 'error.html')

@login_required
def lista_estudiantes(request):
    role = getRole(request)
    if role == "Administrador":
        estudiantes = Estudiante.objects.all()
        return render(request, 'listaEstudiantes.html', {'estudiantes': estudiantes})
    else:
        return render(request, 'error.html')
    
