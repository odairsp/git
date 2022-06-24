
while True:
    try:
        entrada = input()
    except EOFError as e:
        break
    entrada = entrada.split()
    hora = int(entrada[0])
    min = int(entrada[1])
    print("%02d:%02d" % (hora/30, min/6 ))

