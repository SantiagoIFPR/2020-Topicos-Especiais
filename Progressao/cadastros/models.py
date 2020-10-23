from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=80)
    descricao = models.CharField(max_length=100, verbose_name="Descrição")

    def __str__(self):
        return"{} ({})".format(self.nome, self.descricao)


class UnidadeMedida(models.Model):
    nome = models.CharField(max_length=100)
   
    def __str__(self):
        return"{}".format(self.nome)

class Produto(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Produto")
    descricao = models.CharField(max_length=120, verbose_name="Descrição")
    estoque_max = models.IntegerField(verbose_name="Estoque Máximo")
    estoque_min = models.IntegerField(verbose_name="Estoque Mínimo")
    codigo_barras = models.CharField(max_length=30, verbose_name="Código de Barras")
    unidademedida = models.ForeignKey(UnidadeMedida, on_delete=models.PROTECT)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    
    def __str__(self):
        return"{} ({})".format(self.nome, self.codigo_barras)

class Funcionario(models.Model):
    nome_funcionario = models.CharField(max_length=100, verbose_name="Nome Funcionário")
    setor_funcionario = models.CharField(max_length=40, verbose_name="Setor do Funcionário")

    def __str__(self):
        return"{}".format(self.nome_funcionario)

class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    documento = models.CharField(max_length=30, verbose_name="CPF ou CNPJ", unique=True)
    cep = models.CharField(max_length=20)
    endereco = models.CharField(max_length=120)
    numero = models.DecimalField(decimal_places=2, max_digits=4)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return"{} ({})".format(self.nome, self.documento)