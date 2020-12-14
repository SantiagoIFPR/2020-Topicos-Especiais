from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.views.generic.list import ListView

from .models import Categoria, Fornecedor, Funcionario, Produto, UnidadeMedida

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from braces.views import GroupRequiredMixin

from django.shortcuts import get_object_or_404

# Create your views here.
class CategoriaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Categoria
    fields = ['nome','descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-categoria')

    def get_context_data(self, *args, **kwargs):
        context= super().get_context_data(*args, **kwargs)
        
        context['titulo'] = "Cadastro de Categorias"
        context['botao'] = "Cadastrar"
        
        return context

class UnidadeMedidaCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = UnidadeMedida
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-unidademedida')

    def get_context_data(self, *args, **kwargs):
        context= super().get_context_data(*args, **kwargs)
        
        context['titulo'] = "Cadastro de Unidade de Medida"
        context['botao'] = "Cadastrar"
        
        return context

class ProdutoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Produto
    fields = ['nome','descricao','estoque_max','estoque_min','codigo_barras','unidademedida','categoria']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-produto')

    def get_context_data(self, *args, **kwargs):
        context= super().get_context_data(*args, **kwargs)
        
        context['titulo'] = "Cadastro de Produtos"
        context['botao'] = "Cadastrar"
        
        return context

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

    def get_context_data(self, *args, **kwargs):
        context= super().get_context_data(*args, **kwargs)
        
        context['titulo'] = "Cadastro de Funcionários"
        context['botao'] = "Cadastrar"
        
        return context

class FornecedorCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Fornecedor
    fields = ['nome','documento','cep','endereco','numero','bairro','cidade','estado','telefone','email']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-fornecedor')  

    def get_context_data(self, *args, **kwargs):
        context= super().get_context_data(*args, **kwargs)
        
        context['titulo'] = "Cadastro de Fornecedor"
        context['botao'] = "Cadastrar"
        
        return context

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

    def get_context_data(self, *args, **kwargs):
        context= super().get_context_data(*args, **kwargs)
        
        context['titulo'] = "Edição de Categoria"
        context['botao'] = "Salvar"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'
        
        return context

class UnidadeMedidaUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = UnidadeMedida
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-unidademedida')

    def get_context_data(self, *args, **kwargs):
        context= super().get_context_data(*args, **kwargs)
        
        context['titulo'] = "Edição de Unidade de Medida"
        context['botao'] = "Salvar"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'
        
        return context

class ProdutoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Produto
    fields = ['nome','descricao','estoque_max','estoque_min','codigo_barras','unidademedida','categoria']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-produto')

    def get_context_data(self, *args, **kwargs):
        context= super().get_context_data(*args, **kwargs)
        
        context['titulo'] = "Edição de Produto"
        context['botao'] = "Salvar"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'
        
        return context

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Produto, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

class FuncionarioUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Funcionario
    fields = ['nome_funcionario','setor_funcionario']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-funcionario')

    def get_context_data(self, *args, **kwargs):
        context= super().get_context_data(*args, **kwargs)
        
        context['titulo'] = "Edição de Funcionário"
        context['botao'] = "Salvar"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'
        
        return context

class FornecedorUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Fornecedor
    fields = ['nome','documento','cep','endereco','numero','bairro','cidade','estado','telefone','email']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-fornecedor')  

    def get_context_data(self, *args, **kwargs):
        context= super().get_context_data(*args, **kwargs)
        
        context['titulo'] = "Edição de Fornecedor"
        context['botao'] = "Salvar"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'
        
        return context

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Fornecedor, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

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

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Produto, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

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

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Fornecedor, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

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