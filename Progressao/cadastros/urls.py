from django.urls import path

# Importa as views que a gente criou 
from .views import CategoriaCreate, FornecedorCreate, FuncionarioCreate, ProdutoCreate, UnidadeMedidaCreate
from .views import CategoriaUpdate, FornecedorUpdate, FuncionarioUpdate, ProdutoUpdate, UnidadeMedidaUpdate
from .views import CategoriaDelete, FornecedorDelete, FuncionarioDelete, ProdutoDelete, UnidadeMedidaDelete
from .views import CategoriaList, FornecedorList, FuncionarioList, ProdutoList, UnidadeMedidaList

# Tem que ser urlpatterns porque é padrão do Django
urlpatterns = [
    # Todo path tem endereço, sua_view.as_view() e nome
    path('cadastrar/categoria/', CategoriaCreate.as_view(), name='cadastrar-categoria'),
    path('cadastrar/fornecedor/', FornecedorCreate.as_view(), name='cadastrar-fornecedor'),
    path('cadastrar/funcionario/', FuncionarioCreate.as_view(), name='cadastrar-funcionario'),
    path('cadastrar/produto/', ProdutoCreate.as_view(), name='cadastrar-produto'),
    path('cadastrar/unidademedida/', UnidadeMedidaCreate.as_view(), name='cadastrar-unidademedida'), 

    path('editar/categoria/<int:pk>/', CategoriaUpdate.as_view(), name='editar-categoria'),
    path('editar/fornecedor/<int:pk>/', FornecedorUpdate.as_view(), name='editar-fornecedor'),
    path('editar/funcionario/<int:pk>/', FuncionarioUpdate.as_view(), name='editar-funcionario'),
    path('editar/produto/<int:pk>/', ProdutoUpdate.as_view(), name='editar-produto'),
    path('editar/unidademedida/<int:pk>/', UnidadeMedidaUpdate.as_view(), name='editar-unidademedida'),

    path('excluir/categoria/<int:pk>/', CategoriaDelete.as_view(), name='excluir-categoria'),
    path('excluir/fornecedor/<int:pk>/', FornecedorDelete.as_view(), name='excluir-fornecedor'),
    path('excluir/funcionario/<int:pk>/', FuncionarioDelete.as_view(), name='excluir-funcionario'),
    path('excluir/produto/<int:pk>/', ProdutoDelete.as_view(), name='excluir-produto'),
    path('excluir/unidademedida/<int:pk>/', UnidadeMedidaDelete.as_view(), name='excluir-unidademedida'),

    path('listar/categoria/', CategoriaList.as_view(), name='listar-categoria'),
    path('listar/fornecedor/', FornecedorList.as_view(), name='listar-fornecedor'),
    path('listar/funcionario/', FuncionarioList.as_view(), name='listar-funcionario'),
    path('listar/produto/', ProdutoList.as_view(), name='listar-produto'),
    path('listar/unidademedida/', UnidadeMedidaList.as_view(), name='listar-unidademedida'),
]
