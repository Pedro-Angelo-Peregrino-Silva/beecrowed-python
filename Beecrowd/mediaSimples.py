def media_simples(a, b):
    media = (a * 3.5 + b * 7.5) / (3.5 + 7.5)
    resultado = float('{:.5f}'.format(media))
    return resultado

# entrada de dados
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
resposta = media_simples(nota1, nota2)
# saida de dados
print('A primeira nota do aluno foi {}, segunda {}, sendo a média geral {}.'.format(nota1, nota2, resposta))


