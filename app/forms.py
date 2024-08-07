from django import forms
from .models import *

class CadastroForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
        
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome', 'tipo']
        
class DespesaForm(forms.ModelForm):
    class Meta:
        model = Despesa
        fields = ['nome', 'valor', 'data', 'observacoes', 'categoria']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
        }
        
    def __init__(self, *args, **kwargs):
        usuario = kwargs.pop('usuario')
        super(DespesaForm, self).__init__(*args, **kwargs)
        self.fields['categoria'].queryset = Categoria.objects.filter(usuario=usuario)
        for field_name, field in self.fields.items():
            placeholder = f'Digite o {field.label.lower()}'
            field.widget.attrs['placeholder'] = placeholder
        
class EntradaForm(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = ['nome', 'valor', 'data', 'observacoes', 'categoria']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
        }
        
    def __init__(self, *args, **kwargs):
        usuario = kwargs.pop('usuario')
        super(EntradaForm, self).__init__(*args, **kwargs)
        self.fields['categoria'].queryset = Categoria.objects.filter(usuario=usuario)

class TransacaoForm(forms.ModelForm):
    class Meta:
        model = Transacao
        fields = ['nome', 'valor', 'data', 'observacoes', 'categoria']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
        }
        
    def __init__(self, *args, **kwargs):
        usuario = kwargs.pop('usuario')
        super(TransacaoForm, self).__init__(*args, **kwargs)
        self.fields['categoria'].queryset = Categoria.objects.filter(usuario=usuario)

class MetaFinanceiraForm(forms.ModelForm):
    class Meta:
        model = MetaFinanceira
        fields = ['nome', 'valor_total', 'meta_valor_mes']
        
class MetaFinanceiraFilterForm(forms.ModelForm):
    class Meta:
        model = MetaFinanceira
        fields = ['nome']