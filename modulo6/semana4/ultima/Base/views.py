from django.shortcuts import render
# Create your views here.
from Base.forms import InscreverForm

from eventos.models import Evento

def inicio(request):
    dados = []
    contexto = {
        'eventos': Evento.objects.filter(publicado=True)[:2],
    }
       
    resposta = render(request, 'inicio.html', contexto)
    return resposta



def inscrever(request):
    contexto = {'sucesso': False}
    form = InscreverForm(request.POST or None)
    if form.is_valid():
        form.save()
        contexto['sucesso'] = True
    contexto['form'] = form
    return render(request, 'inscrever.html', contexto)