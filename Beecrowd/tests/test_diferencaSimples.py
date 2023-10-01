def test_diferenca_simples():
    assert diferenca_simples(5, 6, 7, 8) == -26


def diferenca_simples(a, b, c, d):
    diferenca = (a * b - c * d)
    return diferenca