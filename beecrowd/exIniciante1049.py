''' 
Animal
Por Neilor Tonin, URI  Brasil

Timelimit: 1
Neste problema, você deverá ler 3 palavras que definem o tipo de 
animal possível segundo o esquema abaixo, da esquerda para a direita.  
Em seguida conclua qual dos animais seguintes foi escolhido, através 
das três palavras fornecidas.



Entrada
A entrada contém 3 palavras, uma em cada linha, necessárias para 
identificar o animal segundo a figura acima, com todas as letras 
minúsculas.

Saída
Imprima o nome do animal correspondente à entrada fornecida.

Exemplos de Entrada	    Exemplos de Saída
vertebrado              homem
mamifero                
onivoro                 

vertebrado              aguia
ave
carnivoro

invertebrado            minhoca
anelideo
onivoro

'''
animal1 = input()
animal2 = input()
animal3 = input()

if animal1 == "vertebrado":
    if animal2 == "ave":
        if animal3 == "carnivoro":
            print("aguia")
        else:
            print("pomba")
    else:
        if animal3 == "onivoro":
            print("homem")
        else:
            print("vaca")
else:
    if animal2 == "inseto":
        if animal3 == "hematofago":
            print("pulga")
        else:
            print("lagarta")
    else:
        if animal3 == "hematofago":
            print("sanguessuga")
        else:
            print("minhoca")
