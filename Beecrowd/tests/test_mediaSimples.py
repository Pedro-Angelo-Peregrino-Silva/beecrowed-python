import pytest


def test_media_simples():
    assert media_simples(5.0, 7.1) == 6.43182


def media_simples(a, b):
    media = (a * 3.5 + b * 7.5) / (3.5 + 7.5)
    resultado = float('{:.5f}'.format(media))
    return resultado