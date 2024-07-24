from collections import OrderedDict
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .forms import *
from .models import *

@login_required
def index(request):
    return render(request, 'app/index.html')

def cadastro(request):
    form = CadastroForm()
    if request.method == 'POST':
        nome_usuario = request.POST.get('nome_usuario')
        senha = request.POST.get('senha')
        # if User.objects.get(username=nome_usuario).exists():
        #     messages.error(request, 'Usuário já cadastrado!')
        # else:
        User.objects.create_user(username=nome_usuario, password=senha)
        messages.success(request, 'Usuário cadastrado com sucesso!')
        return redirect(reverse('login'))
    return render(request, 'app/cadastro.html', {'form': form})

def get_field_names(model):
    fields = model._meta.get_fields()
    field_names = []
    
    for field in fields:
        if field.name == 'id' or field.name == 'usuario':
            continue
        if field.many_to_one and not field.auto_created:  # Campo ForeignKey
            field_names.append(field.verbose_name)
        elif not field.many_to_one and not field.one_to_many:  # Outros campos
            field_names.append(field.verbose_name)
    
    return field_names

@login_required
def categorias(request):
    categorias = Categoria.objects.filter(usuario=request.user)
    return render(request, 'app/categorias.html', {'categorias': categorias, 'fields': get_field_names(Categoria)})

class CategoriaCreateView(LoginRequiredMixin, CreateView):
    model = Categoria
    fields = ['nome', 'tipo']
    template_name = 'app/add_categoria.html'
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class CategoriaUpdateView(LoginRequiredMixin, UpdateView):
    model = Categoria
    fields = ['nome', 'tipo']
    template_name = 'app/update_categoria.html'

class CategoriaDeleteView(LoginRequiredMixin, DeleteView):
    model = Categoria
    success_url = reverse_lazy('categorias')
    template_name = 'app/delete_categoria.html'

@login_required
def despesas(request):
    despesas = Despesa.objects.filter(usuario=request.user)
    return render(request, 'app/despesas.html', {'despesas': despesas, 'fields': get_field_names(Despesa)})

class DespesaCreateView(LoginRequiredMixin, CreateView):
    model = Despesa
    fields = ['nome', 'valor', 'data', 'observacoes', 'categoria']
    template_name = 'app/add_despesa.html'
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)
    
class DespesaUpdateView(LoginRequiredMixin, UpdateView):
    model = Despesa
    fields = ['nome', 'valor', 'data', 'observacoes', 'categoria']
    template_name = 'app/update_despesa.html'

class DespesaDeleteView(LoginRequiredMixin, DeleteView):
    model = Despesa
    success_url = reverse_lazy('despesas')

@login_required
def entradas(request):
    entradas = Entrada.objects.filter(usuario=request.user)
    return render(request, 'app/entradas.html', {'entradas': entradas, 'fields': get_field_names(Entrada)})

class EntradaCreateView(LoginRequiredMixin, CreateView):
    model = Entrada
    fields = ['fonte', 'valor', 'data', 'observacoes', 'categoria']
    template_name = 'app/add_entrada.html'
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)
    
class EntradaUpdateView(LoginRequiredMixin, UpdateView):
    model = Entrada
    fields = ['fonte', 'valor', 'data', 'observacoes', 'categoria']
    template_name = 'app/update_entrada.html'

class EntradaDeleteView(LoginRequiredMixin, DeleteView):
    model = Entrada
    success_url = reverse_lazy('entradas')

@login_required
def transacoes(request):
    transacoes = Transacao.objects.filter(usuario=request.user).order_by('data')
    return render(request, 'app/transacoes.html', {'transacoes': transacoes, 'fields': get_field_names(Transacao)})

class TransacaoCreateView(LoginRequiredMixin, CreateView):
    model = Transacao
    fields = ['nome', 'valor', 'data', 'observacoes', 'categoria']
    template_name = 'app/add_transacao.html'
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class TransacaoUpdateView(LoginRequiredMixin, UpdateView):
    model = Transacao
    fields = ['nome', 'valor', 'data', 'observacoes', 'categoria']
    template_name = 'app/update_transacao.html'

class TransacaoDeleteView(LoginRequiredMixin, DeleteView):
    model = Transacao
    success_url = reverse_lazy('transacoes')

@login_required
def metas_financeiras(request):
    metas_financeiras = MetaFinanceira.objects.filter(usuario=request.user)
    return render(request, 'app/metas_financeiras.html', {'metas_financeiras': metas_financeiras, 'fields': get_field_names(MetaFinanceira)})

class MetaFinanceiraCreateView(LoginRequiredMixin, CreateView):
    model = MetaFinanceira
    fields = ['nome', 'valor_total', 'meta_valor_mes']
    template_name = 'app/add_meta_financeira.html'
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class MetaFinanceiraUpdateView(LoginRequiredMixin, UpdateView):
    model = MetaFinanceira
    fields = ['nome', 'valor_total', 'meta_valor_mes']
    template_name = 'app/update_meta_financeira.html'

class MetaFinanceiraUpdateValueView(LoginRequiredMixin, UpdateView):
    model = MetaFinanceira
    fields = ['valor_guardar_mes']
    template_name = 'app/update_valor_meta_financeira.html'

class MetaFinanceiraDeleteView(LoginRequiredMixin, DeleteView):
    model = MetaFinanceira
    success_url = reverse_lazy('metas_financeiras')

@login_required
def relatorio_mensal(request):
    entradas_mes = (Transacao.objects.filter(usuario=request.user, categoria__tipo='Entrada')
    .annotate(mes=TruncMonth('data'))
    .values('mes')
    .annotate(total_entradas=Sum('valor'))
    .order_by('mes'))
    
    despesas_mes = (Transacao.objects.filter(usuario=request.user, categoria__tipo='Despesa')
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