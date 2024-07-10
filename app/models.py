from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=64)
    tipo = models.CharField(max_length=64)

    def __str__(self):
        return self.nome

class Despesa(models.Model):
    nome = models.CharField(max_length=64)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    data = models.DateField()
    observacoes = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Entrada(models.Model):
    fonte = models.CharField(max_length=64)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    data = models.DateField()
    observacoes = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.fonte

class Transacao(models.Model):
    nome = models.CharField(max_length=64)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    data = models.DateField()
    observacoes = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Transações'

    def __str__(self):
        return self.nome

class MetaFinanceira(models.Model):
    nome = models.CharField(max_length=64)
    valor_total = models.DecimalField(max_digits=8, decimal_places=2)
    meta_valor_mes = models.DecimalField(max_digits=8, decimal_places=2)
    valor_guardar_mes = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.nome