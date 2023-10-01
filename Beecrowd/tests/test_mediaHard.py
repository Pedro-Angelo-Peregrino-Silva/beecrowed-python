def test_media_hard():
    assert media_hard(5.0, 6.0, 7.0) == 6.3


def media_hard(a, b, c):
    media = (a * 2 + b * 3 + c * 5) / (2 + 3 + 5)
    resultado = float('{:.1f}'.format(media))
    return resultado
