''' 
Fórmula de Bhaskara
Adaptado por Neilor Tonin, URI  Brasil

Timelimit: 1
Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da 
equação de Bhaskara. Se não for possível calcular as raízes, 
mostre a mensagem correspondente “Impossivel calcular”, 
caso haja uma divisão por 0 ou raiz de numero negativo.

Entrada
Leia três valores de ponto flutuante (double) A, B e C.

Saída
Se não houver possibilidade de calcular as raízes, apresente a 
mensagem "Impossivel calcular". Caso contrário, imprima o 
resultado das raízes com 5 dígitos após o ponto, 
com uma mensagem correspondente conforme exemplo abaixo. 
Imprima sempre o final de linha após cada mensagem.

Exemplos de Entrada	    Exemplos de Saída
10.0 20.1 5.1           R1 = -0.29788
                        R2 = -1.71212

0.0 20.0 5.0            Impossivel calcular

10.3 203.0 5.0          R1 = -0.02466
                        R2 = -19.68408

10.0 3.0 5.0            Impossivel calcular

'''

abc = [float(x) for x in input().split()]

delta = abc[1]**2 - (4*abc[0]*abc[2])

if delta >= 0 and abc[0] > 0:
    x1 = (-abc[1] + delta**0.5) / (2*abc[0])
    x2 = (-abc[1] - delta**0.5) / (2*abc[0])
    print("R1 = %.5f" % x1)
    print("R2 = %.5f" % x2)
else:
    print("Impossivel calcular")
