def diferenca_simples(a, b, c, d):
    diferenca = (a * b - c * d)
    return diferenca


# entrada de dados
a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C: '))
d = int(input('Digite o valor de D: '))
Diferenca = diferenca_simples(a, b, c, d)
# saida de dados
print(f'A diferença do produto de ({a} x {b} - {c} x {d}) é igual a {Diferenca}.')