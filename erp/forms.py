from django import forms

from .models import Funcionario, Produto


class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario    
        fields = "__all__"


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = "__all__"
        labels = {
            'descricao' : 'Descrição',
            'preco' : 'Preço',
        }