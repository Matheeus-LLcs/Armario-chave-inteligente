from django.db import models

# Create your models here.


class Meta:
    managed = False
    db_table = 'tb_chave'

    class DiaDaSemana(models.IntegerChoices):
        SEGUNDA = 0, 'Segunda-Feira'
        TERCA = 1, 'Terça-Feria'
        QUARTA = 2, 'Quarta-Feira'
        QUINTA = 3, 'Quinta-Feira'
        SEXTA = 4, 'Sexta-Feira'

        class Reservaia(models.Model):
            nr_dia_semana = models.IntegerField(choices=DiaDaSemana)
            hr_inicio = models.TimeField()
            hr_fim = models.TimeField()
