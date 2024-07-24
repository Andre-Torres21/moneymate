from django import forms

class CadastroForm(forms.Form):
    nome = forms.CharField(max_length=64)
    nome_usuario = forms.CharField(label='Nome de usuário')
    senha = forms.CharField(widget=forms.PasswordInput)