# Generated by Django 5.0.7 on 2024-07-24 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='tipo',
            field=models.CharField(choices=[('E', 'Entrada'), ('D', 'Despesa')], verbose_name='Tipo'),
        ),
    ]
