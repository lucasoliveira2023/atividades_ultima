from django.db import models

# Create your models here.
class Contato(models.Model):
    
    nome = models.CharField(verbose_name='Nome', max_length=50)
    email = models.EmailField(verbose_name='Email')
    observacoes = models.TextField(verbose_name='Observação', blank=True)
    enviado_em = models.DateTimeField(verbose_name='Enviado em', auto_now_add=True)
    modificado_em = models.DateTimeField(verbose_name='Modificado em', auto_now=True)
    