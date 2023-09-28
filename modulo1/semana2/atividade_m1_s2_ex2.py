horas_estimadas = 80
valor_inicial = 1000.00
valor_hora = 20.45
taxa = 0.15

valor_total = valor_inicial + horas_estimadas * valor_hora + taxa * (valor_inicial + horas_estimadas * valor_hora)

print(f'{valor_total:.2f}')