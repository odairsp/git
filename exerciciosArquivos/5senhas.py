import funcoes


# xxxxxxxxxxxxxxxxxxxx   INICIO   xxxxxxxxxxxxxxxxxxxx
while True:
    funcoes.existe_senhas()
    senha = input("Digite sua senha: ")
    senha = funcoes.conferir_senha(senha)
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
                funcoes.criar_arquivo(senha)
            elif tarefa == "2" and senha[1][0] == "2":
                funcoes.ler_arquivo(senha)
            elif tarefa == "3" and senha[1][0] == "3":
                funcoes.modificar_arquivo(senha)
            elif tarefa == "4" and senha[1][0] == "4":
                funcoes.deletar_arquivo(senha)
            elif tarefa == "0":
                break
            else:
                print("Sua senha não tem permissão!\n")
        else:
            print("Senha não confere!\n")
            break
