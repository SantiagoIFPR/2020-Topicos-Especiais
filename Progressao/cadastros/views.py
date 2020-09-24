from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.views.generic.list import ListView

from .models import Categoria, Fornecedor, Funcionario, Produto, UnidadeMedida

from django.urls import reverse_lazy

# Create your views here.
class CategoriaCreate(CreateView):
    model = Categoria
    fields = ['nome','descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-categoria')

class UnidadeMedidaCreate(CreateView):
    model = UnidadeMedida
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-unidademedida')

class ProdutoCreate(CreateView):
    model = Produto
    fields = ['nome','descricao','estoque_max','estoque_min','codigo_barras','unidademedida','categoria']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-produto')

class FuncionarioCreate(CreateView):
    model = Funcionario
    fields = ['nome_funcionario','setor_funcionario']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-funcionario')

class FornecedorCreate(CreateView):
    model = Fornecedor
    fields = ['nome','documento','cep','endereco','numero','bairro','cidade','estado','telefone','email']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-fornecedor')    

########## UPDATES ########## 
class CategoriaUpdate(UpdateView):
    model = Categoria
    fields = ['nome','descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-categoria')

class UnidadeMedidaUpdate(UpdateView):
    model = UnidadeMedida
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-unidademedida')

class ProdutoUpdate(UpdateView):
    model = Produto
    fields = ['nome','descricao','estoque_max','estoque_min','codigo_barras','unidademedida','categoria']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-produto')

class FuncionarioUpdate(UpdateView):
    model = Funcionario
    fields = ['nome_funcionario','setor_funcionario']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-funcionario')

class FornecedorUpdate(UpdateView):
    model = Fornecedor
    fields = ['nome','documento','cep','endereco','numero','bairro','cidade','estado','telefone','email']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-fornecedor')  

########## DELETE ########## 
class CategoriaDelete(DeleteView):
    model = Categoria
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-categoria')

class UnidadeMedidaDelete(DeleteView):
    model = UnidadeMedida
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-unidademedida')

class ProdutoDelete(DeleteView):
    model = Produto
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-produto')

class FuncionarioDelete(DeleteView):
    model = Funcionario
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-funcionario')

class FornecedorDelete(DeleteView):
    model = Fornecedor
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-fornecedor')

########## LISTA ########## 
class CategoriaList(ListView):
    model = Categoria
    template_name = 'cadastros/listas/categoria.html'

class UnidadeMedidaList(ListView):
    model = UnidadeMedida
    template_name = 'cadastros/listas/unidademedida.html'

class ProdutoList(ListView):
    model = Produto
    template_name = 'cadastros/listas/produto.html'

class FuncionarioList(ListView):
    model = Funcionario
    template_name = 'cadastros/listas/funcionario.html'

class FornecedorList(ListView):
    model = Fornecedor
    template_name = 'cadastros/listas/fornecedor.html'