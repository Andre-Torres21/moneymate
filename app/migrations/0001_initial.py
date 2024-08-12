# Generated by Django 5.0.8 on 2024-08-12 10:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=64, verbose_name='Nome')),
                ('tipo', models.CharField(choices=[('Entrada', 'Entrada'), ('Despesa', 'Despesa')], verbose_name='Tipo')),
                ('slug', models.SlugField(unique=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Despesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=64, verbose_name='Nome')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Valor')),
                ('data', models.DateField(verbose_name='Data')),
                ('observacoes', models.TextField(blank=True, verbose_name='Observações')),
                ('slug', models.SlugField(unique=True)),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.categoria', verbose_name='Categoria')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=64, verbose_name='Nome')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Valor')),
                ('data', models.DateField(verbose_name='Data')),
                ('observacoes', models.TextField(blank=True, verbose_name='Observações')),
                ('slug', models.SlugField(unique=True)),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.categoria', verbose_name='Categoria')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MetaFinanceira',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=64, verbose_name='Nome')),
                ('valor_total', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Valor total')),
                ('meta_valor_mes', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Meta de valor por mês')),
                ('valor_guardar_mes', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Valor a guardar no mês')),
                ('slug', models.SlugField(unique=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=64, verbose_name='Nome')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Valor')),
                ('data', models.DateField(verbose_name='Data')),
                ('observacoes', models.TextField(blank=True, verbose_name='Observações')),
                ('slug', models.SlugField(unique=True)),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.categoria', verbose_name='Categoria')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Transações',
            },
        ),
    ]
