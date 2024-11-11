from django.shortcuts import render, get_object_or_404, redirect
from cuenta.forms import CuentaForm
    
def crear_cuentaa(request):
    if request.method == 'POST':
        form = CuentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirigir a una página de éxito o lista de cuentas
    else:
        form = CuentaForm()
    return render(request, 'crear_cuenta.html', {'form': form})
