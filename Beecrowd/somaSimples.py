def soma_simples(a, b):
    soma = a + b
    return soma


a = int(input('Digite um número: '))
b = int(input('Digite um número: '))

resposta = soma_simples(a, b)

print('Soma = {}'.format(resposta))
