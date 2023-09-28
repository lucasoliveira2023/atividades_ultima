valor_string = 'UltimaSchool'
objet_iter = iter(valor_string)

for item in objet_iter:
    print(item)
    
while True:
    try:
        item = next(objet_iter)
        print(item)
    except StopIteration:
        break