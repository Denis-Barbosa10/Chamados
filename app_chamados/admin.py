from django.contrib import admin

# Register your models here.
from .models import *


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Pendencia)
class PendenciaAdmin(admin.ModelAdmin):
    pass



@admin.register(Chamado)
class ChamadoAdmin(admin.ModelAdmin):
    pass


@admin.register(Atendimento)
class AtendimentoAdmin(admin.ModelAdmin):
	pass


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
	pass