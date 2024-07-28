from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('cadastro/', cadastro, name='cadastro'),
    path('login/', LoginView.as_view(template_name='app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='app/logout.html'), name='logout'),
    
    path('despesas/', despesas, name='despesas'),
    path('despesas/add/', DespesaCreateView.as_view(), name='add_despesa'),
    path('despesas/<slug:slug>/', DespesaUpdateView.as_view(), name='update_despesa'),
    path('despesas/<slug:slug>/delete/', DespesaDeleteView.as_view(), name='delete_despesa'),
    
    path('entradas/', entradas, name='entradas'),
    path('entradas/add/', EntradaCreateView.as_view(), name='add_entrada'),
    path('entradas/<slug:slug>/', EntradaUpdateView.as_view(), name='update_entrada'),
    path('entradas/<slug:slug>/delete/', EntradaDeleteView.as_view(), name='delete_entrada'),
    
    path('transacoes/', transacoes, name='transacoes'),
    path('transacoes/add/', TransacaoCreateView.as_view(), name='add_transacao'),
    path('transacoes/<slug:slug>/', TransacaoUpdateView.as_view(), name='update_transacao'),
    path('transacoes/<slug:slug>/delete/', TransacaoDeleteView.as_view(), name='delete_transacao'),
    
    path('metas_financeiras/', metas_financeiras, name='metas_financeiras'),
    path('metas_financeiras/add/', MetaFinanceiraCreateView.as_view(), name='add_meta_financeira'),
    path('metas_financeiras/<slug:slug>/', MetaFinanceiraUpdateView.as_view(), name='update_meta_financeira'),
    path('metas_financeiras/update_value/<slug:slug>/', MetaFinanceiraUpdateValueView.as_view(), name='update_valor_meta_financeira'),
    path('metas_financeiras/<slug:slug>/delete/', MetaFinanceiraDeleteView.as_view(), name='delete_meta_financeira'),
    
    path('categorias/', categorias, name='categorias'),
    path('categorias/add/', CategoriaCreateView.as_view(), name='add_categoria'),
    path('categorias/<slug:slug>/', CategoriaUpdateView.as_view(), name='update_categoria'),
    path('categorias/<slug:slug>/delete/', CategoriaDeleteView.as_view(), name='delete_categoria'),
    
    path('relatorio_mensal/', relatorio_mensal, name='relatorio_mensal'),
]