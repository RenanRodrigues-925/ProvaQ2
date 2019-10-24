from django.contrib import admin
from .models import *

class TurmaInline(admin.TabularInline):
    model = Turma

admin.site.register(Turma)


class ProfessorInline(admin.TabularInline):
    model = Professor
admin.site.register(Professor)

class CursoAdmin(admin.TabularInline):
    inlines = [
            TurmaInline,ProfessorInline
        ]
admin.site.register(Curso)

admin.site.site_header = 'Painel de Cursos'
admin.site.index_title = 'Cursos'
admin.site.site_title = 'Cadastro de Cursos'

