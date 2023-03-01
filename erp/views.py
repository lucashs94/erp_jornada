from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DetailView
from django.views.generic.edit import DeleteView
from django.http import Http404, HttpRequest, HttpResponseRedirect

from .models import Funcionario, Produto, Venda
from .forms import FuncionarioForm, ProdutoForm


# Create your views here.
# def home(request: HttpRequest):
#     if request.method == 'GET':
#         return render(request,'erp/index.html')

class HomeView(TemplateView):
    template_name = 'erp/index.html'
    

def cria_funcionario(request: HttpRequest):
    if request.method == 'GET':
        form = FuncionarioForm()

        context = {
            'form': form,
        }

        return render(request,'erp/funcionarios/novo.html', context)

    if request.method == 'POST':
        form = FuncionarioForm(request.POST)

        if form.is_valid():
            funcionario = Funcionario(**form.cleaned_data)
            funcionario.save()

            return HttpResponseRedirect(redirect_to='/')
        

def lista_funcionarios(request: HttpRequest):
    if request.method == 'GET':
        funcionarios = Funcionario.objects.all()

        context = {'funcionarios': funcionarios}

        return render(request, 'erp/funcionarios/lista.html', context)
    

def busca_funcionario_id(request: HttpRequest, pk: int):
    if request.method == 'GET':
        try:
            funcionario = Funcionario.objects.get(pk=pk)
        except Funcionario.DoesNotExist:
            funcionario = None

        context = {'funcionario': funcionario}

        return render(request, 'erp/funcionarios/detalhe.html', context)
    

def atualiza_funcionario(request:HttpRequest, pk:int):
    if request.method == 'GET':
        funcionario = Funcionario.objects.get(pk=pk)
        form = FuncionarioForm(instance=funcionario)
        
        context = {'form': form}

        return render(request, 'erp/funcionarios/atualiza.html', context)
    
    if request.method == 'POST':
        funcionario = Funcionario.objects.get(pk=pk)
        form = FuncionarioForm(request.POST, instance=funcionario)

        if form.is_valid():
            form.save()

        return HttpResponseRedirect(redirect_to=f'/funcionarios/detalhe/{pk}')
    

# Views de Produtos
class ProdutoCreateView(CreateView):
    template_name = 'erp/produtos/novo.html'
    model = Produto
    form_class = ProdutoForm
    success_url = reverse_lazy('erp:home')


class ProdutoListView(ListView):
    model = Produto
    template_name = 'erp/produtos/lista.html'
    context_object_name = 'produtos'
    
    
class ProdutoUpdateView(UpdateView):
    model = Produto
    template_name = 'erp/produtos/atualiza.html'
    form_class = ProdutoForm
    success_url = reverse_lazy('erp:lista_produtos')
    
    
class ProdutoDetailView(DetailView):
    model = Produto
    template_name = 'erp/produtos/detalhe.html'
    context_object_name = 'produto'
    
    
    def get_object(self, queryset=None):            # Sobrescrevendo metodo da classe DETAILVIEW para capturar o erro e mudar o retorno
        try:
            return super().get_object(queryset)
        except Http404:
            return None
        
        
class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = 'erp/produtos/deleta.html'
    context_object_name = 'produto'
    success_url = reverse_lazy('erp:lista_produtos')
    
    
    def get_object(self, queryset=None):            # Sobrescrevendo metodo da classe DETAILVIEW para capturar o erro e mudar o retorno
        try:
            return super().get_object(queryset)
        except Http404:
            return None
        
        

# VIEWS DE VENDAS

class VendaCreateView(CreateView):
    model = Venda
    template_name = 'erp/vendas/novo.html'
    success_url = reverse_lazy('erp:lista_vendas')
    fields = ['funcionario','produto']
    
    
class VendaListView(ListView):
    model = Venda
    template_name = 'erp/vendas/lista.html'
    context_object_name = 'vendas'
    
    
class VendaDateilView(DetailView):
    model = Venda
    template_name = 'erp/vendas/detalhe.html'
    context_object_name = 'venda'
    
    def get_object(self, queryset=None):            # Sobrescrevendo metodo da classe DETAILVIEW para capturar o erro e mudar o retorno
        try:
            return super().get_object(queryset)
        except Http404:
            return None
        
        
class VendaUpdateView(UpdateView):
    model = Venda
    template_name = 'erp/vendas/atualiza.html'
    fields = ['funcionario','produto']
    success_url = reverse_lazy('erp:lista_vendas')
    
    
class VendaDeleteView(DeleteView):
    model = Venda
    template_name = 'erp/vendas/deleta.html'
    context_object_name = 'venda'
    success_url = reverse_lazy('erp:lista_vendas')
    
    
    def get_object(self, queryset=None):            # Sobrescrevendo metodo da classe DETAILVIEW para capturar o erro e mudar o retorno
        try:
            return super().get_object(queryset)
        except Http404:
            return None