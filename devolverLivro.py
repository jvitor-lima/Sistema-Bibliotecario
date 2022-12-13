# AINDA EM FASE DE TESTES, NÃO ALTERAR DADOS
def retornarLivro ():
    import os, time
    abrirnome = open('usuariologadotemporario.csv')
    nomecache = abrirnome.readlines()
    nomedousuario = str(nomecache)[2:-2]
    print("Olá,",nomedousuario)
    time.sleep(1)
    diretorio = 'acervo/'+nomedousuario+'_livroreservado.csv'
    existe = os.path.exists(diretorio)
    if existe:
        from datetime import date, datetime
        livroreservado = open('acervo/'+nomedousuario+'_livroreservado.csv', 'r')
        lerlivro = livroreservado.readlines()
        nomelivro = lerlivro[0]
        prazolivro = lerlivro[1]
        vencimentolivro = lerlivro[2]
        Date_required = date.today()
        dataatual = Date_required
        stringvecimento = datetime.strptime(vencimentolivro, "%Y-%m-%d").date()
        print("nome do livro: ",nomelivro)
        time.sleep(2)
        print("a data de vencimento é : ",stringvecimento)
        media = (dataatual - stringvecimento)
        media2 = (stringvecimento - dataatual)
        if dataatual > stringvecimento:
            print("")
            time.sleep(2)
            print("o livro esta em atraso com a biblitoeca")
            time.sleep(1)
            print("O livro está atrasado {} dias com a biblioteca ".format(media.days))
            convertervalor = int(media.days)
            mediajuros = convertervalor * 0.25
            time.sleep(2)
            print("a multa do atraso é de 25 centavos ao dia, sua multa é de {} ".format(mediajuros))
            enviarparabb = str(input("deseja fazer o pagamento? \n1- Sim\n2- Não\nDigite a opção: "))
            if enviarparabb == "1" or "Sim" or "sim" or "s":
                print("foi enviada uma requisição para os Bibliotecarios para verificar se sua divida foi paga!")
                time.sleep(2)
                print("assim que os bibliotecarios verificarem e autorizarem, seu livro será devolvido e você poderá "
                      "reservar livros na biblioteca novamente")
                criararquivo = open('.\\usuariosdividas/'+nomedousuario+'PagamentoLivro.csv','w')
                criararquivo.write(nomedousuario)
                criararquivo.write(";")
                criararquivo.write("{}".format(mediajuros))
                criararquivo.write("\n")
                criararquivo.close()
                time.sleep(6)
                import MenuUsuarioLogado
                MenuUsuarioLogado.MenuPrincipal()

        elif dataatual < stringvecimento:
            print("o livro esta em dias com a biblitoeca")
            print("faltam {} dias para o livro vencer a biblioteca ".format(media2.days))
            devolver = str(input("deseja devolver o livro para o acervo da biblioteca? \n1- Sim \n2- Não"))
            if devolver.lower() == "sim" or "s" or "yes" or "y":
                categorialivro = str(input("digite o nome da categoria do livro: "))
                arquivo = open('acervo/acervo.csv', 'a')
                arquivo.write(nomelivro + ";" + categorialivro)
                arquivo.close()
                livroreservado.close()
                os.remove(diretorio)
                print("livro devolvido com sucesso!")
                os.system('cls')
                import MenuUsuarioLogado
                MenuUsuarioLogado.MenuPrincipal()

        elif dataatual == stringvecimento:
            print("o livro esta em dias com a biblitoeca")
            print("faltam {} dias para o livro vencer a biblioteca ".format(media2.days))
            print("Atenção o livro vence hoje, lembre-se de devolver para não ser multado")
            devolver = str(input("deseja devolver o livro para o acervo da biblioteca? \n1- Sim \n2- Não\nDigite:  "))
            if devolver.lower() == "sim" or "s" or "yes" or "y":
                categorialivro = str(input("digite o nome da categoria do livro: "))
                arquivo = open('acervo/acervo.csv', 'a')
                arquivo.write(nomelivro+";"+categorialivro)
                arquivo.close()
                livroreservado.close()
                os.remove(diretorio)
                print("livro devolvido com sucesso!")
                os.system('cls')
                import MenuUsuarioLogado
                MenuUsuarioLogado.MenuPrincipal()

    elif not existe:
        print("você não tem livros reservados na biblioteca, escolha a opção de reservar um livro no menu.")
        time.sleep(1)
        print("retornando ao menu principal, aguarde!")
        time.sleep(3)
        import MenuUsuarioLogado
        MenuUsuarioLogado.MenuPrincipal()


