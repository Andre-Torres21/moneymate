from django import forms
from .models import *

class CadastroForm(forms.Form):
    nome = forms.CharField(max_length=64)
    nome_usuario = forms.CharField(label='Nome de usuário')
    senha = forms.CharField(widget=forms.PasswordInput)
        
class DespesaForm(forms.ModelForm):
    class Meta:
        model = Despesa
        fields = ['nome', 'valor', 'data', 'observacoes', 'categoria']
        
    def __init__(self, *args, **kwargs):
        usuario = kwargs.pop('usuario')
        super(DespesaForm, self).__init__(*args, **kwargs)
        self.fields['categoria'].queryset = Categoria.objects.filter(usuario=usuario)
        
class EntradaForm(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = ['fonte', 'valor', 'data', 'observacoes', 'categoria']
        
    def __init__(self, *args, **kwargs):
        usuario = kwargs.pop('usuario')
        super(EntradaForm, self).__init__(*args, **kwargs)
        self.fields['categoria'].queryset = Categoria.objects.filter(usuario=usuario)

class TransacaoForm(forms.ModelForm):
    class Meta:
        model = Transacao
        fields = ['nome', 'valor', 'data', 'observacoes', 'categoria']
        
    def __init__(self, *args, **kwargs):
        usuario = kwargs.pop('usuario')
        super(TransacaoForm, self).__init__(*args, **kwargs)
        self.fields['categoria'].queryset = Categoria.objects.filter(usuario=usuario)

class MetaFinanceiraForm(forms.ModelForm):
    class Meta:
        model = MetaFinanceira
        fields = ['nome', 'valor_total', 'meta_valor_mes']
        
    def __init__(self, *args, **kwargs):
        usuario = kwargs.pop('usuario')
        super(MetaFinanceiraForm, self).__init__(*args, **kwargs)
        self.fields['categoria'].queryset = Categoria.objects.filter(usuario=usuario)