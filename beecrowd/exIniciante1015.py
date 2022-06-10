'''
Distância Entre Dois Pontos
Adaptado por Neilor Tonin, URI  Brasil

Timelimit: 1
Leia os quatro valores correspondentes aos eixos x e y de dois pontos
quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre
eles, mostrando 4 casas decimais após a vírgula, segundo a fórmula:

Distancia = raiz (x2 - x1)^2 + (y2 - y1)^2

Entrada
O arquivo de entrada contém duas linhas de dados. A primeira linha
contém dois valores de ponto flutuante: x1 y1 e a segunda linha contém
dois valores de ponto flutuante x2 y2.

Saída
Calcule e imprima o valor da distância segundo a fórmula fornecida,
com 4 casas após o ponto decimal.

Exemplo de Entrada
1.0 7.0
5.0 9.0


Exemplo de Saída
4.4721
'''

xy1 = [float(x) for x in input().split()]
xy2 = [float(x) for x in input().split()]

distancia = ((xy2[0] - xy1[0])**2 + (xy2[1] - xy1[1])**2) ** 0.5

print("%.4f" % distancia)
