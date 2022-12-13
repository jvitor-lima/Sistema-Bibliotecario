import os,time
def deletarLivro():
    print("\033[1;43m\tExcluír Livro...\t\033[m")
    nome_livro = input('\033[1;30mDigite o nome do livro que deseja excluir: \033[m')
    arq2 = open('acervo/acervo.csv', 'r')
    lerlivros = arq2.readlines()
    arrayAux = []  # array vazio para nao interferir no array original por conta do laço FOR
    try:
        for i in lerlivros:
            deixar = True # sempre deixar o que não será alterado no arquivo csv
            i = i.replace('\n', '')
            nomenoarq = i.split(';')
            if nomenoarq[0] == nome_livro:
                time.sleep(1)
                alterar = str(input('\033[1;30mDeseja realmente exlcuir o Livro? \n[1] - Sim \n[2] - Não \nDigite: \033[m'))
                if alterar == "1" or alterar == "sim" or alterar == "s":
                    print("")
                    print("\033[1;42mlivro excluído com sucesso!\033[m")
                    time.sleep(1)
                    print("")
                    deixar = False # ele encontrou e foi confirmado pelo usuario para ser deletado
                elif alterar == "2" or alterar == "nao" or alterar == "não" or alterar == "n":
                    deixar = True
                    print("")
                    print("\033[7;30;41mLivro não excluído!\033[m")
                    time.sleep(1)
                    print("")
                else:
                    print("")
                    print("\033[7;41mTem certeza que digitou corretamente? Por favor, confira e tente novamente!\033[m")
                    print("")

                    return deletarLivro()
            if deixar:              # sempre testará o deixar por conta do IF anterior
                arrayAux.append((';'.join(nomenoarq) + '\n'))  #essa linha será adicionado os que não será exlcuido pelo nome que o usuario digitou


        arq2.close()
        arq = open('acervo/acervo.csv','w') # essa linha vai recriar o arquivo após fecha-ló reabrindo em modo escrita
        arq.writelines(arrayAux) # vai escrever a nova lista sem o dado deletado
        arq.close()
    except (ValueError, TypeError):
        print("erro, por favor digite um nome valido!")
    except:
        print("ERRO! não conseguimos identificar, por favor tente novamente!")
        time.sleep(3)
        deletarLivro()


    finally:
        msg = str(input("você recebeu a mensagem de livro excluido com sucesso?\n[1] - sim \n[2] - não\nDigite:  "))
        if msg.lower() == "sim" or msg == "1":
            print("Livro excluido com sucesso!")
            print("retornando ao menu principal...")
            time.sleep(2)
            import paineladm
            paineladm.menuadm()

        elif msg.lower() == 'não' or msg == '2' or msg.lower() == 'nao':
            print("Livro não excluido ")
            print("verifique o nome do livro que deseja excluir e digite corretamente")
            time.sleep(2)
            print("retornando ao menu...")
            import paineladm
            time.sleep(2)
            paineladm.menuadm()
        else:
            print("opção incorreta, tente novamente!")
            time.sleep(3)
            deletarLivro()


    print("retornando ao menu do administrador...")
    time.sleep(2)
    import paineladm
    paineladm.menuadm()


