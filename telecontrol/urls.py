from django.urls import path
from . import views
urlpatterns = [
    path("", views.telecontrol_home),
    path("form/", views.telecontrol_form),
    path("chamadas/", views.telecontrol_chamadas),
    path("chamados/", views.telecontrol_chamados),
]