from collections import OrderedDict
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .forms import *
from .models import *

@login_required
def index(request):
    return render(request, 'app/index.html')

class CadastroView(CreateView):
    form_class = CadastroForm
    template_name = 'app/cadastro.html'
    success_url = reverse_lazy('login')
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse_lazy('index'))
        return super().get(request, *args, **kwargs)
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        return super().form_valid(form)

class CustomLoginView(LoginView):
    template_name = 'app/login.html'
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse_lazy('index'))
        return super().dispatch(request, *args, **kwargs)

def get_field_names(model):
    fields = model._meta.get_fields()
    field_names = []
    
    for field in fields:
        if field.name == 'id' or field.name == 'usuario' or field.name == 'slug':
            continue
        if field.many_to_one and not field.auto_created:  # Campo ForeignKey
            field_names.append(field.verbose_name)
        elif not field.many_to_one and not field.one_to_many:  # Outros campos
            field_names.append(field.verbose_name)
    
    return field_names

@login_required
def categorias(request):
    categorias = Categoria.objects.filter(usuario=request.user).order_by('nome')
    form = CategoriaForm()
    if request.method == 'POST':
        categoria = form.save(commit=False)
        categoria.usuario = request.user
        nome = request.POST.get('nome')
        tipo = request.POST.get('tipo')
        if nome or tipo:
            if nome:
                categorias = categorias.filter(nome__icontains=nome)
            if tipo:
                categorias = categorias.filter(tipo__icontains=tipo)
    return render(request, 'app/categorias.html', {'categorias': categorias, 'field_names': get_field_names(Categoria), 'form': form})

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
    despesas = Despesa.objects.filter(usuario=request.user).order_by('data')
    form = DespesaForm(usuario=request.user)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        valor = request.POST.get('valor')
        data = request.POST.get('data')
        observacoes = request.POST.get('observacoes')
        categoria = request.POST.get('categoria')
        
        if nome or valor or data or observacoes or categoria:
            if nome:
                despesas = despesas.filter(nome__icontains=nome)
            if valor:
                despesas = despesas.filter(valor__icontains=valor)
            if data:
                despesas = despesas.filter(data=data)
            if observacoes:
                despesas = despesas.filter(observacoes__icontains=observacoes)
            if categoria:
                despesas = despesas.filter(categoria=categoria)
    return render(request, 'app/despesas.html', {'despesas': despesas, 'field_names': get_field_names(Despesa), 'form': form})

class DespesaCreateView(LoginRequiredMixin, CreateView):
    model = Despesa
    form_class = DespesaForm
    template_name = 'app/add_despesa.html'
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)
    
    def get_form_kwargs(self):
            kwargs = super().get_form_kwargs()
            kwargs['usuario'] = self.request.user
            return kwargs
    
class DespesaUpdateView(LoginRequiredMixin, UpdateView):
    model = Despesa
    form_class = DespesaForm
    template_name = 'app/update_despesa.html'
    
    def get_form_kwargs(self):
            kwargs = super().get_form_kwargs()
            kwargs['usuario'] = self.request.user
            return kwargs

class DespesaDeleteView(LoginRequiredMixin, DeleteView):
    model = Despesa
    success_url = reverse_lazy('despesas')
    template_name = 'app/delete_despesa.html'

@login_required
def entradas(request):
    entradas = Entrada.objects.filter(usuario=request.user).order_by('data')
    form = EntradaForm(usuario=request.user)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        valor = request.POST.get('valor')
        data = request.POST.get('data')
        observacoes = request.POST.get('observacoes')
        categoria = request.POST.get('categoria')
        
        if nome or valor or data or observacoes or categoria:
            if nome:
                entradas = entradas.filter(nome__icontains=nome)
            if valor:
                entradas = entradas.filter(valor__icontains=valor)
            if data:
                entradas = entradas.filter(data=data)
            if observacoes:
                entradas = entradas.filter(observacoes__icontains=observacoes)
            if categoria:
                entradas = entradas.filter(categoria=categoria)
    return render(request, 'app/entradas.html', {'entradas': entradas, 'field_names': get_field_names(Entrada), 'form': form})

