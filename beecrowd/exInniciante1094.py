'''
Experiências
Adaptado por Neilor Tonin, URI  Brasil

Timelimit: 1
Maria acabou de iniciar seu curso de graduação na faculdade de 
medicina e precisa de sua ajuda para organizar os experimentos 
de um laboratório o qual ela é responsável. Ela quer saber no 
final do ano, quantas cobaias foram utilizadas no laboratório e o 
percentual de cada tipo de cobaia utilizada.

Este laboratório em especial utiliza três tipos de cobaias: 
sapos, ratos e coelhos. Para obter estas informações, 
ela sabe exatamente o número de experimentos que foram realizados, 
o tipo de cobaia utilizada e a quantidade de cobaias utilizadas em 
cada experimento.

Entrada
A primeira linha de entrada contém um valor inteiro N que indica os 
vários casos de teste que vem a seguir. Cada caso de teste contém 
um inteiro Quantia (1 ≤ Quantia ≤ 15) que representa a quantidade 
de cobaias utilizadas e um caractere Tipo ('C', 'R' ou 'S'), 
indicando o tipo de cobaia (R:rato S:Sapo C:Coelho).

Saída
Apresente o total de cobaias utilizadas, o total de cada tipo de 
cobaia utilizada e o percentual de cada uma em relação ao total de 
cobaias utilizadas, sendo que o percentual deve ser apresentado 
com dois dígitos após o ponto.

Exemplo de Entrada	Exemplo de Saída
10
10 C
6 R
15 S
5 C
14 R
9 C
6 R
8 S
5 C
14 R

Total: 92 cobaias
Total de coelhos: 29
Total de ratos: 40
Total de sapos: 23
Percentual de coelhos: 31.52 %
Percentual de ratos: 43.48 %
Percentual de sapos: 25.00 %
'''
experimento = {"coelhos": 0, "ratos": 0, "sapos": 0, }

n = int(input())
animais = []
for x in range(n):
    animais.append([n.upper() for n in input().split()])
soma = 0
for x in animais:
    soma += int(x[0])
    if x[1] == "R":
        experimento["ratos"] += int(x[0])
    elif x[1] == "S":
        experimento["sapos"] += int(x[0])
    elif x[1] == "C":
        experimento["coelhos"] += int(x[0])


print("Total: %i cobaias" % soma)
for animal, qtd in experimento.items():
    print("Total de %s: %i" % (animal, qtd))

for animal, qtd in experimento.items():
    print(f"Percental de {animal}: {round((qtd*100/soma)),2} %")
