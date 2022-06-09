"""
Escreva um programa de preparo de pizzas onde o usuario pode escolher 5
ingredientes ou menos para fazer a pizza. No fim mostrar os ingredientes
escolhidos.
"""

ingredientes = ["queijo", "presunto", "tomate", "ovo", "carne seca"]
pizza = []
qtdIngredientes = 0
opcao = ""

print("\nEscolha até 5 ingredientes para sua pizza ou 0 para terminar!")

while qtdIngredientes < 5:
    cont = 1
    for ingrediente in ingredientes:
        print(cont, "-", ingrediente)
        cont += 1
    opcao = input("Escolha o %d ingrediente: " % (qtdIngredientes+1))
    if opcao.isdigit():
        if int(opcao) > 0 and int(opcao) < len(ingredientes):
            if ingredientes[int(opcao)-1] not in pizza:
                pizza.append(ingredientes[int(opcao)-1])
                qtdIngredientes += 1
                print("\nVocê escolheu ", pizza, ".")
            else:
                print("\nVocê já escolheu", pizza, ".")
        elif int(opcao) == 0:
            break

        else:
            print("\nOpcção inválida")
    else:
        print("\nOpcção inválida")
print("\nSua pizza de", pizza, "esta sendo preparada tenha um bom dia!\n")
