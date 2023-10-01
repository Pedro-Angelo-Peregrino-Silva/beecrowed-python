import pytest


def test_area_circulo():
    assert area_circulo(2.00) == 12.5664


def area_circulo(raio):
    calculo = 3.14159 * (raio ** 2)
    area = float('{:.4f}'.format(calculo))
    return area

