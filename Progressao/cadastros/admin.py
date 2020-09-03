from django.contrib import admin

from .models import Categoria, UnidadeMedida, Produto, Funcionario, Fornecedor

# Register your models here.
admin.site.register(Categoria)
admin.site.register(UnidadeMedida)
admin.site.register(Produto)
admin.site.register(Funcionario)
admin.site.register(Fornecedor)