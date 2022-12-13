
#AINDA EM FASE DE TESTES, NÃO ALTERAR DADOS
def reservar():
    from datetime import date, timedelta
    import os, time
    os.system('cls')
    abrirnome = open('usuariologadotemporario.csv')
    nomecache = abrirnome.readlines()
    nomedousuario = str(nomecache)[2:-2]
    print("\t\t\tRESERVA DE LIVROS")
    nome_livro = str(input('\033[1;30mDigite o nome do livro que deseja reservar: \033[m'))
    time.sleep(1)
    arq2 = open('acervo/acervo.csv','r')
    lerusers = arq2.readlines()
    arrayAux = []  # array vazio para nao interferir no array original por conta do laço FOR
    try:
        for i in lerusers:
            deixar = True # sempre deixar o que não será alterado no arquivo csv
            i = i.replace('\n', '')
            nomedoarq = i.split(';')
            #VERIFICA SE O NOME DO LIVRO EXISTE NO BANCO E SE EXISTIR FAZ A CONFIRMAÇÃO DE RESERVA
            if nomedoarq[0] == nome_livro:
                alterar = str(input('\033[1;30mDeseja realmente reservar o livro? \n[1] - Sim \n[2] - Não \nDigite: \033[m'))
                time.sleep(1)
                if alterar == "1" or alterar == "sim" or alterar == "s":
                    diretorio = 'acervo/'+nomedousuario+'_livroreservado.csv'
                    existe = os.path.exists(diretorio)
                    if existe:
                        print("\033[1;41mVocê já possui livros reservados!                                     \033[m")
                        time.sleep(1)
                        print("\033[1;41mSó é possível pegar um livro por vez! Confira se tem livros pendentes!\033[m")
                        deixar = False
                        return
                    elif not existe:
                        Date_required = date.today()  # pegando data atual
                        data = str(Date_required)
                        criarlivroreservado = open('acervo/'+nomedousuario+'_livroreservado.csv','w')
                        criarlivroreservado.write(nome_livro)
                        criarlivroreservado.write('\n')
                        criarlivroreservado.write(data) # escrevendo data atual na linha 2
                        datalivrovencimento =  date.today()+ timedelta(days=5)
                        criarlivroreservado.write('\n')
                        data2 = str(datalivrovencimento)
                        criarlivroreservado.write(data2)
                        time.sleep(1)
                        print("\033[1;43mLivro reservado com sucesso!\033[m")
                        time.sleep(1)
                        print("\033[1;41mVocê tem até 5 dias para devolver o livro ou será multado.\033[m")
                        time.sleep(1)
                        print("\033[7;41mA data do vencimento é \033[m",data2)
                        time.sleep(4)
                        criarlivroreservado.close()
                        deixar = False

                elif alterar == "2" or alterar == "nao" or alterar == "não" or alterar == "n":
                    deixar = True
                    time.sleep(1)
                    print("\033[1;41mO livro não foi reservado :( Você retornará ao menu principal...\033[m")
                    time.sleep(3)

                else:
                    print("\033[7;41mTem certeza que digitou corretamente? Por favor, verifique e tente novamente!\033[m")
                    time.sleep(3)
                    return reservar()
            if deixar:  # sempre testará o deixar por conta do IF anterior
                arrayAux.append((';'.join(
                    nomedoarq) + '\n'))  # essa linha será adicionado os que não será exlcuido pelo nome que o usuario digitou

        arq2.close()
        arq = open('acervo/acervo.csv','w')  # essa linha vai recriar o arquivo após fecha-ló reabrindo em modo escrita
        arq.writelines(arrayAux)  # vai escrever a nova lista sem o dado deletado
        arq.close()
    except (ValueError, TypeError):
        print("ERRO! não conseguimos identificar, por favor tente novamente!")

    finally:
        msg = str(input("você recebeu a mensagem de livro reservado com sucesso?\n[1] - sim \n[2] - não\nDigite:  "))
        if msg.lower() == "sim" or msg == "1":
            print("você poderá ver seus livros reservados na opção [3] do menu!")
            time.sleep(2)
            print("retornando ao menu principal...")
            import MenuUsuarioLogado
            time.sleep(5)
            MenuUsuarioLogado.MenuPrincipal()

        elif msg.lower() == 'não' or msg == '2' or msg.lower() =='nao':
            time.sleep(2)
            print("retornando ao menu...")
            import MenuUsuarioLogado
            time.sleep(2)
            MenuUsuarioLogado.MenuPrincipal()

        else:
            print("opção incorreta, tente novamente!")
            time.sleep(4)
            reservar()




