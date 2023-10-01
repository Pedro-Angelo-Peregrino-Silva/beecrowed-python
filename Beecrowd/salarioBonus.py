def calculo_salario_bonus(salario_fixo, valor_vendas):
    bonus = valor_vendas * 15 / 100
    salario = salario_fixo + bonus
    return round(salario, 2)


# entrada de dados
nome_funcionario = str(input('Digite o nome do funcionário: '))
salario_fixo = float(input('Valor do salário fixo? '))
valor_vendas = float(input('Valor do montante de vendas: '))
Salario = calculo_salario_bonus(salario_fixo, valor_vendas)

# saida de dados
print(f'TOTAL = R$ {Salario:.2f}')
