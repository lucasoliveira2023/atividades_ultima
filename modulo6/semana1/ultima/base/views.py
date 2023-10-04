from django.shortcuts import render
# Create your views here.
def inicio(request):
    dados = []
    dados.append(
        {
            'titulo':'Titulo legal 1',
            'categoria':'Categoria 1',
            'Data':'02/10/2023'
        },
    )
    dados.append(
        {
            'titulo':'Titulo legal 2',
            'categoria':'Categoria 2',
            'Data':'01/10/2023'
        }
    )
    contexto = {
        'dados': dados
    }
    resposta = render(request, 'inicio.html', contexto)
    return resposta