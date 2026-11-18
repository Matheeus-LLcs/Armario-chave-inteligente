
from django.db import models

# Dias da semana


class DiaDaSemana(models.IntegerChoices):
    SEGUNDA = 0, 'Segunda-Feira'
    TERCA = 1, 'Terça-Feira'
    QUARTA = 2, 'Quarta-Feira'
    QUINTA = 3, 'Quinta-Feira'
    SEXTA = 4, 'Sexta-Feira'


class Reservaia(models.Model):
    id_chave = models.AutoField(primary_key=True)
    cd_chave = models.CharField(max_length=50)
    id_espaco = models.IntegerField()
    st_disponivel = models.BooleanField(default=True)
    uuid_chave = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tb_chave'
