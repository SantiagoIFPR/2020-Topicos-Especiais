from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.views.generic.list import ListView

from .models import Categoria, Fornecedor, Funcionario, Produto, UnidadeMedida

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class CategoriaCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Categoria
    fields = ['nome','descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-categoria')

class UnidadeMedidaCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = UnidadeMedida
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-unidademedida')

class ProdutoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Produto
    fields = ['nome','descricao','estoque_max','estoque_min','codigo_barras','unidademedida','categoria']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-produto')

class FuncionarioCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Funcionario
    fields = ['nome_funcionario','setor_funcionario']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-funcionario')

class FornecedorCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Fornecedor
    fields = ['nome','documento','cep','endereco','numero','bairro','cidade','estado','telefone','email']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-fornecedor')    

########## UPDATES ########## 
class CategoriaUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Categoria
    fields = ['nome','descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-categoria')

class UnidadeMedidaUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = UnidadeMedida
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-unidademedida')

class ProdutoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Produto
    fields = ['nome','descricao','estoque_max','estoque_min','codigo_barras','unidademedida','categoria']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-produto')

class FuncionarioUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Funcionario
    fields = ['nome_funcionario','setor_funcionario']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-funcionario')

class FornecedorUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Fornecedor
    fields = ['nome','documento','cep','endereco','numero','bairro','cidade','estado','telefone','email']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-fornecedor')  

########## DELETE ########## 
class CategoriaDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Categoria
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-categoria')

class UnidadeMedidaDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = UnidadeMedida
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-unidademedida')

class ProdutoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Produto
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-produto')

class FuncionarioDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Funcionario
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-funcionario')

class FornecedorDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Fornecedor
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-fornecedor')

########## LISTA ########## 
class CategoriaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Categoria
    template_name = 'cadastros/listas/categoria.html'

class UnidadeMedidaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = UnidadeMedida
    template_name = 'cadastros/listas/unidademedida.html'

class ProdutoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Produto
    template_name = 'cadastros/listas/produto.html'

class FuncionarioList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Funcionario
    template_name = 'cadastros/listas/funcionario.html'

class FornecedorList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Fornecedor
    template_name = 'cadastros/listas/fornecedor.html'