from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def telecontrol_home(request):
    return render(request, 'HTML/login.html')

def telecontrol_form(request):
    return render(request, 'HTML/form.html')
    
def telecontrol_chamadas(request):
    return render(request, 'HTML/chamadas_tc.html')

def telecontrol_chamados(request):
    return render(request, 'HTML/chamados.html')