from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=500)
    cep = models.BigIntegerField()
    rua = models.CharField(max_length=1000)
    cidade = models.CharField(max_length=500)
    estado = models.CharField(max_length=2)
