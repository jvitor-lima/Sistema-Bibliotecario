
def menuInicial():
    import time, os
    os.system('cls')
    time.sleep(0.1)
    print('\033[1;43m        BEM VINDO A NOSSA BIBLIOTECA         \033[0;0m')
    time.sleep(0.1)
    print('\033[7;37m                                             \033[0;0m')
    time.sleep(0.2)
    print('\033[1;37m|\      \033[1;34m[1] - Criar uma conta              \033[1;37m|| \033[0;0m')
    time.sleep(0.2)
    print('\033[1;37m||      \033[1;34m[2] - Efetuar login                \033[1;37m\| \033[0;0m')
    time.sleep(0.3)
    print('\033[1;37m|\      \033[1;34m[3] - Área do Bibliotecário        \033[1;37m|| \033[0;0m')
    time.sleep(0.3)
    print('\033[1;37m||      \033[1;34m[4] - Para sair do menu            \033[1;37m|\ \033[0;0m')
    time.sleep(0.3)
    print('\033[7;37m                                             \033[m')
    try:
        menu = int(input("\033[1;30mDigite uma opção: \033[m"))
        if menu == 1:
            print("")
            import criarLogin
            criarLogin.criarLogin()

        elif menu == 2:
            print("")
            import logar
            logar.logar()

        elif menu == 3:
            print("")
            import logaradm
            logaradm.logarbibliotecario()

        elif menu == 4:
            print("")
            desejasair = str(input("\033[1;30mDeseja realmente encerrar serrão e sair do sistema? \n[1] - Sim\n[2] - Não\nDigite: \033[m"))
            time.sleep(1)
            if (desejasair == "1") or (desejasair.lower() == "sim"):
                print("\033[1;37mSessão encerrada! Volte sempre \033[1;31m♥\033[m")
                time.sleep(2)
                exit()
            elif desejasair == "2" or desejasair.lower() == "não" or desejasair.lower() == "nao":
                print("\033[1;30mvocê escolheu continuar no sistema\033[m")
                time.sleep(1)
                print("\033[1;30mretornando ao menu...\033[m")
                time.sleep(2)
                return menuInicial()
            else:
                print("opção invalida!\n Por favor digite a opção correta.")
                time.sleep(1)
                print("retornando ao menu...")
                time.sleep(2)
                return menuInicial()
        else:
                print("erro, opção não identificada por favor verifique e digite novamente! ")
                menuInicial()

    except(ValueError, TypeError):
        print("ERRO! por favor digite uma opção valida!")
        time.sleep(1)
        print("Retornando ao menu...")
        time.sleep(2)
        menuInicial()
