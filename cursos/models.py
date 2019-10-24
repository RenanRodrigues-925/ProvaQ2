from django.db import models
from django.conf import settings

class Curso(models.Model):
    nome = models.CharField('Nome',max_length=70)
    carga_horaria = models.CharField('Carga Horária',max_length=10)
    ementa = models.CharField('Ementa', max_length=100)
    valor = models.CharField('Valor', max_length=10)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'


class Turma(models.Model):
        Curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
        data_inicio = models.DateField('Data de Incio',)
        data_termino = models.DateField('Data do Termino',)
        hora_inicio = models.TimeField('Hora de Inicio',)
        hora_termino = models.TimeField('Hora do Termino',)

        def __str__(self):
            return self.Curso

        class Meta:
            verbose_name_plural = 'Turmas'
            indexes = [
                models.Index(fields=['data_inicio','data_termino','hora_inicio','hora_termino']),
            ]

class Professor(models.Model):
        Turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
        nome = models.CharField('Nome',max_length=100)
        telefone = models.CharField('Telefone', max_length=13)
        valor_hora_aula = models.CharField('Valor da Hora Aula',max_length=10)

        def __str__(self):
            return self.Turma

        class Meta:
            verbose_name_plural = 'Professores'
            indexes = [
                models.Index(fields=['nome','telefone','valor_hora_aula']),
            ]