def produto_simples(a, b):
    produto = a * b
    return produto


# entrada de dados
a = int(input('Digite um número: '))
b = int(input('Digite um número: '))
resultado = produto_simples(a, b)
# saida de dados
print('A multiplicação entre os números {} e {} resulta no produto de {}.'.format(a, b, resultado))
