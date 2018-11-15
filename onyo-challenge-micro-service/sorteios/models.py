from django.db import models

# Create your models here.


class Sorteio(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    nome = models.CharField(max_length=100)
    minimo = models.IntegerField()
    maximo = models.IntegerField()
    quantidadeValores = models.IntegerField()
    owner = models.IntegerField()
    realizado = models.BooleanField(default=False)
    data_realizado = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ('createdAt',)

    def __str__(self):
        return 'Sorteio {} com {} número(s) de {} a {}'.format(self.nome, self.quantidadeValores, self.minimo, self.maximo)


class Resultado(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    sorteio = models.ForeignKey(Sorteio, on_delete=models.CASCADE)
    resultado = models.CharField(max_length=255)

    class Meta:
        ordering = ('createdAt',)

    def __str__(self):
        return 'Resultado {} para {}'.format(self.resultado, self.sorteio.__str__())
