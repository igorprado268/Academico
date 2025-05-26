# from django.contrib import admin

# # Register your models here.

# from .models import*
# from django.contrib import admin

# admin.site.register(Cidade)
# admin.site.register(Ocupacao)
# admin.site.register(Pessoa)
# admin.site.register(Instituicao)
# admin.site.register(AreaSaber)
# admin.site.register(Curso)
# admin.site.register(Turno)
# admin.site.register(Disciplina)
# admin.site.register(Matricula)
# admin.site.register(TipoAvaliacao)
# admin.site.register(Avaliacao)
# admin.site.register(Frequencia)
# admin.site.register(Turma)
# admin.site.register(Ocorrencia)

from django.contrib import admin
from .models import (
    Cidade, Ocupacao, Pessoa, Instituicao, AreaSaber, Curso,
    Turno, Disciplina, Matricula, TipoAvaliacao, Avaliacao,
    Frequencia, Turma, Ocorrencia, CursoDisciplina
)

# *************inlines *********************

class PessoaInline(admin.TabularInline):
    model = Pessoa
    extra = 1

class InstituicaoInline(admin.TabularInline):
    model = Instituicao
    extra = 1

class CursoInline(admin.TabularInline):
    model = Curso
    extra = 1

class MatriculaInline(admin.TabularInline):
    model = Matricula
    extra = 1

class AvaliacaoInline(admin.TabularInline):
    model = Avaliacao
    extra = 1

class FrequenciaInline(admin.TabularInline):
    model = Frequencia
    extra = 1

class OcorrenciaInline(admin.TabularInline):
    model = Ocorrencia
    extra = 1

class CursoDisciplinaInline(admin.TabularInline):
    model = CursoDisciplina
    extra = 1
class DisciplinaInline(admin.TabularInline):
    model = Disciplina
    extra = 1

# **********************************

class OcupacaoAdmin(admin.ModelAdmin):
    inlines = [PessoaInline]

class InstituicaoAdmin(admin.ModelAdmin):
    inlines = [CursoInline]

class AreaSaberAdmin(admin.ModelAdmin):
    inlines = [CursoInline]

class CursoAdmin(admin.ModelAdmin):
    inlines = [DisciplinaInline]

class DisciplinaAdmin(admin.ModelAdmin):
    inlines = [AvaliacaoInline]

class TurmaAdmin(admin.ModelAdmin):
    inlines = [MatriculaInline]

class CidadeAdmin(admin.ModelAdmin):
    inlines = [InstituicaoInline]

# *************registro dos modelos********************

admin.site.register(Ocupacao, OcupacaoAdmin)
admin.site.register(Instituicao, InstituicaoAdmin)
admin.site.register(AreaSaber, AreaSaberAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Disciplina, DisciplinaAdmin)
admin.site.register(Turma, TurmaAdmin)
admin.site.register(Cidade, CidadeAdmin)

# modelos sem inlines
admin.site.register(Pessoa)
admin.site.register(Turno)
admin.site.register(TipoAvaliacao)
admin.site.register(CursoDisciplina)

