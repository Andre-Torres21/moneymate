from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Despesa)
admin.site.register(Entrada)
admin.site.register(Transacao)
admin.site.register(MetaFinanceira)