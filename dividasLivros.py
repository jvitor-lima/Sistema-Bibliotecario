import time,os
def dividasLivros():
    os.system('cls')
    #verificar usuarios que estão com dividas
    path = r"C:\Sistema_Bibliotecario\usuariosdividas"
    path2 = r"C:\Sistema_Bibliotecario\acervo"

    os.chdir(path)
    print("Os usuarios que estão com pagamentos pendentes: ")
    time.sleep(2)
    def read_text_file(file_path):
        with open(file_path, 'r') as f:
            print('USUARIO;VALOR')
            print(f.read())
            print("")

    for file in os.listdir():
        if file.endswith(".csv"):
            file_path = f"{path}\{file}"
            read_text_file(file_path)


    if not os.listdir():
        print("não foi encontrado usuarios com dividas!")
        time.sleep(2)
        print("retornando ao menu do administrador...")
        time.sleep(3)
        import  paineladm
        paineladm.menuadm()
    else:
        try:
            pgnome = str(input("digite o nome do usuario que deseja receber o pagamento:  "))
            file_diretorio = f"{path}\{pgnome}"
            file_diretorio2 = f"{path2}\{pgnome}"
            acervo_diretorio = f"{path2}\{'acervo.csv'}"
            abrirarquivo = open(file_diretorio+'PagamentoLivro.csv','r')
            lerarquivo = abrirarquivo.read()
            mysplit = lerarquivo.split(';')
            print('Usuario: ',mysplit[0],'com a divida de: ',mysplit[1])
            diretorio = 'acervo/'+pgnome+'_livroreservado.csv'
            existe = os.path.exists(diretorio)
            nomedouser = open(file_diretorio2+'_livroreservado.csv', 'r')
            lerlivro = nomedouser.readlines()
            nomelivro = lerlivro[0]
            print("nome do livro -->  ",nomelivro)
            desejaapagar = str(input("você tem certeza que esse usuario ja pagou e deseja devolver o livro ao acervo? \n[1] - Sim\n[2] - Não\nDigite: "))

            if (desejaapagar == "1") or (desejaapagar == "um"):
                #Inserindo o nome do livro e a categoria de volta no Acervo geral
                categorialivro = str(input("digite o nome da categoria do livro: "))
                #apagando os registros de dividas do usuario e livro reservado antigo
                diretorio = file_diretorio2+'_livroreservado.csv'
                existe = os.path.exists(diretorio)
                segdiretorio = file_diretorio+'PagamentoLivro.csv'
                segundoexiste = os.path.exists(segdiretorio)
                if existe and segundoexiste:
                    print("removendo livro reservado do usuario...")
                    time.sleep(3)
                    print("removendo divida do usuario...")
                    time.sleep(3)
                    print("devolvendo livro ao acervo")
                    arquivo = open(acervo_diretorio, 'a')
                    nomedolivro = nomelivro
                    nomestring = str(nomedolivro)
                    nomecompletolivro = ("{};{}".format(nomestring, categorialivro))
                    nomeall = nomecompletolivro.replace('\n', '')
                    arquivo.write(nomeall)
                    arquivo.write('\n')
                    arquivo.close()
                    nomedouser.close()
                    abrirarquivo.close()
                    os.remove(diretorio)
                    os.remove(segdiretorio)
                elif not existe:
                    print("divida não encontranda")
                    time.sleep(1)
                    print("retornando ao menu principal...")
                    time.sleep(3)
                    import paineladm
                    paineladm.menuadm()

                print("retornando ao menu principal...")
                time.sleep(3)
                import paineladm
                paineladm.menuadm()

            elif (desejaapagar == "2") or (desejaapagar == "não"):
                print("2- Retornando ao menu principal...")
                time.sleep(3)
                import paineladm
                paineladm.menuadm()

            else:
                print("opção incorreta, por favor digite a opção corretamente!")
                time.sleep(2)
                print("retornando ao menu...")
                time.sleep(3)
                import paineladm
                paineladm.menuadm()
        except(FileNotFoundError):
            print("ESSE USUARIO NÃO EXISTE")
            time.sleep(1)
            print("retornando para o menu")
            import paineladm
            paineladm.menuadm()

