''' 
Teste de Seleção 1
Adaptado por Neilor Tonin, URI  Brasil

Timelimit: 1
Leia 4 valores inteiros A, B, C e D. 
A seguir, se B for maior do que C e se D for maior do que A, 
e a soma de C com D for maior que a soma de A e B e se C e D, 
ambos, forem positivos e se a variável A for par 
escrever a mensagem "Valores aceitos", 
senão escrever "Valores nao aceitos".

Entrada
Quatro números inteiros A, B, C e D.

Saída
Mostre a respectiva mensagem após a validação dos valores.

Exemplo de Entrada	
5 6 7 8

Exemplo de Saída
Valores nao aceitos

Exemplo de Entrada
2 3 2 6

Exemplo de Saída
Valores aceitos
'''

abcd = [int(x) for x in input().split()]

if abcd[1] > abcd[2] and abcd[3] > abcd[0] and \
    (abcd[2] + abcd[3]) > (abcd[0] + abcd[1]) and \
        abcd[2] >= 0 and abcd[3] >= 0 and abcd[0] % 2 == 0:

    print("Valores aceitos")
else:
    print("Valores nao aceitos")
