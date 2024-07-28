from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.
class Categoria(models.Model):
    tipos_despesa = {
        'Entrada': 'Entrada',
        'Despesa': 'Despesa'
    }
    nome = models.CharField(max_length=64, verbose_name='Nome')
    tipo = models.CharField(choices=tipos_despesa, verbose_name='Tipo')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(null=True)

    def get_absolute_url(self):
        return reverse('categorias')
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.nome

class Despesa(models.Model):
    nome = models.CharField(max_length=64, verbose_name='Nome')
    valor = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Valor')
    data = models.DateField(verbose_name='Data')
    observacoes = models.TextField(blank=True, verbose_name='Observações')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, verbose_name='Categoria')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(null=True)

    def get_absolute_url(self):
        return reverse('despesas')
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.nome

class Entrada(models.Model):
    fonte = models.CharField(max_length=64, verbose_name='Fonte')
    valor = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Valor')
    data = models.DateField(verbose_name='Data')
    observacoes = models.TextField(blank=True, verbose_name='Observações')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, verbose_name='Categoria')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(null=True)
    
    def get_absolute_url(self):
        return reverse('entradas')
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.fonte)

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.fonte

class Transacao(models.Model):
    nome = models.CharField(max_length=64, verbose_name='Nome')
    valor = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Valor')
    data = models.DateField(verbose_name='Data')
    observacoes = models.TextField(blank=True, verbose_name='Observações')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, verbose_name='Categoria')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(null=True)
    
    def get_absolute_url(self):
        return reverse('transacoes')
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)

        return super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Transações'

    def __str__(self):
        return self.nome

class MetaFinanceira(models.Model):
    nome = models.CharField(max_length=64, verbose_name='Nome')
    valor_total = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Valor total')
    meta_valor_mes = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Meta de valor por mês')
    valor_guardar_mes = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, verbose_name='Valor a guardar no mês')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(null=True)
    
    def get_absolute_url(self):
        return reverse('metas_financeiras')
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.nome