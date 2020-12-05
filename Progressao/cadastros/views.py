from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.views.generic.list import ListView

from .models import Categoria, Fornecedor, Funcionario, Produto, UnidadeMedida

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from braces.views import GroupRequiredMixin

# Create your views here.
class CategoriaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
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

    def form_valid(self, form):

        #Antes do super o meu objeto equipamento ainda não foi criado nem salvo no banco.
        form.instance.usuario = self.request.user

        url = super().form_valid(form)

        #Depois do super o objeto está criado.
        return url

class FuncionarioCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
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

    def form_valid(self, form):

        #Antes do super o meu objeto equipamento ainda não foi criado nem salvo no banco.
        form.instance.usuario = self.request.user

        url = super().form_valid(form)

        #Depois do super o objeto está criado.
        return url

########## UPDATES ########## 
class CategoriaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
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

class FuncionarioUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
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
class CategoriaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
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

class FuncionarioDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
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

    def get_queryset(self):
        self.object_list = Produto.objects.filter(usuario=self.request.user)
        return self.object_list

class FuncionarioList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Funcionario
    template_name = 'cadastros/listas/funcionario.html'

class FornecedorList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Fornecedor
    template_name = 'cadastros/listas/fornecedor.html'

    def get_queryset(self):
        self.object_list = Fornecedor.objects.filter(usuario=self.request.user)
        return self.object_list