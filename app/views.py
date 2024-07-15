from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from . import models

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def get_field_names (table):
    fields = table._meta.get_fields()
    field_names = [field.verbose_name for field in fields if not (field.many_to_one or field.one_to_many) and field.name != 'id']
    return field_names

def despesas(request):
    despesas = models.Despesa.objects.all()
    return render(request, 'app/despesas.html', {'despesas': despesas, 'fields': get_field_names(models.Despesa)})

class DespesaCreateView(CreateView):
    model = models.Despesa
    fields = ['nome', 'valor', 'data', 'observacoes', 'categoria']
    template_name = 'app/add_despesa.html'
    success_url = reverse_lazy('despesas')

def entradas(request):
    entradas = models.Entrada.objects.all()
    return render(request, 'app/entradas.html', {'entradas': entradas, 'fields': get_field_names(models.Entrada)})

class EntradaCreateView(CreateView):
    model = models.Entrada
    fields = ['fonte', 'valor', 'data', 'observacoes', 'categoria']
    template_name = 'app/add_entrada.html'
    success_url = reverse_lazy('entradas')

def transacoes(request):
    transacoes = models.Transacao.objects.all()
    return render(request, 'app/transacoes.html', {'transacoes': transacoes, 'fields': get_field_names(models.Transacao)})

class TransacaoCreateView(CreateView):
    model = models.Transacao
    fields = ['nome', 'valor', 'data', 'observacoes', 'categoria']
    template_name = 'app/add_transacao.html'
    success_url = reverse_lazy('transacoes')

def relatorio_mensal(request):
    entradas_mes = (models.Transacao.objects.filter(categoria__tipo='Entrada')
    .annotate(mes=TruncMonth('data'))
    .values('mes')
    .annotate(total_entradas=Sum('valor'))
    .order_by('mes'))
    
    despesas_mes = (models.Transacao.objects.filter(categoria__tipo='Despesa')
    .annotate(mes=TruncMonth('data'))
    .values('mes')
    .annotate(total_despesas=Sum('valor'))
    .order_by('mes'))
    
    relatorio_mensal = {}
    for entrada in entradas_mes:
        mes = entrada['mes'] 
        relatorio_mensal[mes] = {
            'mes': mes.month,
            'ano': mes.year,
            'total_entradas': entrada['total_entradas'],
            'total_despesas': 0,
            'saldo_final': entrada['total_entradas']
        }
    
    for despesa in despesas_mes:
        mes = despesa['mes']
        if mes in relatorio_mensal:
            relatorio_mensal[mes]['total_despesas'] = despesa['total_despesas']
            relatorio_mensal[mes]['saldo_final'] -= despesa['total_despesas']
            
        else:
            relatorio_mensal[mes] = {
                'mes': mes.month,
                'ano': mes.year,
                'total_entradas': 0,
                'total_despesas': despesa['total_despesas'],
                'saldo_final': -despesa['total_despesas']
            }

    return render(request, 'app/relatorio_mensal.html', {'relatorio_mensal': relatorio_mensal.values()})

def metas_financeiras(request):
    metas_financeiras = models.MetaFinanceira.objects.all()
    return render(request, 'app/metas_financeiras.html', {'metas_financeiras': metas_financeiras, 'fields': get_field_names(models.MetaFinanceira)})

class MetaFinanceiraCreateView(CreateView):
    model = models.MetaFinanceira
    fields = ['nome', 'valor_total', 'meta_valor_mes']
    template_name = 'app/add_meta_financeira.html'
    success_url = reverse_lazy('metas_financeiras')
    
class MetaFinanceiraAddValueView(CreateView):
    model = models.MetaFinanceira
    fields = ['valor_guardar_mes']
    template_name = 'app/add_valor_meta_financeira.html'
    success_url = reverse_lazy('metas_financeiras')

def categorias(request):
    categorias = models.Categoria.objects.all()
    return render(request, 'app/categorias.html', {'categorias': categorias, 'fields': get_field_names(models.Categoria)})

class CategoriaCreateView(CreateView):
    model = models.Categoria
    fields = ['nome', 'tipo']
    template_name = 'app/add_categoria.html'
    success_url = reverse_lazy('categorias')