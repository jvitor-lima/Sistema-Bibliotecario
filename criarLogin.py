
def criarLogin():
    import os, time
    from datetime import date
    os.system('cls')
    print("\033[1;43m\tCriando login...\t\033[m")
    time.sleep(1)
    nome_usuario = input('\033[1;30mDigite o nome de usuário: \033[m')
    arq = open('usuarioscadastrados.csv', 'a')
    arq2 = open('usuarioscadastrados.csv','r')
    lerusers = arq2.readlines()
    for i in lerusers:
        nomedoarq = i.split(';')
        auxnome = nomedoarq[0]
        if nome_usuario == auxnome:
            print('\033[7;30;41mUsuário já existente! Por favor, tente novamente! \033[m')
            time.sleep(1)
            opcaologin = str(input("\033[1;30m[1] - Menu da biblioteca\n[2] - Tentar novamente \nDigite: \033[m"))
            if opcaologin == "1":
                import tela_inicial
                tela_inicial.menuInicial()
            elif opcaologin == "2":
                criarLogin()
            else:
                print("ERRO! não foi digitada a opção corretamente, tente novamente")
                time.sleep(3)
                return criarLogin()
    senha_usuario= input('\033[1;30mDigite sua senha: \033[m')
    conta_usuario = nome_usuario +";"+ senha_usuario
    arq.write('{}\n'.format(conta_usuario))
    print("")
    print('\033[1;42mCadastro realizado com sucesso!\033[m\n')
    time.sleep(1)
    arq.close()  # O arquivo é fechado do modo de adição para ser aberto posteriormente no modo de leitura
    arq2.close()

    Date_required = date.today()
    data = str(Date_required)
    registrologin = nome_usuario+";"+data
    arquivoRegistro = open('registrosusuarios.csv', 'a')
    arquivoRegistro.write(registrologin)
    arquivoRegistro.write("\n")
    arquivoRegistro.close()

    input("\033[1;37mPressione ENTER para voltar ao menu... \033[m")
    time.sleep(1)
    print("")
    import tela_inicial
    tela_inicial.menuInicial()


