import time
from datetime import datetime

def time_exec(func):
    def interno(*args, **kwargs):
        inicio = time.time()
        
        fim = time.time()
        print(func.__name__+ 'executado em' + str((fim-inicio)*1000) + 'milisegundos')
    return interno

@time_exec
def calc_quad(numbers):
    result = []
    for number in numbers:
        result.append(number*number)
    return result

@time_exec
def calc_cubo(numbers):
    result = []
    for number in numbers:
        result.append(number*number*number)
    return result

if __name__ == '__main__':
    list_number = range(1,100000)
    print(datetime.now())
    calc_quad(list_number)
    calc_cubo(list_number)
    print(datetime.now())