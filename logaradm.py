import os,time
def logarbibliotecario():
    os.system('cls')
    arquiv = open('admin_account.csv')  # abrindo no modo de leitura
    print("\033[1;43m\tEfetuando login... \033[7;30;41m [MODO: Desenvolvedor]\t\033[m")
    time.sleep(2)
    nome_loginadm = input('\033[1;30mDigite o seu nome de usuário: \033[m')
    senha_loginadm = input('\033[1;30mDigite sua senha: \033[m')
    time.sleep(1)
    conta_loginadm = nome_loginadm.lower() +';'+ senha_loginadm.lower()
    registrados = arquiv.readlines()

    if conta_loginadm + '\n' in registrados:
        os.system('cls')
        print("")
        print('Seja bem vindo ''\033[31m''{}''\033[0;0,m'', à nossa biblioteca!'.format(nome_loginadm)) #comando  ->  '\033[33m'   para atribuir a cor amarela
        print("")
        input("\033[1;37mPressione ENTER para voltar ao menu... \033[m")
        import paineladm
        paineladm.menuadm()
    else:
        os.system('cls')
        print("")
        print('\033[7;41mTem certeza que digitou corretamente? Por favor, verifique e tente novamente!\033[m')
        continuar = str(input("\033[1;37mDigite '\033[32mSim\033[m'\033[1;37m para tentar novamente...\033[m"))
        if continuar.lower() == "sim" or "s":
            print("")
            logarbibliotecario()
        else:
            os.system('cls')
            print("Programa encerrado!")

    arquiv.close()
