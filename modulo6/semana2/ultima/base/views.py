from django.shortcuts import render

from base.forms import InscreverForm

def inicio(request):
    dados = []
    dados.append(
        {
            'titulo': 'titulo legal 1',
            'categoria': 'categoria 1',
            'data': '02/10/2023'
        }
    )
    dados.append(
        {           
            'titulo': 'titulo legal 2',
            'categoria': 'categoria 2',
            'data': '02/10/2023'
        }       
    )
    contexto = {
        'dados': dados
    }
    resposta = render(request, 'inicio.html', contexto)
    return resposta


def inscrever(request):
    contexto = {'sucesso': False}
    form = InscreverForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data['nome'])
        print(form.cleaned_data['email'])
        print(form.cleaned_data['observaçao'])
        print(form.cleaned_data['data'])
        print(type(form.cleaned_data['data']))
        contexto['sucesso'] = True
    contexto['form'] = form
    return render(request, 'inscrever.html', contexto)
