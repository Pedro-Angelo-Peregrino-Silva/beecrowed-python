import pytest

def test_produto_simples():
    assert produto_simples(2, 5)


def produto_simples(a, b):
    produto = a * b
    return produto
