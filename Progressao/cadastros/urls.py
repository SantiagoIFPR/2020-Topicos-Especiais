from django.urls import path

# Importa as views que a gente criou 
from .views import CategoriaCreate, FornecedorCreate, FuncionarioCreate, ProdutoCreate, UnidadeMedidaCreate
from .views import CategoriaUpdate, FornecedorUpdate, FuncionarioUpdate, ProdutoUpdate, UnidadeMedidaUpdate

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
]
