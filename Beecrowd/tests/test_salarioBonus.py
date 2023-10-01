def test_salario_bonus():
    assert calculo_salario_bonus(salario_fixo=500.00, valor_vendas=1230.30) == 684.54


def calculo_salario_bonus(salario_fixo, valor_vendas):
    bonus = valor_vendas * 15 / 100
    salario = salario_fixo + bonus
    return round(salario, 2)
