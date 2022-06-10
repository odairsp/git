''' 
Triângulo
Adaptado por Neilor Tonin, URI  Brasil

Timelimit: 1
Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo.
Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:

a + b < c
a + c < b
b + c < c

Perimetro = XX.X

Em caso negativo, calcule a área do trapézio que tem A e B como base e C como
altura, mostrando a mensagem

Area = XX.X

Entrada
A entrada contém três valores reais.

Saída
O resultado deve ser apresentado com uma casa decimal.

Exemplo de Entrada	Exemplo de Saída
6.0 4.0 2.0         Area = 10.0

6.0 4.0 2.1         Perimetro = 12.1
'''

a, b, c = [float(x) for x in input().split()]

if (a + b) > c and (a + c) > b and (b + c) > a:
    print("Perimetro = %.1f" % (a + b + c))
else:
    print("Area = %.1f" % (((a+b)*c)/2))