class EntradaCreateView(LoginRequiredMixin, CreateView):
    model = Entrada
    form_class = EntradaForm
    template_name = 'app/add_entrada.html'
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)
    
    def get_form_kwargs(self):
            kwargs = super().get_form_kwargs()
            kwargs['usuario'] = self.request.user
            return kwargs
    
class EntradaUpdateView(LoginRequiredMixin, UpdateView):
    model = Entrada
    form_class = EntradaForm
    template_name = 'app/update_entrada.html'
    
    def get_form_kwargs(self):
            kwargs = super().get_form_kwargs()
            kwargs['usuario'] = self.request.user
            return kwargs

class EntradaDeleteView(LoginRequiredMixin, DeleteView):
    model = Entrada
    success_url = reverse_lazy('entradas')
    template_name = 'app/delete_entrada.html'

@login_required
def transacoes(request):
    transacoes = Transacao.objects.filter(usuario=request.user).order_by('data')
    form = TransacaoForm(usuario=request.user)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        valor = request.POST.get('valor')
        data = request.POST.get('data')
        observacoes = request.POST.get('observacoes')
        categoria = request.POST.get('categoria')
        
        if nome or valor or data or observacoes or categoria:
            if nome:
                transacoes = transacoes.filter(nome__icontains=nome)
            if valor:
                transacoes = transacoes.filter(valor__icontains=valor)
            if data:
                transacoes = transacoes.filter(data=data)
            if observacoes:
                transacoes = transacoes.filter(observacoes__icontains=observacoes)
            if categoria:
                transacoes = transacoes.filter(categoria=categoria)
    return render(request, 'app/transacoes.html', {'transacoes': transacoes, 'field_names': get_field_names(Transacao), 'form': form})

class TransacaoCreateView(LoginRequiredMixin, CreateView):
    model = Transacao
    form_class = TransacaoForm
    template_name = 'app/add_transacao.html'
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)
    
    def get_form_kwargs(self):
            kwargs = super().get_form_kwargs()
            kwargs['usuario'] = self.request.user
            return kwargs

class TransacaoUpdateView(LoginRequiredMixin, UpdateView):
    model = Transacao
    form_class = TransacaoForm
    template_name = 'app/update_transacao.html'
    
    def get_form_kwargs(self):
            kwargs = super().get_form_kwargs()
            kwargs['usuario'] = self.request.user
            return kwargs

class TransacaoDeleteView(LoginRequiredMixin, DeleteView):
    model = Transacao
    success_url = reverse_lazy('transacoes')
    template_name = 'app/delete_transacao.html'

@login_required
def metas_financeiras(request):
    metas_financeiras = MetaFinanceira.objects.filter(usuario=request.user).order_by('nome')
    form = MetaFinanceiraFilterForm()
    if request.method == 'POST':
        meta_financeira = form.save(commit=False)
        meta_financeira.usuario = request.user
        nome = request.POST.get('nome')
        if nome:
            metas_financeiras = metas_financeiras.filter(nome__icontains=nome)
    return render(request, 'app/metas_financeiras.html', {'metas_financeiras': metas_financeiras, 'field_names': get_field_names(MetaFinanceira), 'form': form})

class MetaFinanceiraCreateView(LoginRequiredMixin, CreateView):
    model = MetaFinanceira
    form_class = MetaFinanceiraForm
    template_name = 'app/add_meta_financeira.html'
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class MetaFinanceiraUpdateView(LoginRequiredMixin, UpdateView):
    model = MetaFinanceira
    form_class = MetaFinanceiraForm
    template_name = 'app/update_meta_financeira.html'
    
class MetaFinanceiraUpdateValueView(LoginRequiredMixin, UpdateView):
    model = MetaFinanceira
    fields = ['valor_guardar_mes']
    template_name = 'app/update_valor_meta_financeira.html'

class MetaFinanceiraDeleteView(LoginRequiredMixin, DeleteView):
    model = MetaFinanceira
    success_url = reverse_lazy('metas_financeiras')
    template_name = 'app/delete_meta_financeira.html'

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