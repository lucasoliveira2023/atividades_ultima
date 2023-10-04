from django.db import models

# Create your models here.
class ReservaBanho(models.Model):
    nome_pet = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    dia_reserva = models.DateField()
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome_pet



