def test_calculo_simples():
    assert calculo_simples(numero_pecas1=1,
                          valor_unitario_peca1=5.30,
                          numero_pecas2=2,
                          valor_unitario_peca2=5.10) == 15.50


def calculo_simples(numero_pecas1, valor_unitario_peca1, numero_pecas2, valor_unitario_peca2):
    valor_total = (
        numero_pecas1 * valor_unitario_peca1 + numero_pecas2 * valor_unitario_peca2
    )
    return round(valor_total, 2)