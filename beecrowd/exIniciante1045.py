''' 
Tipos de Triângulos
Adaptado por Neilor Tonin, URI  Brasil

Timelimit: 1
Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente, de modo que o 
lado A representa o maior dos 3 lados. A seguir, determine o tipo de triângulo que estes 
três lados formam, com base nos seguintes casos, sempre escrevendo uma mensagem adequada:

se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO
se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO
se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO

se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES
Entrada
A entrada contem três valores de ponto flutuante de 
dupla precisão A (0 < A) , B (0 < B) e C (0 < C).

Saída
Imprima todas as classificações do triângulo especificado na entrada.

Exemplos de Entrada	Exemplos de Saída
7.0 5.0 7.0         TRIANGULO ACUTANGULO
                    TRIANGULO ISOSCELES

6.0 6.0 10.0        TRIANGULO OBTUSANGULO
                    TRIANGULO ISOSCELES
'''

lados = [float(x) for x in input().split()]
lados.sort()
lados.reverse()
a,b,c = [x for x in lados]

if a >= b + c:
    print("NAO FORMA TRIANGULO")
else:
    if a*a == b*b + c*c:
        print("TRIANGULO RETANGULO")
    elif a*a > b*b + c*c:
        print("TRIANGULO OBTUSANGULO")
    elif a*a < b*b + c*c:
        print("TRIANGULO ACUTANGULO")
    if a == b and c == a:
        print("TRIANGULO EQUILATERO")
    elif a == b or b == c or c == a:
        print("TRIANGULO ISOSCELES")

