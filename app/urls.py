from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('despesas/', views.despesas, name='despesas'),
    path('despesas/add/', views.DespesaCreateView.as_view(), name='add_despesa'),
    path('despesas/<int:pk>/', views.DespesaUpdateView.as_view(), name='update_despesa'),
    path('despesas/<int:pk>/delete/', views.DespesaDeleteView.as_view(), name='delete_despesa'),
    
    path('entradas/', views.entradas, name='entradas'),
    path('entradas/add/', views.EntradaCreateView.as_view(), name='add_entrada'),
    path('entradas/<int:pk>/', views.EntradaUpdateView.as_view(), name='update_entrada'),
    path('entradas/<int:pk>/delete/', views.EntradaDeleteView.as_view(), name='delete_entrada'),
    
    path('transacoes/', views.transacoes, name='transacoes'),
    path('transacoes/add/', views.TransacaoCreateView.as_view(), name='add_transacao'),
    path('transacoes/<int:pk>/', views.TransacaoUpdateView.as_view(), name='update_transacao'),
    path('transacoes/<int:pk>/delete/', views.TransacaoDeleteView.as_view(), name='delete_transacao'),
    
    path('metas_financeiras/', views.metas_financeiras, name='metas_financeiras'),
    path('metas_financeiras/add/', views.MetaFinanceiraCreateView.as_view(), name='add_meta_financeira'),
    path('metas_financeiras/<int:pk>/', views.MetaFinanceiraUpdateView.as_view(), name='update_meta_financeira'),
    path('metas_financeiras/update_value/<int:pk>/', views.MetaFinanceiraUpdateValueView.as_view(), name='update_valor_meta_financeira'),
    path('metas_financeiras/<int:pk>/delete/', views.MetaFinanceiraDeleteView.as_view(), name='delete_meta_financeira'),
    
    path('categorias/', views.categorias, name='categorias'),
    path('categorias/add/', views.CategoriaCreateView.as_view(), name='add_categoria'),
    path('categorias/<int:pk>/', views.CategoriaUpdateView.as_view(), name='update_categoria'),
    path('categorias/<int:pk>/delete/', views.CategoriaDeleteView.as_view(), name='delete_categoria'),
    
    path('relatorio_mensal/', views.relatorio_mensal, name='relatorio_mensal'),
]