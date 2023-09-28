from requests_html import HTMLSession

sessao = HTMLSession()
imoveis = []
url ='https://www.zapimoveis.com.br/venda/apartamentos/sp+sao-paulo/'
resposta = sessao.get(url)
links = resposta.html.find()
for link in links:
    #url_imovel = link.attrs[]
    resposta_imovel = sessao.get(url)
    titulo = resposta_imovel.html.find('h1', first=True).text 
    preco = resposta_imovel.html.find('h2')[2].text 
    imoveis.append({
        'url': url,
        'titulo': titulo,
        'preco': preco
    })
    
print(imoveis)