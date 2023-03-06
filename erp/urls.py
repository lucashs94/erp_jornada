from django.urls import path
from django.conf.urls.static import static
from core import settings
from .views import HomeView, cria_funcionario, lista_funcionarios, \
    busca_funcionario_id, atualiza_funcionario, \
    ProdutoCreateView, ProdutoListView, ProdutoUpdateView, ProdutoDetailView, ProdutoDeleteView, \
    VendaCreateView, VendaListView, VendaDateilView, VendaUpdateView, VendaDeleteView

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
    
    # Vendas
    path('vendas', VendaListView.as_view(), name='lista_vendas'),
    path('vendas/novo', VendaCreateView.as_view(), name='novo_venda'),
    path('vendas/detalhe/<int:pk>', VendaDateilView.as_view(), name='detalhe_venda'),
    path('vendas/atualiza/<int:pk>', VendaUpdateView.as_view(), name='atualiza_venda'),
    path('vendas/deleta/<int:pk>', VendaDeleteView.as_view(), name='deleta_venda'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)