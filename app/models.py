from django.db import models
from django.urls import reverse

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=64, verbose_name='Nome')
    tipo = models.CharField(max_length=64, verbose_name='Tipo')

    def get_absolute_url(self):
        return reverse('categorias')

    def __str__(self):
        return self.nome

class Despesa(models.Model):
    nome = models.CharField(max_length=64, verbose_name='Nome')
    valor = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Valor')
    data = models.DateField(verbose_name='Data')
    observacoes = models.TextField(blank=True, verbose_name='Observações')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Categorias')

    def get_absolute_url(self):
        return reverse('despesas')

    def __str__(self):
        return self.nome

class Entrada(models.Model):
    fonte = models.CharField(max_length=64, verbose_name='Fonte')
    valor = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Valor')
    data = models.DateField(verbose_name='Data')
    observacoes = models.TextField(blank=True, verbose_name='Observações')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Categoria')

    def get_absolute_url(self):
        return reverse('entradas')

    def __str__(self):
        return self.fonte

class Transacao(models.Model):
    nome = models.CharField(max_length=64, verbose_name='Nome')
    valor = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Valor')
    data = models.DateField(verbose_name='Data')
    observacoes = models.TextField(blank=True, verbose_name='Observações')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Categoria')

    def get_absolute_url(self):
        return reverse('transacoes')

    class Meta:
        verbose_name_plural = 'Transações'

    def __str__(self):
        return self.nome

class MetaFinanceira(models.Model):
    nome = models.CharField(max_length=64, verbose_name='Nome')
    valor_total = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Valor total')
    meta_valor_mes = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Meta de valor por mês')
    valor_guardar_mes = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, verbose_name='Valor a guardar no mês')

    def get_absolute_url(self):
        return reverse('metas_financeiras')

    def __str__(self):
        return self.nome