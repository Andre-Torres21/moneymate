from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('despesas/', views.despesas, name='despesas'),
    path('despesas/add', views.DespesaCreateView.as_view(), name='add_despesa'),
    path('entradas/', views.entradas, name='entradas'),
    path('entradas/add', views.EntradaCreateView.as_view(), name='add_entrada'),
    path('transacoes/', views.transacoes, name='transacoes'),
    path('transacoes/add', views.TransacaoCreateView.as_view(), name='add_transacao'),
    path('relatorio_mensal/', views.relatorio_mensal, name='relatorio_mensal'),
    path('metas_financeiras/', views.metas_financeiras, name='metas_financeiras'),
    path('metas_financeiras/add', views.MetaFinanceiraCreateView.as_view(), name='add_meta_financeira'),
    path('metas_financeiras/add_value', views.MetaFinanceiraAddValueView.as_view(), name='add_valor_meta_financeira'),
    path('categorias/', views.categorias, name='categorias'),
    path('categorias/add', views.CategoriaCreateView.as_view(), name='add_categoria'),
]