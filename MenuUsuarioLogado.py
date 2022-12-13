import time,os
def MenuPrincipal():
    try:
        os.system('cls')
        print("\033[1;43m           MENU PRINCIPAL            \033[m")
        print("\033[7;37m                                     \033[m")
        print("\033[1;37m|\   \033[34m[1] - Consultar Acervo\033[37m        \| \033[37m")
        print("\033[1;37m||   \033[34m[2] - Reservar Livros\033[37m         || \033[37m")
        print("\033[1;37m\|   \033[34m[3] - Meus Livros Reservados\033[37m  |\ \033[37m")
        print("\033[1;37m||   \033[34m[4] - Devolver Livro\033[37m          || \033[37m")
        print("\033[1;37m||   \033[34m[5] - Alterar Dados da Conta\033[37m  || \033[37m")
        print("\033[1;37m\|   \033[34m[6] - Encerrar Sessão\033[37m         |\ \033[37m")
        print("\033[7;37m                                     \033[m")
        opcaoMenu = int(input("\033[1;30mDigite: \033[m"))
        time.sleep(1)

        if opcaoMenu == 1:
            print("")
            import ConsultaAcervo
            ConsultaAcervo.consultarAcervo()

        elif opcaoMenu == 2:
            print("")
            import ReservarLivro
            ReservarLivro.reservar()

        elif opcaoMenu == 3:
            print("")
            import MeusLivros
            MeusLivros.MeusLivrosReservados()

        elif opcaoMenu == 4:
            print("")
            import devolverLivro
            devolverLivro.retornarLivro()

        elif opcaoMenu == 5:
            print("")
            import alterarLogin
            alterarLogin.editarLogin()

        elif opcaoMenu == 6:
            print("")
            desejasair = str(input("\033[1;30mDeseja realmente encerrar serrão e sair do sistema? \n[1] - Sim\n[2] - Não\nDigite: \033[m"))
            time.sleep(1)
            if (desejasair == "1") or (desejasair.lower() == "sim"):
                print("\033[1;37mSessão encerrada! Volte sempre \033[1;31m♥\033[m")
                time.sleep(2)
                exit()

            elif (desejasair == "2") or (desejasair.lower() == "não") or (desejasair.lower() == "nao"):
                print("\033[1;30mvocê escolheu continuar no sistema\033[m")
                time.sleep(1)
                print("\033[1;30mretornando ao menu...\033[m")
                time.sleep(2)
                return MenuPrincipal()

            else:
                print("")
                print("\033[7;41mTem certeza que digitou corretamente? Por favor, verifique e tente novamente!\033[m")
                time.sleep(2)
                print("retornando ao menu...")
                time.sleep(2)
                MenuPrincipal()

    except (ValueError,TypeError):
        print("erro, verifique se você digitou a opção do menu corretamente. ")
        print("retornando ao menu...")
        time.sleep(3)
        MenuPrincipal()

    except (KeyboardInterrupt):
        quit()

