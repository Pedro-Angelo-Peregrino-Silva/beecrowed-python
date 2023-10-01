from math import sqrt
# entrada de dados

a, b, c = map(int, input().split())

maior_a_b = (a + b + abs(a - b)) / 2

eh_maior = (maior_a_b + c + abs(maior_a_b - c)) / 2

print(f'{eh_maior} eh o maior')
