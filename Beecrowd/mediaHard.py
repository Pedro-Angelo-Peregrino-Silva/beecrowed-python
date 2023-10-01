def media_hard(a, b, c):
    media = (a * 2 + b * 3 + c * 5) / (2+3+5)
    resultado = float('{:.1f}'.format(media))
    return resultado


# entrada de dados
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
resposta = media_hard(nota1, nota2, nota3)
# saida de dados
print('A primeira nota do aluno foi {}, segunda {} e terceira {} sendo a média geral {}.'.format(
    nota1, nota2, nota3, resposta))