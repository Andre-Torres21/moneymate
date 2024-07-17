from collections import OrderedDict
from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import *

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def get_field_names(table):
    fields = table._meta.get_fields()
    field_names = [field.verbose_name for field in fields if not (field.many_to_one or field.one_to_many) and field.name != 'id']
    return field_names

def despesas(request):
    despesas = Despesa.objects.all()
    return render(request, 'app/despesas.html', {'despesas': despesas, 'fields': get_field_names(Despesa)})

class DespesaCreateView(CreateView):
    model = Despesa
    fields = '__all__'
    template_name = 'app/add_despesa.html'
    
class DespesaUpdateView(UpdateView):
    model = Despesa
    fields = '__all__'
    template_name = 'app/update_despesa.html'
    
class DespesaDeleteView(DeleteView):
    model = Despesa
    success_url = reverse_lazy('despesas')

def entradas(request):
    entradas = Entrada.objects.all()
    return render(request, 'app/entradas.html', {'entradas': entradas, 'fields': get_field_names(Entrada)})

class EntradaCreateView(CreateView):
    model = Entrada
    fields = '__all__'
    template_name = 'app/add_entrada.html'
    
class EntradaUpdateView(UpdateView):
    model = Entrada
    fields = '__all__'
    template_name = 'app/update_entrada.html'
    
class EntradaDeleteView(DeleteView):
    model = Entrada
    success_url = reverse_lazy('entradas')

def transacoes(request):
    transacoes = Transacao.objects.order_by('data')
    return render(request, 'app/transacoes.html', {'transacoes': transacoes, 'fields': get_field_names(Transacao)})

class TransacaoCreateView(CreateView):
    model = Transacao
    fields = '__all__'
    template_name = 'app/add_transacao.html'
    
class TransacaoUpdateView(UpdateView):
    model = Transacao
    fields = '__all__'
    template_name = 'app/update_transacao.html'
    
class TransacaoDeleteView(DeleteView):
    model = Transacao
    success_url = reverse_lazy('transacoes')

def metas_financeiras(request):
    metas_financeiras = MetaFinanceira.objects.all()
    return render(request, 'app/metas_financeiras.html', {'metas_financeiras': metas_financeiras, 'fields': get_field_names(MetaFinanceira)})

class MetaFinanceiraCreateView(CreateView):
    model = MetaFinanceira
    fields = ['nome', 'valor_total', 'meta_valor_mes']
    template_name = 'app/add_meta_financeira.html'
    
class MetaFinanceiraUpdateView(UpdateView):
    model = MetaFinanceira
    fields = ['nome', 'valor_total', 'meta_valor_mes']
    template_name = 'app/update_meta_financeira.html'
    
class MetaFinanceiraUpdateValueView(UpdateView):
    model = MetaFinanceira
    fields = ['valor_guardar_mes']
    template_name = 'app/update_valor_meta_financeira.html'
    
class MetaFinanceiraDeleteView(DeleteView):
    model = MetaFinanceira
    success_url = reverse_lazy('metas_financeiras')

def categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'app/categorias.html', {'categorias': categorias, 'fields': get_field_names(Categoria)})

class CategoriaCreateView(CreateView):
    model = Categoria
    fields = '__all__'
    template_name = 'app/add_categoria.html'
    
class CategoriaUpdateView(UpdateView):
    model = Categoria
    fields = '__all__'
    template_name = 'app/update_categoria.html'
    
class CategoriaDeleteView(DeleteView):
    model = Categoria
    success_url = reverse_lazy('categorias')
    
def relatorio_mensal(request):
    entradas_mes = (Transacao.objects.filter(categoria__tipo='Entrada')
    .annotate(mes=TruncMonth('data'))
    .values('mes')
    .annotate(total_entradas=Sum('valor'))
    .order_by('mes'))
    
    despesas_mes = (Transacao.objects.filter(categoria__tipo='Despesa')
    .annotate(mes=TruncMonth('data'))
    .values('mes')
    .annotate(total_despesas=Sum('valor'))
    .order_by('mes'))
    
    relatorio_mensal = OrderedDict()
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

    sorted_relatorio_mensal = sorted(relatorio_mensal.items())
    return render(request, 'app/relatorio_mensal.html', {'relatorio_mensal': [relatorio[1] for relatorio in sorted_relatorio_mensal]})