from django.db import models

# Create your models here.
class ChamadoModel(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(null=True, blank=True)
    empresa = models.CharField(max_length=100)
    email = models.EmailField()
    especialidades = models.TextField()
    localizacao = models.CharField(max_length=100)

    def __str__(self):
        return self.id