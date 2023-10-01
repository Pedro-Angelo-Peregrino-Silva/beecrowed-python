def area_circulo(raio):
    calculo = 3.14159 * (raio ** 2)
    area = float('{:.4f}'.format(calculo))
    return area


# Entrada de dados
raio = float(input('Número: '))
resultado = (area_circulo(raio))
# saida de dados
print('A área do circulo com raio de {} é igual a {}.'.format(raio, resultado))
