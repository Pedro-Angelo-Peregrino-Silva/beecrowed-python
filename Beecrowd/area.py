# entrada de dados
a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))

triangulo = (a * c) / 2
circulo = 3.14159 * c ** 2
trapezio = (a + b) * c / 2
quadrado = b ** 2
retangulo = a * b

# saida de dados
print(f'TRIANGULO: {triangulo:.3f}\n'
      f'CIRCULO: {circulo:.3f}\n'
      f'TRAPEZIO: {trapezio:.3f}\n'
      f'QUADRADO: {quadrado:.3f}\n'
      f'RETANGULO: {retangulo:.3f}')
