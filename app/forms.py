from django import forms

class CadastroLoginForm(forms.Form):
    nome_usuario = forms.CharField(label='Nome de usuário')
    senha = forms.CharField(widget=forms.PasswordInput)