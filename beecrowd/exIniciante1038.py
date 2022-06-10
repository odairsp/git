''' 
Lanche
Adaptado por Neilor Tonin, URI  Brasil

Timelimit: 1
Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.

1 cachorro quente 4,00
2 x-salada 4,50
3 x bacon 5,00
4 torrada simples 2,00
5 refrierante 1,50
Entrada
O arquivo de entrada contém dois valores inteiros correspondentes ao 
código e à quantidade de um item conforme tabela acima.

Saída
O arquivo de saída deve conter a mensagem 
"Total: R$ " seguido pelo valor a ser pago, com 2 casas após 
o ponto decimal.

Exemplo de Entrada	Exemplo de Saída
3 2

Total: R$ 10.00

4 3

Total: R$ 6.00
'''
tabela = {1: 4, 2: 4.5, 3: 5, 4: 2, 5: 1.5}
pedido = [int(x) for x in input().split()]

if pedido[0] in tabela:
    print("Total: R$ %.2f" % (pedido[1]*tabela[pedido[0]]))
