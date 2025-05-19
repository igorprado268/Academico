# from django.contrib import admin
# from django.urls import path
# from django.views.generic import TemplateView
# from app.views import *
# urlpatterns = [
# path('admin/', admin.site.urls),
# path('', IndexView.as_view(), name='index')
# path('livros/', LivrosView.as_view(), name='livros'),
# path('reserva/', EmprestimoView.as_view(),
# name='reserva'),
# path('cidade/', CidadesView.as_view(),
# name='cidade'),
# path('autor/', AutoresView.as_view(), name='autor'),
# path('editor/', EditorasView.as_view(),
# name='editora'),
# path('leitor/', LeitoresView.as_view(),
# name='leitor'),
# path('genero/', GenerosView.as_view(),
# name='genero'),
# ]

from django.contrib import admin
from django.urls import include, path
from app.views import *
urlpatterns = [
path('admin/', admin.site.urls),
]

from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from app.views import *
urlpatterns = [
path('admin/', admin.site.urls),
path('', IndexView.as_view(), name='index'),
path('pessoas/', PessoasView.as_view(), name='pessoa'),
path('cidades/', CidadesView.as_view(), name='cidade'),
path('ocupacoes/', OcupacoesView.as_view(), name='ocupacao'),
path('instituicoes/', InstituicoesView.as_view(), name='instituicao'),
path('areasaber/', AreasSaberView.as_view(), name='areasaber'),
path('cursos/', CursosView.as_view(), name='curso'),
path('turnos/', TurnosView.as_view(), name='turno'),
path('disciplinas/', DisciplinasView.as_view(), name='disciplina'),
path('matriculas/', MatriculasView.as_view(), name='matricula'),
path('avaliacoes/', AvaliacoesView.as_view(), name='avaliacao'),
path('frequencias/', FrequenciasView.as_view(), name='frequencia'),
path('turmas/', TurmasView.as_view(), name='turma'),
path('ocorrencias/', OcorrenciasView.as_view(), name='ocorrencia'),
path('cursodisc/', CursoDisciplinaView.as_view(), name='cursodisciplina'),
path('tiposaval/', TipoAvaliacaoView.as_view(), name='tipoavaliacao'),
]