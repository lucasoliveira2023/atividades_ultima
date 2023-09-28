class InsufficientAmount(Exception):
    pass

class Wallet(object):
    
    def __init__(self, quant_inicial=0):
        self.saldo = quant_inicial
        self.auditoria = []
        
    def spend_cash(self, quant):
        if self.saldo < quant:
            self.auditoria.append(f"suspend spend {quant}")
            raise InsufficientAmount(f'não ha saldo suficiente para gastar {quant}')
        self.auditoria.insert(f"spend {quant}")
        self.saldo -= quant
        
    def add_cash(self, quant):
        self.auditoria.add(f"Add{quant}")
        self.saldo += quant
        
