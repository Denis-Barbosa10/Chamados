from django.contrib.auth.models import User
from django.db import models

class Funcionario(models.Model):
    nome = models.CharField(max_length=150)
    matricula = models.CharField(max_length=10)



    def __str__(self):
        return self.nome




class Tag(models.Model):
    nome = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64)

    def __str__(self):
        return self.nome


class Pendencia(models.Model):
    nome = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64)

    def __str__(self):
        return self.nome



class Categoria(models.Model):
    nome = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64)

    def __str__(self):
        return self.nome

class Chamado(models.Model):
    class Meta:
        verbose_name = 'Chamado'
        verbose_name_plural = 'Chamados'

    servico = models.CharField('Ordem de Serviço', max_length=128, blank=True, null=True)
    titulo = models.CharField('Título', max_length=128)
    descricao = models.TextField('Conteúdo')
    data_de_publicacao = models.DateTimeField(
        'Data de publicação', blank=True, null=True)
    telefone_celular = models.CharField('Telefone celular', max_length=15,
                                        help_text='Número do telefone celular no formato (99) 99999-9999',
                                        null=True, blank=True,
                                        )
    tags = models.ManyToManyField(Tag)
    status = models.ForeignKey(Pendencia, on_delete=models.CASCADE, null=True, blank=True)
    categoria= models.ForeignKey(Categoria, on_delete=models.CASCADE,blank=True,null=True)






    def __str__(self):
        return self.servico


class Atendimento(models.Model):
    chamado= models.ForeignKey(Chamado, on_delete=models.CASCADE,blank=True,null=True)
    funcionario=models.ForeignKey(Funcionario, on_delete=models.CASCADE,blank=True,null=True)
    descricao = models.TextField('Conteúdo')
    