from django.shortcuts import render

from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.views import View
from django.contrib import messages
class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
    def post(self, request):
           pass

class CidadesView(View):
    def get(self, request, *args, **kwargs):
        cidades = Cidade.objects.all()
        return render(request, 'cidades.html', {'cidades': cidades})

class PessoasView(View):
    def get(self, request, *args, **kwargs):
        pessoas = Pessoa.objects.all()
        return render(request, 'pessoas.html', {'pessoas': pessoas})

class OcupacoesView(View):
    def get(self, request, *args, **kwargs):
        ocupacoes = Ocupacao.objects.all()
        return render(request, 'ocupacoes.html', {'ocupacoes': ocupacoes})

class InstituicoesView(View):
    def get(self, request, *args, **kwargs):
        instituicoes = Instituicao.objects.all()
        return render(request, 'instituicoes.html', {'instituicoes': instituicoes})

class AreasSaberView(View):
    def get(self, request, *args, **kwargs):
        areas = AreaSaber.objects.all()
        return render(request, 'areasaber.html', {'areas': areas})

class CursosView(View):
    def get(self, request, *args, **kwargs):
        cursos = Curso.objects.all()
        return render(request, 'cursos.html', {'cursos': cursos})

class TurnosView(View):
    def get(self, request, *args, **kwargs):
        turnos = Turno.objects.all()
        return render(request, 'turnos.html', {'turnos': turnos})

class DisciplinasView(View):
    def get(self, request, *args, **kwargs):
        disciplinas = Disciplina.objects.all()
        return render(request, 'disciplinas.html', {'disciplinas': disciplinas})

class MatriculasView(View):
    def get(self, request, *args, **kwargs):
        matriculas = Matricula.objects.all()
        return render(request, 'matriculas.html', {'matriculas': matriculas})

class AvaliacoesView(View):
    def get(self, request, *args, **kwargs):
        avaliacoes = Avaliacao.objects.all()
        return render(request, 'avaliacoes.html', {'avaliacoes': avaliacoes})

class FrequenciasView(View):
    def get(self, request, *args, **kwargs):
        frequencias = Frequencia.objects.all()
        return render(request, 'frequencias.html', {'frequencias': frequencias})

class TurmasView(View):
    def get(self, request, *args, **kwargs):
        turmas = Turma.objects.all()
        return render(request, 'turmas.html', {'turmas': turmas})

class OcorrenciasView(View):
    def get(self, request, *args, **kwargs):
        ocorrencias = Ocorrencia.objects.all()
        return render(request, 'ocorrencias.html', {'ocorrencias': ocorrencias})

class CursoDisciplinaView(View):
    def get(self, request, *args, **kwargs):
        relacoes = CursoDisciplina.objects.all()
        return render(request, 'cursodisc.html', {'relacoes': relacoes})

class TipoAvaliacaoView(View):
    def get(self, request, *args, **kwargs):
        tipos = TipoAvaliacao.objects.all()
        return render(request, 'tiposaval.html', {'tipos': tipos})