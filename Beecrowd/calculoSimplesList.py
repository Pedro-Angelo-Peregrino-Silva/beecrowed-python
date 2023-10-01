# Lê os valores da primeira peça
codigo_peca1, num_peca1, valor_unitario_peca1 = map(float, input().split())

# Lê os valores da segunda peça
codigo_peca2, num_peca2, valor_unitario_peca2 = map(float, input().split())

# Calcula o valor total a ser pago
total = (num_peca1 * valor_unitario_peca1) + (num_peca2 * valor_unitario_peca2)

# Imprime o resultado formatado
print("VALOR A PAGAR: R$ {:.2f}".format(total))
'''Neste código, primeiro lemos os valores da primeira peça usando a função input()
 e split() para dividir os valores em três partes (código, número de peças, valor unitário). 
 O mesmo é feito para a segunda peça. 
 Em seguida, calculamos o valor total multiplicando o número de peças pelo valor unitário de cada peça e 
 somando esses dois resultados. Finalmente, usamos format() para imprimir 
 o resultado formatado com duas casas decimais.'''






