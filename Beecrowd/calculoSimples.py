def calculo_simples(numero_pecas1, valor_unitario_peca1, numero_pecas2, valor_unitario_peca2):
    valor_total = (
        numero_pecas1 * valor_unitario_peca1 + numero_pecas2 * valor_unitario_peca2
    )
    return round(valor_total, 2)


# entrada de dados
cod_peca1 = int(input('Código peça 01: '))
qnt_peca1 = int(input('Quantas peças foram compradas? '))
valor_peca1 = float(input('Qual o valor unitário da peça? '))

cod_peca2 = int(input('Código peça 02: '))
qnt_peca2 = int(input('Quantas peças foram compradas? '))
valor_peca2 = float(input('Qual o valor unitário da peça? '))

valor_pagar = calculo_simples(qnt_peca1, valor_peca1, qnt_peca2, valor_peca2)

# saida de dados
print(f'VALOR A PAGAR: R$ {valor_pagar:.2f}')
