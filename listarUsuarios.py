def listarUsers():
    import time,os
    os.system('cls')
    try:
        arq = open('usuarioscadastrados.csv','r')
    except:
        print('\033[1;41mERRO!\033[7;30;41m Não foi possível abrir o arquivo!\033[m')
    else:
        print("USUARIOS CADASTRADOS:")
        for linha in arq:

            dado = linha.split(';')
            print(dado[0])
        input("digite enter para continuar:  ")
        time.sleep(1)
        import paineladm
        paineladm.menuadm()


