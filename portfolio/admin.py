from django.contrib import admin
from .models import (
    Licenciatura, UnidadeCurricular, Docente, 
    Projeto, Tecnologia, TFC, Competencia, 
    Formacao, MakingOf, TipoTecnologia
)

admin.site.register(TipoTecnologia)
admin.site.register(Licenciatura)
admin.site.register(Docente)
admin.site.register(Competencia)
admin.site.register(Formacao)

@admin.register(UnidadeCurricular)
class UnidadeCurricularAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ano', 'semestre', 'ects')
    list_filter = ('ano', 'semestre')
    search_fields = ('nome',)

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'unidade_curricular')
    list_filter = ('unidade_curricular', 'tecnologias')
    search_fields = ('nome', 'descricao')

@admin.register(TFC)
class TFCAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autores', 'ano', 'destaque')
    list_filter = ('ano', 'destaque')
    search_fields = ('titulo', 'resumo', 'autores')

@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'nivel_interesse')
    list_filter = ('tipo', 'nivel_interesse')
    search_fields = ('nome',)

@admin.register(MakingOf)
class MakingOfAdmin(admin.ModelAdmin):
    list_display = ('etapa', 'data')
    search_fields = ('etapa', 'descricao')