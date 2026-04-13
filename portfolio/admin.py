from django.contrib import admin
from .models import (
    Licenciatura, UnidadeCurricular, Docente, 
    Projeto, Tecnologia, TFC, Competencia, 
    Formacao, MakingOf
)

# Configuração para Unidades Curriculares
@admin.register(UnidadeCurricular)
class UnidadeCurricularAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ano', 'semestre', 'ects') # Colunas visíveis na tabela
    list_filter = ('ano', 'semestre')                  # Filtros na barra lateral direita
    search_fields = ('nome',)                         # Barra de pesquisa por nome

# Configuração para Projetos
@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'unidade_curricular')
    list_filter = ('unidade_curricular', 'tecnologias')
    search_fields = ('nome', 'descricao', 'conceitos_aplicados')

# Configuração para TFC (Crucial para validar a importação do JSON)
@admin.register(TFC)
class TFCAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autores', 'ano', 'destaque')
    list_filter = ('ano', 'destaque')
    search_fields = ('titulo', 'resumo', 'autores')

# Configuração para Tecnologias
@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nivel_interesse')
    list_filter = ('nivel_interesse',)
    search_fields = ('nome', 'descricao')

# Configuração para o Making Of (Obrigatório e valorizado)
@admin.register(MakingOf)
class MakingOfAdmin(admin.ModelAdmin):
    list_display = ('etapa', 'data')
    list_filter = ('data',)
    search_fields = ('etapa', 'descricao', 'erros_encontrados')

# Registos simples para as restantes entidades
admin.site.register(Licenciatura)
admin.site.register(Docente)
admin.site.register(Competencia)
admin.site.register(Formacao)