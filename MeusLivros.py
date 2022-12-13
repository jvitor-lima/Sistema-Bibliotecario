
def MeusLivrosReservados():
    import os, time
    os.system('cls')
    abrirnome = open('usuariologadotemporario.csv')
    nomecache = abrirnome.readlines()
    nomedousuario = str(nomecache)[2:-2]
    diretorio = 'acervo/' + nomedousuario + '_livroreservado.csv'
    existe = os.path.exists(diretorio)
    if existe:
        from datetime import date, datetime
        livroreservado = open('acervo/'+nomedousuario+'_livroreservado.csv')
        lerlivro = livroreservado.readlines()
        nomelivro = lerlivro[0]
        prazolivro = lerlivro[1]
        vencimentolivro = lerlivro[2]
        Date_required = date.today()
        dataatual = Date_required
        stringvecimento = datetime.strptime(vencimentolivro, "%Y-%m-%d").date()
        print("Olá,", nomedousuario)
        print("seu livro reservado é: ",nomelivro)
        time.sleep(2)
        media = (dataatual - stringvecimento)
        media2 = (stringvecimento - dataatual)
        if dataatual > stringvecimento:
             print("Você está em atraso com a biblioteca!")
             time.sleep(1)
             print("O livro está atrasado {} dias com a biblioteca ".format(media.days))
             print("")
             time.sleep(2)
             print("retornando ao menu...")
             time.sleep(5)
             import MenuUsuarioLogado
             MenuUsuarioLogado.MenuPrincipal()

        elif dataatual < stringvecimento:
            print("o livro esta em dias com a biblitoeca")
            time.sleep(1)
            print("faltam {} dias para o livro vencer a biblioteca ".format(media2.days))
            time.sleep(2)
            print("retornando ao menu...")
            time.sleep(4)
            import MenuUsuarioLogado
            MenuUsuarioLogado.MenuPrincipal()

        elif dataatual == stringvecimento:
            print("o livro esta em dias com a biblitoeca")
            time.sleep(1)
            print("faltam {} dias para o livro vencer a biblioteca ".format(media2.days))
            time.sleep(1)
            print("Atenção o livro vence hoje, lembre-se de devolver para não ser multado")
            time.sleep(3)
            print("retornando ao menu...")
            time.sleep(5)
            import MenuUsuarioLogado
            MenuUsuarioLogado.MenuPrincipal()
    else:
        print("erro, você não possui livros reservados!")
        time.sleep(1)
        print("retornando ao menu...")
        time.sleep(3)
        import MenuUsuarioLogado
        MenuUsuarioLogado.MenuPrincipal()

