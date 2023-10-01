def test_calculo_salario():
    assert calculo_salario(25, 100, 5.50) == (25, 550.00)


def calculo_salario(number, qnt_horas_trabalhadas, valor_hora_trabalhada):
    numero = number
    salario = qnt_horas_trabalhadas * valor_hora_trabalhada
    return numero, salario