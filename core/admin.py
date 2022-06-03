from re import S
from django.contrib import admin
from .models import Aluno, Turma

# Register your models here.
@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_filter = ('turma',)
    search_fields = ('nome',)
    list_display = ('nome', 'email', 'telefone','turma',)
    list_display_links = ('nome', 'email', 'telefone','turma',)

admin.site.register(Turma)



