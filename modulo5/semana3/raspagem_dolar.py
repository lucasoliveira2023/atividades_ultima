#import sqlite3
from requests_html import HTMLSession
session = HTMLSession()
campo = '#taxa-comercial'
url = 'https://www.melhorcambio.com/dolar-hoje'
response = session.get(url)
dolar = response.html.find(campo, first=True)
print(dolar)
print(dolar.attrs['value']) 

