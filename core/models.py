import email
from django.db import models

class Turma(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Aluno (models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    telefone = models.CharField(max_length=100)
    turma = models.ForeignKey(Turma, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome
