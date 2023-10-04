from django.shortcuts import render
# Create your views here.
from Base.forms import InscreverForm

from Base.models import Contato

def inicio(request):
    dados = []
    dados.append(
        {
            'titulo': 'Titulo Legal 1',
            'categoria': 'Categoria 1',
            'data': '02/10/2023',
        }
    )
    dados.append(
        {
            'titulo': 'Titulo Legal 2',
            'categoria': 'Categoria 2',
            'data': '03/10/2023',
        }
    )
    contexto ={
        'dados': dados
    }
    resposta = render(request, 'inicio.html', contexto)
    return resposta



def inscrever(request):
    contexto = {'sucesso': False}
    form = InscreverForm(request.POST or None)
    if form.is_valid():
        contato = Contato()
        contato.nome = form.cleaned_data['nome']
        contato.email = form.cleaned_data['email']
        contato.observacoes = form.cleaned_data['observacao']
        contato.save()
        contexto['sucesso'] = True
    contexto['form'] = form
    return render(request, 'inscrever.html', contexto)