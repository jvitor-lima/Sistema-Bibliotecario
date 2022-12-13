def RegistroUsers ():
    import os,time
    print("")
    print("DATA PADRÃO AMERICANO \033[1;107m(EXEMPLO 	\033[1;35m2022-09-20\033[0;0m\033[1;107m)\033[0;0m ")
    try:
        desejasair = str(input("Digite a data que deseja filtrar os usuarios registrados. \nDigite: "))
        arquivo = open('registrosusuarios.csv', encoding='utf-8')
        lerlogs = arquivo.readlines()
        cont = 0
        for i in lerlogs:
            i = i.replace('\n', ';')
            nomedolog = i.split(';')
            arquivoaux = nomedolog[1]
            arquivoaux2 = nomedolog[0]
            if arquivoaux == desejasair:
                print("Usuario: ",arquivoaux2)
                cont += 1
                time.sleep(1)
            else:
                cont = cont
        print("foram criados nessa data {} usuarios".format(cont))
    except(TypeError,ValueError):
        print("erro, por favor verifique o modelo de data americano e tente novamente!")

    finally:
        print("")
        input("digite enter para voltar ao menu")
        print("retornando ao menu...")
        import paineladm
        paineladm.menuadm()


