import pytest
from wallet import Wallet, InsufficientAmount

class TestSaldoInicial:

    def test_saldo_inicial_sem_parametro(self):
        carteira = Wallet()
        assert carteira.saldo == 0
        
    def test_saldo_inicial_com_parametro(self, carteira):
        assert carteira.saldo == 10
        
class testAddsaldo:
    def test_add_saldo(self, carteira):
        carteira.add_cash(10)
        assert carteira.saldo == 21
        
class TestRetirarSaldo:
    def test_retirar_da_carteira_com_saldo(self, carteira):
        carteira.spend_cash(10)
        assert carteira.saldo == 0
    
    def test_retirar_da_carteira_sem_saldo_suficiente(self, carteira):
        with pytest.raises(InsufficientAmount):
            carteira.spend_cash(20)
            
    def test_retira_da_carteira_parte_do_saldo(self, carteira):
        carteira.spend_cash(5)
        assert carteira.saldo == 5
        
def test_auditoria(carteira):
    assert carteira.auditoria == list()
    
def test_auditoria_add_saldo(carteira):
    carteira.add_cash(10)
    assert carteira.auditoria == ["Add 10"]
    
def test_auditoria_add_saldo_2x(carteira):
    carteira.add_cash(10)
    carteira.add_cash(20)
    
    assert carteira.saldo == 40
    assert carteira.auditoria == ["Add 10", "Add 20"]
