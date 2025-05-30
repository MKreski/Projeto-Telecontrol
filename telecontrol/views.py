from django.shortcuts import render, redirect
from .forms import ChamadoForm
from .models import ChamadoModel
from django.http import HttpRequest

# Create your views here.
def telecontrol_home(request):
    return render(request, 'HTML/login.html')

def telecontrol_form(request: HttpRequest):
    if request.method == 'POST':
        form = ChamadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('telecontrol:telecontrol_chamados')	    
    else:
        form = ChamadoForm()
    context = {
        'form': ChamadoForm
    }
    return render(request, 'HTML/form.html', context)
    
def telecontrol_chamadas(request):
    return render(request, 'HTML/chamadas_tc.html')

def telecontrol_chamados(request):
    context = {
        'chamados': ChamadoModel.objects.all()
    }
    return render(request, 'HTML/chamados.html', context)