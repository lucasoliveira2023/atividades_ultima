# Generated by Django 4.2.4 on 2023-10-04 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('preferencia_evento', models.CharField(choices=[('todos', 'Todos'), ('musicas', 'Evento Musicas'), ('esportivos', 'Eventos Esportivos'), ('educativos', 'Eventos Educativos')], default='todos', max_length=10, verbose_name='Preferencia de Evento')),
                ('observacoes', models.TextField(blank=True, verbose_name='Observação')),
                ('enviado_em', models.DateTimeField(auto_now_add=True, verbose_name='Enviado em')),
                ('modificado_em', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
            ],
        ),
    ]
