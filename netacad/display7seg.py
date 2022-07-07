numeros = [
    ["000","0 0","0 0","0 0","000"],
    [" 1 ","11 "," 1 "," 1 ","111"],
    ["222","  2","222","2  ","222"],
    ["333","  3","333","  3","333"],
    ["4 4","4 4","444","  4","  4"],
    ["555","5  ","555","  5","555"],
    ["666","6  ","666","6 6","666"],
    ["777"," 7 "," 7 ","7  ","7  "],
    ["888","8 8","888","8 8","888"],
    ["999","9 9","999","  9","999"]
]

while True:
    numero  = input("\nDigite o numero desejado: ")
    if len(numero) <= 0 or not numero.isdigit():
        print("Numero invalido!")
    else:
        numeroPrint = []
        for digit in numero:
            numeroPrint.append(numeros[int(digit)])
        for x in range(5):
            print()
            for y in range(len(numeroPrint)):
                print(numeroPrint[y][x], end="   ")    

