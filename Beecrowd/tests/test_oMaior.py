def test_maior():
    assert maior(a=-7, b=-14, c=-106) == -7


def maior(a, b, c):
    maior_a_b = (a + b + abs(a - b)) / 2
    maior_a_c = (a + c + abs(a - c)) / 2
    maior_b_c = (b + c + abs(b - c)) / 2
    if maior_a_b > maior_a_c > maior_b_c:
        return maior_a_b
    if maior_b_c > maior_a_c > maior_a_b:
        return maior_b_c
    else:
        return maior_a_c
