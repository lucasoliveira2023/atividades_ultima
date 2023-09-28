from requests_html import HTMLSession

sessao = HTMLSession()


url = "https://www.olx.com.br/eletronicos-e-celulares/estado-sp?q=iphone"


response = sessao.get(url)


anuncios = []


links = response.html.find('#ad-list li a')


for link in links:
    
    url_iphone = link.attrs['href']
    
    response_iphone = sessao.get(url_iphone)
    
    titulo = response_iphone.html.find('h1', first =True).text 
    preco = response_iphone.html.find('h2', first =True).text 
    
    
    anuncios.append({
        'url': url_iphone,
        'titulo': titulo,
        'preco': preco,        
    })
    
print(anuncios)
    