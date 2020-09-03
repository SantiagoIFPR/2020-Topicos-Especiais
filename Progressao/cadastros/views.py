from django.views.generic.edit import CreateView, UpdateView

from .models import Categoria, Fornecedor, Funcionario, Produto, UnidadeMedida

from django.urls import reverse_lazy

# Create your views here.
class CategoriaCreate(CreateView):
    model = Categoria
    fields = ['nome','descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class UnidadeMedidaCreate(CreateView):
    model = UnidadeMedida
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class ProdutoCreate(CreateView):
    model = Produto
    fields = ['nome','descricao','estoque_max','estoque_min','codigo_barras','unidademedida','categoria']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class FuncionarioCreate(CreateView):
    model = Funcionario
    fields = ['nome_funcionario','setor_funcionario']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class FornecedorCreate(CreateView):
    model = Fornecedor
    fields = ['nome','documento','cep','endereco','numero','bairro','cidade','estado','telefone','email']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')    

########## UPDATES ########## 
class CategoriaUpdate(UpdateView):
    model = Categoria
    fields = ['nome','descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class UnidadeMedidaUpdate(UpdateView):
    model = UnidadeMedida
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class ProdutoUpdate(UpdateView):
    model = Produto
    fields = ['nome','descricao','estoque_max','estoque_min','codigo_barras','unidademedida','categoria']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class FuncionarioUpdate(UpdateView):
    model = Funcionario
    fields = ['nome_funcionario','setor_funcionario']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class FornecedorUpdate(UpdateView):
    model = Fornecedor
    fields = ['nome','documento','cep','endereco','numero','bairro','cidade','estado','telefone','email']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')  