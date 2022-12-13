
def cadlivroacervo():
    import os, time
    from datetime import date
    os.system('cls')
    print("CADASTRAR LIVRO NO ACERVO")
    time.sleep(2)
    nomelivro = str(input("\033[1;30mDigite o nome do livro que deseja cadastrar: \033[m"))
    descricaolivro = str(input("\033[1;30mDigite a categoria do livro: \033[m"))
    livros = nomelivro + ";" + descricaolivro
    abrirarquiv = open('acervo/acervo.csv','a')
    abrirarquiv.write('{}\n'.format(livros))
    abrirarquiv.close()
    print("inserindo livro no acervo...")
    time.sleep(2)
    print("livro inserido com sucesso!")
    time.sleep(1)

    Date_required = date.today()
    data = str(Date_required)
    registrologin = nomelivro+";"+data
    arquivoRegistro = open('registrosCadLivros.csv', 'a')
    arquivoRegistro.write(registrologin)
    arquivoRegistro.write("\n")
    arquivoRegistro.close()

    print("retornando ao menu...")
    time.sleep(2)
    import paineladm
    paineladm.menuadm()

