import os,time
def editarLogin():
    os.system('cls')
    print("\033[1;43m\tAlterando login...\t\033[m")
    nome_usuario = input('\033[1;30mDigite seu nome de usuário:\033[m')
    time.sleep(1)
    arq2 = open('usuarioscadastrados.csv', 'r')
    lerusers = arq2.readlines()
    arrayAux = [] # array vazio para nao interferir no array original por conta do laço FOR
    for i in lerusers:
        i = i.replace('\n', '')
        nomedoarq = i.split(';')
        if nomedoarq[0] == nome_usuario:
            #print(i)
            alterar = str(input("\033[1;30mVocê deseja alterar seu nome ou sua senha? \n[1] - Nome \n[2] - Senha\nDigite:\033[m"))
            if alterar == "1":
                aux = str(input("\033[1;30mDigite seu novo nome de usuário:\033[m"))
                nomedoarq[0] = aux
                print("nome alterado com sucesso!")
                time.sleep(1)
                print("retornando ao menu principal...")
                time.sleep(3)
                import MenuUsuarioLogado
                MenuUsuarioLogado.MenuPrincipal()
            elif alterar == "2":
                aux = str(input("\033[1;30mDigite sua nova senha:\033[m"))
                nomedoarq[1] = aux
                print("senha alterada com sucesso!")
                time.sleep(1)
                print("retornando ao menu principal...")
                time.sleep(3)
                import MenuUsuarioLogado
                MenuUsuarioLogado.MenuPrincipal()
            else:
                print("\n")
                print("\033[1;41mERRO!\033[7;30;41m Por favor, digite uma opção existente!\033[m")
                print("\n")
                return editarLogin()

        arrayAux.append((';'.join(nomedoarq) + '\n'))# join = Juntar
        #print(';'.join(nomedoarq) + '\n')
    arq2.close()
    arq = open('usuarioscadastrados.csv','w')
    arq.writelines(arrayAux)
    arq.close()



