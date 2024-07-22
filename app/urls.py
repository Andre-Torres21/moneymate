from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('cadastro/', cadastro, name='cadastro'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('despesas/', despesas, name='despesas'),
    path('despesas/add/', DespesaCreateView.as_view(), name='add_despesa'),
    path('despesas/<int:pk>/', DespesaUpdateView.as_view(), name='update_despesa'),
    path('despesas/<int:pk>/delete/', DespesaDeleteView.as_view(), name='delete_despesa'),
    
    path('entradas/', entradas, name='entradas'),
    path('entradas/add/', EntradaCreateView.as_view(), name='add_entrada'),
    path('entradas/<int:pk>/', EntradaUpdateView.as_view(), name='update_entrada'),
    path('entradas/<int:pk>/delete/', EntradaDeleteView.as_view(), name='delete_entrada'),
    
    path('transacoes/', transacoes, name='transacoes'),
    path('transacoes/add/', TransacaoCreateView.as_view(), name='add_transacao'),
    path('transacoes/<int:pk>/', TransacaoUpdateView.as_view(), name='update_transacao'),
    path('transacoes/<int:pk>/delete/', TransacaoDeleteView.as_view(), name='delete_transacao'),
    
    path('metas_financeiras/', metas_financeiras, name='metas_financeiras'),
    path('metas_financeiras/add/', MetaFinanceiraCreateView.as_view(), name='add_meta_financeira'),
    path('metas_financeiras/<int:pk>/', MetaFinanceiraUpdateView.as_view(), name='update_meta_financeira'),
    path('metas_financeiras/update_value/<int:pk>/', MetaFinanceiraUpdateValueView.as_view(), name='update_valor_meta_financeira'),
    path('metas_financeiras/<int:pk>/delete/', MetaFinanceiraDeleteView.as_view(), name='delete_meta_financeira'),
    
    path('categorias/', categorias, name='categorias'),
    path('categorias/add/', CategoriaCreateView.as_view(), name='add_categoria'),
    path('categorias/<int:pk>/', CategoriaUpdateView.as_view(), name='update_categoria'),
    path('categorias/<int:pk>/delete/', CategoriaDeleteView.as_view(), name='delete_categoria'),
    
    path('relatorio_mensal/', relatorio_mensal, name='relatorio_mensal'),
]