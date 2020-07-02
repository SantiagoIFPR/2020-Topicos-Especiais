from django.urls import path

# Importa as views que a gente criou 
from .views import PaginaInicial, PaginaSobre, PaginaDiagrama

# Tem que ser urlpatterns porque é padrão do Django
urlpatterns = [
    # Todo path tem endereço, sua_view.as_view() e nome
    path('', PaginaInicial.as_view(), name='index'),
    path('sobre/', PaginaSobre.as_view(), name='sobre'),
    path('diagramas/', PaginaDiagrama.as_view(), name='diagramas')
]
