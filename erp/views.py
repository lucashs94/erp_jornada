from django.shortcuts import render
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DetailView
from django.views.generic.edit import DeleteView
from django.http import Http404, HttpRequest, HttpResponseRedirect

from .models import Funcionario, Produto, Venda
from .forms import FuncionarioForm, ProdutoForm



# AUTH

class ErpLoginView(LoginView):
    template_name = 'erp/auth/login.html'
    success_url = reverse_lazy('erp:dashboard')
    redirect_authenticated_user = True


class ErpLogoutView(LogoutView):
    template_name = 'erp/auth/logout.html'


class HomeView(TemplateView):
    template_name = 'erp/index.html'
    
    
    
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'erp/dashboard.html'
    


## FUNCIONARIOS VIEWS ##
@login_required
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
        

@login_required
def lista_funcionarios(request: HttpRequest):
    if request.method == 'GET':
        funcionarios = Funcionario.objects.all()

        context = {'funcionarios': funcionarios}

        return render(request, 'erp/funcionarios/lista.html', context)
    

@login_required
def busca_funcionario_id(request: HttpRequest, pk: int):
    if request.method == 'GET':
        try:
            funcionario = Funcionario.objects.get(pk=pk)
        except Funcionario.DoesNotExist:
            funcionario = None

        context = {'funcionario': funcionario}

        return render(request, 'erp/funcionarios/detalhe.html', context)
    

@login_required
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
class ProdutoCreateView(LoginRequiredMixin, CreateView):
    template_name = 'erp/produtos/novo.html'
    model = Produto
    form_class = ProdutoForm
    success_url = reverse_lazy('erp:home')


class ProdutoListView(LoginRequiredMixin, ListView):
    model = Produto
    template_name = 'erp/produtos/lista.html'
    context_object_name = 'produtos'
    
    
class ProdutoUpdateView(LoginRequiredMixin, UpdateView):
    model = Produto
    template_name = 'erp/produtos/atualiza.html'
    form_class = ProdutoForm
    success_url = reverse_lazy('erp:lista_produtos')
    
    
class ProdutoDetailView(LoginRequiredMixin, DetailView):
    model = Produto
    template_name = 'erp/produtos/detalhe.html'
    context_object_name = 'produto'
    
    
    def get_object(self, queryset=None):            # Sobrescrevendo metodo da classe DETAILVIEW para capturar o erro e mudar o retorno
        try:
            return super().get_object(queryset)
        except Http404:
            return None
        
        
class ProdutoDeleteView(LoginRequiredMixin, DeleteView):
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

class VendaCreateView(LoginRequiredMixin, CreateView):
    model = Venda
    template_name = 'erp/vendas/novo.html'
    success_url = reverse_lazy('erp:lista_vendas')
    fields = ['funcionario','produto']
    
    
class VendaListView(LoginRequiredMixin, ListView):
    model = Venda
    template_name = 'erp/vendas/lista.html'
    context_object_name = 'vendas'
    
    
class VendaDateilView(LoginRequiredMixin, DetailView):
    model = Venda
    template_name = 'erp/vendas/detalhe.html'
    context_object_name = 'venda'
    
    def get_object(self, queryset=None):            # Sobrescrevendo metodo da classe DETAILVIEW para capturar o erro e mudar o retorno
        try:
            return super().get_object(queryset)
        except Http404:
            return None
        
        
class VendaUpdateView(LoginRequiredMixin, UpdateView):
    model = Venda
    template_name = 'erp/vendas/atualiza.html'
    fields = ['funcionario','produto']
    success_url = reverse_lazy('erp:lista_vendas')
    
    
class VendaDeleteView(LoginRequiredMixin, DeleteView):
    model = Venda
    template_name = 'erp/vendas/deleta.html'
    context_object_name = 'venda'
    success_url = reverse_lazy('erp:lista_vendas')
    
    
    def get_object(self, queryset=None):            # Sobrescrevendo metodo da classe DETAILVIEW para capturar o erro e mudar o retorno
        try:
            return super().get_object(queryset)
        except Http404:
            return None