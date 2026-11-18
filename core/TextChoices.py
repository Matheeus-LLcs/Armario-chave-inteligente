class ReservaPontual(models.Model):
    id_reserva_pontual = models.AutoField(primary_key=True)
    espaço = models.ForeignKey(Espaco, on_delete=models.CASCADE)
    usuário = models.ForeignKey(User, on_delete=models.CASCADE)
    dt_reserva = models.DateField()
    hr_inicio = models.TimeField()
    hr_fim = models.TimeField()
    tp_reserva = models.CharField(max_length=50)
    ds_motivo = models.TextField()
    st_aprovado = models.BooleanField(default=False)

class Remanejamento(models.Model):
    id_remanejamento = models.AutoField(primary_key=True)
    espaço = models.ForeignKey(Espaco, on_delete=models.CASCADE)
    usuario_substituto = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    dt_remanejamento = models.DateField(
        verbose_name="Data Específica da Alteração"
    )
    hr_inicio = models.TimeField()
    hr_fim = models.TimeField()
    tp_reserva = models.CharField(max_length=50)
    ds_motivo = models.TextField()
    dh_registro = models.DateTimeField(auto_now_add=True)