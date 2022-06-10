"""
Escreva um programa de preparo de pizzas onde o usuario pode escolher 5
ingredientes ou menos para fazer a pizza. No fim mostrar os ingredientes
escolhidos.
"""

ingredientes = ["queijo", "presunto", "tomate", "calabresa", "cebola", "ovo",
                "pimentão", "abacaxi"]

qtdIngredientes = 1
pizza = []
escolha = ""

print("Escolha até 5 ingredientes para sua pizza ou 0 para terminar: ")
while qtdIngredientes <= 5:
    contador = 1
    for ingrediente in ingredientes:
        print(contador, "-", ingrediente)
        contador += 1

    escolha = input("Escolha o %d. ingrediente: " % qtdIngredientes)

    if escolha.isdigit():
        if int(escolha) > 0 and int(escolha) <= len(ingredientes):
            if ingredientes[int(escolha)-1] not in pizza:
                qtdIngredientes += 1
                pizza.append(ingredientes[int(escolha)-1])
                print("Você escolheu", pizza, ".")
            else:
                print("Você já escolheu", pizza, ".")
        elif int(escolha) == 0:
            break
        else:
            print("Escolha inváliva")
            break
    else:
        print("Escolha inváliva")

print("Sua pizza de", pizza, "está sendo preparada tenha um bom dia!")
