import os


# senha tem permissão
def tem_permissao(senha):
    pass


# confere se existe a senha
def conferir_senha(senha):
    senhas = open(os.path.dirname(os.path.dirname(__file__)) +
                  "\\exerciciosArquivos\\"+"senhas.txt", "r")
    lista_senhas = senhas.readlines()
    senhas.close()

    for s in lista_senhas:
        if senha == s.split()[1]:
            return [True, s.split()]
    return [False]


# cria arquivo
def criar_arquivo(senha):
    try:
        nome_arquivo = input("Digite o nome do arquivo .txt a ser criado: ")
        arquivo = open(os.path.dirname(os.path.dirname(__file__)) +
                       "\\exerciciosArquivos\\" + nome_arquivo + ".txt", "x")
        arquivo.close()
        print("Arquivo criado com sucesso!\n")
    except FileNotFoundError:
        print("Nome de arquivo invalido!\n")


# ler arquivo
def ler_arquivo(senha):
    try:
        lista = os.listdir(os.path.dirname(os.path.dirname(__file__)) +
                           "\\exerciciosArquivos\\")
        for iten in lista:
            if iten.endswith(".txt"):
                print(iten)
        nome_arquivo = input("Digite o nome do arquivo: ")
        print("\nLendo arquivo %s: \n" % nome_arquivo)
        file = open(nome_arquivo, "r")
        for linha in file:
            print(linha, end="")
        file.close()
        print("\nFIM!")
    except FileNotFoundError:
        print("Arquivo inexistente!\n")


# modificar o conteudo
def modificar_arquivo(senha):
    try:
        lista = os.listdir(os.path.dirname(os.path.dirname(__file__)) + "\\exerciciosArquivos\\")
        for iten in lista:
            if iten.endswith(".txt"):
                print(iten)
        nome_arquivo = input("Digite o nome do arquivo: ")
        os.system("notepad.exe" + nome_arquivo)
        print("Arquivo modificado!")
    except FileNotFoundError:
        print("Arquivo inexistente!\n")


# deletar arquivo
def deletar_arquivo(senha):
    try:
        lista = os.listdir(os.path.dirname(os.path.dirname(__file__)) + "\\exerciciosArquivos\\")
        for iten in lista:
            if iten.endswith(".txt"):
                print(iten)
        nome_arquivo = input("Digite o nome do arquivo: ")
        os.remove(nome_arquivo)
        print("Arquivo deletado!")
    except FileNotFoundError:
        print("Arquivo inexistente!\n")


# existe senhas
def existe_senhas():
    if not os.path.isfile("senhas.txt"):
        print("\nDigite as senhas de controle: ")
        file = open("senhas.txt", "x")
        tipos = ["Criar", "Ler", "Modificar", "Apagar"]
        for x in range(4):
            file.write("%i " % (x+1) + input("%i Senha %s arquivo: " %
                       ((x+1), tipos[x]))+"\n")
        file.close()
    else:
        return True
