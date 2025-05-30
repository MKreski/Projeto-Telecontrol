from django.urls import path
from . import views

app_name = 'telecontrol'

urlpatterns = [
    path("", views.telecontrol_home, name="home"),
    path('form/', views.telecontrol_form, name='telecontrol_form'),
    path("chamadas/", views.telecontrol_chamadas),
    path("chamados/", views.telecontrol_chamados, name='telecontrol_chamados'),
]