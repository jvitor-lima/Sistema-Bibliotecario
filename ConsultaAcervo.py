
def consultarAcervo():
    import os,time
    os.system('cls')
    print('\033[1;30m[1] - \033[mListar todos os livros do acervo')
    print('\033[1;30m[2] - \033[mListar por categoria')
    print('\033[1;30m[3] - \033[mVoltar para menu inicial')
    opcao = str(input("\033[1;30mDigite: \033[m"))
    print("")
    time.sleep(1)
    if opcao == "1":
        os.system('cls')
        print('\t\033[1;37;40m | LIVROS | \033[m')
        arquivo = open('acervo/acervo.csv', 'r')
        for linha in arquivo:
            dado = linha.split(';')
            print(dado[0])
        arquivo.close()
        print("")
        input("\033[1;37mPressione ENTER para voltar ao menu... \033[m")
        import MenuUsuarioLogado
        MenuUsuarioLogado.MenuPrincipal()
        print("")
    elif opcao == "3":
        print("retornando ao menu Inicial...")
        time.sleep(2)
        import MenuUsuarioLogado
        MenuUsuarioLogado.MenuPrincipal()

    elif opcao == "2":
        os.system('cls')
        print("\033[1;43m                                    C A T E G O R I A                                        \033[m")
        print('\033[1;30;44m Ficçao cientifica | Infantil | AutoAjuda | Filosofia | Educação | Administração | Religião  \033[m')
        print("\033[7;37m                                                                                             \033[m")

        categoria = str(input("\033[1;30mDigite o nome da categoria que deseja listar o acervo: \033[m"))
        print("")

        if (categoria.lower() == "infantil") or (categoria.lower() == "infantis") or (categoria.lower() == "infancia"):
            print('\t\033[1;37;40m | LIVROS INFANTIS | \033[m')
            arquivo = open('acervo/acervo.csv','r')
            lerusers = arquivo.readlines()
            for i in lerusers:
                i = i.replace('\n',';')
                nomedoarq = i.split(';')
                arquivoaux = nomedoarq[1]
                arquivoaux2 = nomedoarq[0]
                if arquivoaux == "infantil":
                    print("- ",arquivoaux2)
            print("")
            input("\033[1;37mPressione ENTER para voltar ao menu... \033[m")
            print("")
            time.sleep(1)
            import MenuUsuarioLogado
            MenuUsuarioLogado.MenuPrincipal()


        elif (categoria == "ficção") or (categoria == "ficcao") or (categoria =="ficção cientifica") or (categoria=="livro ficção"):
            print('\t\033[1;37;40m | LIVROS DE FICÇÃO CIENTIFICA | \033[m')
            arquivo = open('acervo/acervo.csv','r')
            lerusers = arquivo.readlines()
            for i in lerusers:
                i = i.replace('\n', ';')
                nomedoarq = i.split(';')
                arquivoaux = nomedoarq[1]
                arquivoaux2 = nomedoarq[0]
                if arquivoaux == "ficcao":
                    print("- ",arquivoaux2)
            print("")
            input("\033[1;37mPressione ENTER para voltar ao menu... \033[m")
            print("")
            time.sleep(1)
            import MenuUsuarioLogado
            MenuUsuarioLogado.MenuPrincipal()


        elif (categoria == "filosofia") or (categoria == "livro de filosofia") or (categoria == "livro filosofia"):
            print('\t\033[1;37;40m | LIVROS DE FILOSOFIA | \033[m')
            arquivo = open('acervo/acervo.csv','r')
            lerusers = arquivo.readlines()
            for i in lerusers:
                i = i.replace('\n', ';')
                nomedoarq = i.split(';')
                arquivoaux = nomedoarq[1]
                arquivoaux2 = nomedoarq[0]
                if arquivoaux == "filosofia":
                    print("- ", arquivoaux2)
            print("")
            input("\033[1;37mPressione ENTER para voltar ao menu... \033[m")
            print("")
            import MenuUsuarioLogado
            MenuUsuarioLogado.MenuPrincipal()

        elif (categoria.lower() == "autoajuda") or (categoria.lower() == "ajuda") or (categoria.lower() == "Auto") or (categoria.lower() == "autoajudar"):
            print('\t\033[1;37;40m | LIVROS DE AUTOAJUDA | \033[m')
            arquivo = open('acervo/acervo.csv','r')
            lerusers = arquivo.readlines()
            for i in lerusers:
                i = i.replace('\n', ';')
                nomedoarq = i.split(';')
                arquivoaux = nomedoarq[1]
                arquivoaux2 = nomedoarq[0]
                if arquivoaux == "autoajuda":
                    print("- ", arquivoaux2)
            print("")
            input("\033[1;37mPressione ENTER para voltar ao menu... \033[m")
            print("")
            import MenuUsuarioLogado
            MenuUsuarioLogado.MenuPrincipal()

        elif (categoria.lower() == "educacao") or (categoria.lower() == "educar") or (categoria.lower() == "educação") or (categoria.lower() == "edu"):
            print('\t\033[1;37;40m | LIVROS DE EDUCAÇÃO | \033[m')
            arquivo = open('acervo/acervo.csv','r')
            lerusers = arquivo.readlines()
            for i in lerusers:
                i = i.replace('\n', ';')
                nomedoarq = i.split(';')
                arquivoaux = nomedoarq[1]
                arquivoaux2 = nomedoarq[0]
                if arquivoaux == "educacao":
                    print("- ", arquivoaux2)
            print("")
            input("\033[1;37mPressione ENTER para voltar ao menu... \033[m")
            print("")
            import MenuUsuarioLogado
            MenuUsuarioLogado.MenuPrincipal()

        elif (categoria.lower() == "administracao") or (categoria.lower() == "adm") or (categoria.lower() == "administração"):
            print('\t\033[1;37;40m | LIVROS DE ADMINISTRAÇÃO | \033[m')
            arquivo = open('acervo/acervo.csv','r')
            lerusers = arquivo.readlines()
            for i in lerusers:
                i = i.replace('\n', ';')
                nomedoarq = i.split(';')
                arquivoaux = nomedoarq[1]
                arquivoaux2 = nomedoarq[0]
                if arquivoaux == "administracao":
                    print("- ", arquivoaux2)
            print("")
            input("\033[1;37mPressione ENTER para voltar ao menu... \033[m")
            print("")
            import MenuUsuarioLogado
            MenuUsuarioLogado.MenuPrincipal()

        elif (categoria.lower() == "religiao") or (categoria.lower() == "religião") or (categoria == "igreja") or (categoria == "evangelico"):
            print('\t\033[1;37;40m | LIVROS DE RELIGIÃO | \033[m')
            arquivo = open('acervo/acervo.csv','r')
            lerusers = arquivo.readlines()
            for i in lerusers:
                i = i.replace('\n', ';')
                nomedoarq = i.split(';')
                arquivoaux = nomedoarq[1]
                arquivoaux2 = nomedoarq[0]
                if arquivoaux == "religiao":
                    print("- ", arquivoaux2)
            print("")
            input("\033[1;37mPressione ENTER para voltar ao menu... \033[m")
            print("")
            import MenuUsuarioLogado
            MenuUsuarioLogado.MenuPrincipal()

        else:
            print("categoria não encontrada, por favor verifique as categorias disponiveis e tente novamente!")
            time.sleep(3)
            consultarAcervo()

    else:
        print("opção invalida por favor tente novamente!")
        time.sleep(2)
        consultarAcervo()


