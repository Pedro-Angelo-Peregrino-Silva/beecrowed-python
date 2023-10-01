def test_area():
    assert area(a=3.0, b=4.0, c=5.2) == (7.800, 84.949, 18.200, 16.000, 12.000)
    pass


def area(a, b, c):
    triangulo = (a * c) / 2
    circulo = 3.14159 * c ** 2
    trapezio = (a + b) * c / 2
    quadrado = b ** 2
    retangulo = a * b

    return round(triangulo, 3), round(circulo, 3), round(trapezio, 3), round(quadrado, 3), round(retangulo, 3)

