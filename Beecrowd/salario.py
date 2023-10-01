def calculo_salario(number, qnt_horas_trabalhadas, valor_hora_trabalhada):
    numero = number
    salario = qnt_horas_trabalhadas * valor_hora_trabalhada
    return numero, salario


# entrada de dados
number = int(input('Digite o número de identificação do funcionário: '))
qnt_horas_trabalhadas = int(input('Digite a quantidade de horas trabalhadas: '))
valor_hora_trabalhada = float(input('Digite o valor por hora trabalhada: '))
Salario = calculo_salario(number, qnt_horas_trabalhadas, valor_hora_trabalhada)

# saida de dados
print(f'NUMBER = {Salario[0]}\nSALARY = U$ {Salario[1]:.2f}')
