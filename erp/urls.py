from django.urls import path
from .views import HomeView, cria_funcionario, lista_funcionarios, \
    busca_funcionario_id, atualiza_funcionario, \
    ProdutoCreateView, ProdutoListView, ProdutoUpdateView, ProdutoDetailView, ProdutoDeleteView

app_name = 'erp'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    # Funcionários
    path('funcionarios/novo', cria_funcionario, name='novo_funcionario'),
    path('funcionarios/lista', lista_funcionarios, name='lista_funcionarios'),
    path('funcionarios/detalhe/<int:pk>', busca_funcionario_id, name='busca_funcionaruio'),
    path('funcionarios/atualiza/<int:pk>', atualiza_funcionario, name='atualiza_funcionario'),
    
    # Produtos
    path('produtos/novo', ProdutoCreateView.as_view(), name='novo_produto'),
    path('produtos', ProdutoListView.as_view(), name='lista_produtos'),
    path('produtos/atualiza/<int:pk>', ProdutoUpdateView.as_view(), name='atualiza_produto'),
    path('produtos/detalhe/<int:pk>', ProdutoDetailView.as_view(), name='detalhe_produto'),
    path('produtos/deleta/<int:pk>', ProdutoDeleteView.as_view(), name='deleta_produto'),
]