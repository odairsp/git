from funcoes import existe_senhas, conferir_senha, criar_arquivo, ler_arquivo,\
    modificar_arquivo, deletar_arquivo


# xxxxxxxxxxxxxxxxxxxx   INICIO   xxxxxxxxxxxxxxxxxxxx
while True:
    existe_senhas()
    senha = input("Digite sua senha: ")
    senha = conferir_senha(senha)
    while True:
        if senha[0]:
            print("\n", "-"*10, "Tarefas", "-"*10)
            print("1 - Criar arquivo")
            print("2 - Ler arquivo")
            print("3 - Modificar conteúdo do arquivo")
            print("4 - Apagar um arquivo")
            print("0 - Sair")
            tarefa = input("Escolha uma tarefa: ")
            if tarefa == "1" and senha[1][0] == "1":
                criar_arquivo(senha)
            elif tarefa == "2" and senha[1][0] == "2":
                ler_arquivo(senha)
            elif tarefa == "3" and senha[1][0] == "3":
                modificar_arquivo(senha)
            elif tarefa == "4" and senha[1][0] == "4":
                deletar_arquivo(senha)
            elif tarefa == "0":
                break
            else:
                print("Sua senha não tem permissão!\n")
        else:
            print("Senha não confere!\n")
            break
