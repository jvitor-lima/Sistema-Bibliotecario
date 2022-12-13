def logar():
    import os, time
    os.system('cls')
    arq = open('usuarioscadastrados.csv','r')  # abrindo no modo de leitura
    print("\033[1;43m\tEfetuando login...\t\033[m")
    time.sleep(2)
    try:
        nome_login = input('\033[1;30mDigite o seu nome de usuario: \033[m')
        senha_login = input('\033[1;30mDigite sua senha: \033[m')
        conta_login = nome_login.lower() +';'+ senha_login.lower()
        registrados = arq.readlines()
        if conta_login + '\n' in registrados:
            print("")
            print('Seja bem vindo ''\033[32m''{}''\033[0;0,m'', à nossa biblioteca!'.format(nome_login)) #comando  ->  '\033[33m'   para atribuir a cor amarela
            print("")
            time.sleep(1)
            input("\033[1;37mPressione ENTER para voltar ao menu... \033[m")
            arq.close()
            cachelogado = open('usuariologadotemporario.csv','w')
            cachelogado.write(nome_login)
            cachelogado.close()
            import MenuUsuarioLogado
            MenuUsuarioLogado.MenuPrincipal()
        else:
            print("")
            print('\033[7;41mTem certeza que digitou corretamente? Por favor, verifique e tente novamente!\033[m')
            print("")
            print("retornando ao Menu...")
            time.sleep(4)
            arq.close()
            import tela_inicial
            tela_inicial.menuInicial()
    except (ValueError, TypeError):
        print("ERRO! por favor informe os dados corretamente")
        time.sleep(2)
        print("retornando ao sistema de login...")
        time.sleep(2)






