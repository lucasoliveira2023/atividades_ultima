import pytest

def calc_valor_total(valor_unitario, quantidade):
    desconto = 1
    
    if quantidade >= 10 and quantidade <= 99:
        desconto = 0.95
    elif quantidade >= 100 and quantidade <= 999:
        desconto = 0.90
    elif quantidade >= 1000:
        desconto = 0.85
        
        
    valor_com_desconto = valor_unitario * desconto * quantidade
    valor_sem_desconto = valor_unitario * quantidade
    
    return valor_sem_desconto, valor_com_desconto


def test_desconto_10_a_99():
    valor_sem_desconto, valor_com_desconto = calc_valor_total(10.0, 50)
    assert valor_sem_desconto == 500.0
    assert valor_com_desconto == 475.0
    
def test_desconto_100_a_999():
    valor_sem_desconto, valor_com_desconto = calc_valor_total(100.0, 500)
    assert valor_sem_desconto == 50000.0
    assert valor_com_desconto == 45000.0
    
def test_desconto_mais_1000():
    valor_sem_desconto, valor_com_desconto = calc_valor_total(100.0, 500)
    assert valor_sem_desconto == 1000000.0
    assert valor_com_desconto == 850000.0
    
if __name__ == '__main__':
    pytest.main()