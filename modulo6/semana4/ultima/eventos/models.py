from django.db import models

# Create your models here.
class Categoria(models.Model):
    
    nome = models.CharField('Nome', max_length=50)
    descricao = models.TextField('Descrição', blank=True)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nome']
        
        
class Evento(models.Model):
    
    nome = models.CharField('Nome', max_length=50)
    categoria = models.ForeignKey(Categoria, models.SET_NULL, null=True, blank=True)
    descricao = models.TextField('Descrição', blank=True)
    data = models.DateField('Data do Evento', null= True, blank=True)
    publicado = models.BooleanField('Publicado', default=False)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'