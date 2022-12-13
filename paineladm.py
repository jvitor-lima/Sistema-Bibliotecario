
def menuadm():
    import time, os

    os.system('cls')
    print("\033[1;43m           PAINEL DE CONTROLE         \033[m")
    print("\033[7;37m                                      \033[m")
    print("\033[1;37m\|  \033[34m[1] - Inserir Livro ao Acervo\033[37m   |\ \033[m")
    print("\033[1;37m||  \033[34m[2] - Remover Livro do Acervo\033[37m   || \033[m")
    print("\033[1;37m|\  \033[34m[3] - Listar Usuários\033[37m           \| \033[m")
    print("\033[1;37m|\  \033[34m[4] - Ver dividas Livros\033[37m        \| \033[m")
    print("\033[1;37m||  \033[34m[5] - Excluir Usuários\033[37m          || \033[m")
    print("\033[1;37m||  \033[34m[6] - Registro de Livros\033[37m        || \033[m")
    print("\033[1;37m||  \033[34m[7] - Registro de Usuarios\033[37m      || \033[m")
    print("\033[1;37m\|  \033[34m[8] - Encerrar Sessão\033[37m           |\ \033[m")
    print("\033[7;37m                                      \033[m")
    try:
        opcaoMenu = int(input("\033[1;30mDigite a opção: \033[m"))

        if opcaoMenu == 1:
            print("")
            import cadastrarlivro
            cadastrarlivro.cadlivroacervo()

        elif opcaoMenu == 2:
            print("")
            import excluirLivro
            excluirLivro.deletarLivro()

        elif opcaoMenu == 3:
            print("")
            import listarUsuarios
            listarUsuarios.listarUsers()

        elif opcaoMenu == 4:
            print("")
            import dividasLivros
            dividasLivros.dividasLivros()

        elif opcaoMenu == 5:
            print("")
            import excluirLogin
            excluirLogin.deletarLogin()

        elif opcaoMenu == 6:
            print("")
            import RegistrosCadLivros
            RegistrosCadLivros.RegistroAcervo()

        elif opcaoMenu == 7:
            print("")
            import RegistrosUsuarios
            RegistrosUsuarios.RegistroUsers()

        elif opcaoMenu == 8:
            print("")
            desejasair = str(
                input("Deseja realmente encerrar serrão e sair do sistema? \n[1] - Sim\n[2] - Não\nDigite: "))
            time.sleep(1)
            if desejasair == "1" or desejasair.lower() == "sim":
                print("\033[1;37mSessão encerrada! Volte sempre \033[1;31m<3\033[m")
                time.sleep(2)
                exit()
            elif desejasair == "2" or desejasair.lower() == "não" or desejasair.lower() == "nao":
                return menuadm()

        else:
            print("")
            print("\033[1;41mERRO!\033[7;30;41m Por favor, digite uma opção existente!\033[m")
            time.sleep(2)
            menuadm()
    except (TypeError, ValueError):
        print("\033[1;41mERRO!\033[7;30;41mDigite uma opção valida!\033[m")
        time.sleep(2)
        menuadm()

