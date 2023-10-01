import pytest


def test_soma_simples():
    assert soma_simples(2, 2) == 4


def soma_simples(a, b):
    soma = a + b
    return soma
