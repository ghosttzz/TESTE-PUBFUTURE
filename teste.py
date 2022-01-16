receita = []
n_receita = 1
despesa = []
n_despesas = 1
conta = []
n_contas = 1
corrente = []
poupança = []
carteira = []
salário = []
presente = []
premio = []
alimentação = []
lazer = []
moradia = []
outros1 = []
outros2 = []



def contas():
        print('Você deseja: '
              '\n [1] Menu Contas;'
              '\n [2] Listar Contas;'
              '\n [3] Listar total;'
              '\n [4] Voltar;'
              )
        d = int(input('Que opção você deseja?'))
        if (d == 1):
            menucontas()
        if (d == 2):
            print('Em que tipo de conta vizualizar?')
            print('[1] Poupança')
            print('[2] Corrente')
            print('[3] Carteira')
            print('[4] Outros')
            pcc = int(input('Digite a opção escolhida:'))
            if (pcc == 1):
                print(poupança)
                return contas()
            if (pcc ==2):
                print(corrente)
                return contas()
            if (pcc ==3):
                print(carteira)
                return contas()
            if (pcc ==4):
                print(outros1)
                return contas()
        if (d == 3):
            print(conta)
            return (contas())
        if (d == 4):
            menu()
def menucontas():
    print('Você quer:')
    print('[1] Cadastrar Contas')
    print('[2] Editar Contas')
    print('[3] Transferir Saldo entre contas;')
    print('[4] Voltar')
    d2 = int(input('Digite a opção escolhida:'))
    if (d2 == 1):
        criarcontas()
    if (d2 == 2):
        print('lala')
    if (d2 == 3):
        print('la')
    if (d2 == 4):
        contas()
def criarcontas():
            for i in range(n_contas):
                contas_valor = float(input('Escreva saldo dessa conta: '))
                print('Em que tipo de conta queres cadastar?')
                print('[1] Poupança')
                print('[2] Corrente')
                print('[3] Carteira')
                print('[4] Outros')
                contas_tipo = input('Digite o tipo da conta: ')
                contas_int = input('Instituição')
                contas_total = (
                'Saldo: ', contas_valor, 'Tipo da conta: ', contas_tipo, 'Intituição financeira: ', contas_int)
                conta.append(contas_total)
                if(contas_tipo==1):
                    conta.append(contas_total)
                    print('\n Cadastro Feito')
                if(contas_tipo==2):
                    corrente.append(contas_total)
                    print(' \n Cadastro feito!')
                if(contas_tipo==3):
                    carteira.append(contas_total)
                    print(' \n Cadastro feito!')
                if (contas_tipo==4):
                    outros2.append(contas_total)
                    print(' \n Cadastro feito!')
                def menueditar2():
                    print('Você quer editar o que?')
                    print(' [1] Valor')
                    print(' [2] Tipo')
                    print(' [3] Data que deve Pagar')
                    print('[4] Sair')
                    edi = int(input('Escolha a opção'))
                    if (edi == 1):
                        editarreceitas1()
                    if (edi == 2):
                        editarreceitas2()
                    if (edi == 3):
                        editarreceitas3()
                    if (edi == 4):
                       terminal()
                def editarreceitas1():
                    print(conta)
                    nr = int(input('Digite o número da conta que deseja editar: '))
                    nn = input('Digite o novo valorda receita: ')
                    contas_valor = nn
                    contas_total = (
                        'Valor: ', contas_valor, 'Tipo da conta: ', contas_tipo, 'Intituição financeira: ', contas_int)
                    conta.pop(nr)
                    conta.append(contas_total)
                    print(conta)
                    return menueditar2()
                def editarreceitas2():
                    print(conta)
                    nr = int(input('Digite o número da conta que deseja editar: '))
                    nn = input('Digite a novo tipo da conta: ')
                    contas_tipo = nn
                    contas_total = ( 'Valor: ', contas_valor, 'Tipo da conta: ', contas_tipo, 'Intituição financeira: ', contas_int)
                    conta.pop(nr)
                    conta.append(contas_total)
                    print(conta)
                    return menueditar2()
                def editarreceitas3():
                    print(conta)
                    nr = int(input('Digite o número da conta que deseja editar: '))
                    nn = int(input('Digite a nova instituição financeira da conta: '))
                    contas_cont = nn
                    contas_total = ('Valor: ', contas_valor, 'Tipo da conta: ', contas_tipo, 'Intituição financeira: ', contas_int)
                    conta.pop(nr)
                    conta.append(contas_total)
                    print(conta)
                    return menueditar2()
                def terminal():
                    print('[1] - Cadastrar novamente')
                    print('[2] - Excluir as Despesas')
                    print('[3] - Editar Receitas')
                    print('[4] Sair')
                    n1 = 0
                    n1 = int(input('Digite a opção escolhida:'))
                    if (n1 == 1):
                        criardespesas()
                    if (n1 == 2):
                        excluirdespesas()
                    if (n1 == 3):
                        menueditar2()
                    if (n1 == 4):
                        menucontas()
                def excluirdespesas():
                    print('Escolha a melhor opção:')
                    print('[1] - Excluir todas as contas: ')
                    print('[2] - Exluir uma especifica; ')
                    print('[3] - Sair')
                    contab = 0
                    e = int(input('Escolha a opção:'))
                    if (e == 1):
                        despesa.clear()
                    if (e == 2):
                        print(f'As contas são: {despesa} ')
                        nd = int(input('Digite o número da despesa que deseja excluir, começando em 0: '))
                        despesa.pop(nd)
                        print(despesa)
                        print('Exclusão completa')
                        return cadastrardespesas()
                    if (e == 3):
                        terminal()
            return terminal()
def menudespesas():
                print('Você deseja: '   
                            '\n [1] Menu Despesas;'
                            '\n [2] Voltar;'
                      )
                d = int(input('Que opção você deseja?'))
                if (d == 1):
                    cadastrardespesas()
                if (d == 2):
                    menu()
def cadastrardespesas():
        print('Você quer:')
        print('[1] Cadastrar Despesas')
        print('[2] Voltar')
        d2 = int(input('Digite a opção escolhida:'))
        if (d2 == 1):
            criardespesas()
        if (d2 == 2):
           menudespesas()
def criardespesas():
            for i in range(n_despesas):
                despesa_nam = input('Escreva o nome da despesa: ')
                print('[1] Alimentação')
                print('[2] Lazer')
                print('[3] Moradia')
                print('[4] Outros')
                despesa_tip = int(input('Escreva o valor do tipo de despesa:'))
                despesa_cont = int(input('Escreva a opção da conta bancaria: '))
                despesa_valor = float(input('Escreva o valor a depositar dessa despesa: '))
                despesa_datap = int(input('Data que deve pagar '))
                despesa_datape = int(input('Data que pagou: '))
                despesa_dados = ('Nome:', despesa_nam, 'Tipo de Despesa:', despesa_tip, 'Conta Bancaria:',
                                 despesa_cont, 'Valor da despesa:R$', despesa_valor, 'Data de pagamento esperado:',
                                 despesa_datap, 'Data de pagamento:', despesa_datape)
                despesa.append(despesa_dados)
                if(despesa_tip == 1):
                    alimentação.append(despesa_dados)
                    print(' \n Cadastro feito!')
                if(despesa_tip == 2):
                    lazer.append(despesa_dados)
                    print(' \n Cadastro feito!')
                if(despesa_tip ==3):
                    moradia.append(despesa_dados)
                    print(' \n Cadastro feito!')
                if(despesa_tip ==4):
                    outros1.append(despesa_dados)
                def menueditar2():
                        print('VocÊ quer editar o que?')
                        print(' [1] Nome')
                        print(' [2] Tipo')
                        print(' [3] Conta')
                        print(' [4] Valor')
                        print(' [5] Data de Pagamento')
                        print(' [6] Data de recebimento')
                        print('[7] Sair')
                        edi = int(input('Escolha a opção'))
                        if (edi == 1):
                            editarreceitas1()
                        if (edi == 2):
                            editarreceitas2()
                        if (edi == 3):
                            editarreceitas3()
                        if(edi==4):
                            editarreceitas4()
                        if(edi ==5):
                            editarreceitas5()
                        if(edi ==6):
                            editarreceitas6()
                        if(edi ==7):
                            terminal1()
                def editarreceitas1():
                            print(despesa)
                            nr = int(input('Digite o número da receita que deseja editar: '))
                            nn = input('Digite o novo nome da receita: ')
                            despesa_nam = nn
                            despesa_dados = (
                                'Nome:', despesa_nam, 'Tipo de Receita: ', despesa_tip,
                                'Conta Bancaria:',
                                despesa_cont, 'Valor da receita:R$', despesa_valor, 'Data de pagamento esperado:',
                                despesa_datap, 'Data de pagamento:', despesa_datape)
                            despesa.pop(nr)
                            despesa.append(despesa_dados)
                            print(despesa)
                            return menueditar2()
                def editarreceitas2():
                        print(despesa)
                        nr = int(input('Digite o número da receita que deseja editar: '))
                        nn = input('Digite a novo tipo da receita: ')
                        despesa_tip = nn
                        despesa_dados = (
                            'Nome:', despesa_nam,  'Tipo de Receita: ', despesa_tip,
                            'Conta Bancaria:',
                            despesa_cont, 'Valor da receita:R$', despesa_valor, 'Data de pagamento esperado:',
                            despesa_datap, 'Data de pagamento:', despesa_datape)
                        despesa.pop(nr)
                        despesa.append(despesa_dados)
                        print(despesa)
                        return menueditar2()
                def editarreceitas3():
                        print(despesa)
                        nr = int(input('Digite o número da receita que deseja editar: '))
                        nn = int(input('Digite a nova conta da receita: '))
                        despesa_cont = nn
                        despesa_dados = (
                            'Nome:', despesa_nam, 'Tipo de Receita: ', despesa_tip,
                            'Conta Bancaria:',
                            despesa_cont, 'Valor da receita:R$', despesa_valor, 'Data de pagamento esperado:',
                            despesa_datap, 'Data de pagamento:', despesa_datape)
                        despesa.pop(nr)
                        despesa.append(despesa_dados)
                        print(despesa)
                        return menueditar2()
                def editarreceitas4():
                        print(despesa)
                        nr = int(input('Digite o número da receita que deseja editar: '))
                        nn = float(input('Digite o novo valor da receita: '))
                        despesa_valor = nn
                        despesa_dados = (
                            'Nome:', despesa_nam, 'Descrição da receita: ','Tipo de Receita: ', despesa_tip,
                            'Conta Bancaria:',
                            despesa_cont, 'Valor da receita:R$', despesa_valor, 'Data de pagamento esperado:',
                            despesa_datap, 'Data de pagamento:', despesa_datape)
                        despesa.pop(nr)
                        despesa.append(despesa_dados)
                        print(receita)
                        return menueditar2()
                def editarreceitas5():
                        print(despesa)
                        nr = int(input('Digite o número da receita que deseja editar: '))
                        nn = float(input('Digite o novo valor da receita: '))
                        despesa_datap = nn
                        despesa_dados = (
                            'Nome:', despesa_nam, 'Descrição da receita: ','Tipo de Receita: ', despesa_tip,
                            'Conta Bancaria:',
                            despesa_cont, 'Valor da receita:R$', despesa_valor, 'Data de pagamento esperado:',
                            despesa_datap, 'Data de pagamento:', despesa_datape)
                        despesa.pop(nr)
                        despesa.append(despesa_dados)
                        print(despesa)
                        return menueditar2()
                def editarreceitas6():
                        print(despesa)
                        nr = int(input('Digite o número da receita que deseja editar: '))
                        nn = float(input('Digite o novo valor da receita: '))
                        despesa_datape = nn
                        despesa_dados = (
                            'Nome:', despesa_nam, 'Descrição da receita: ','Tipo de Receita: ', despesa_tip,
                            'Conta Bancaria:',
                            despesa_cont, 'Valor da receita:R$', despesa_valor, 'Data de pagamento esperado:',
                            despesa_datap, 'Data de pagamento:', despesa_datape)
                        despesa.pop(nr)
                        despesa.append(despesa_dados)
                        print(despesa)
                        return menueditar2()
                def terminal1():
                        print('[1] - Cadastrar novamente')
                        print('[2] - Excluir as Despesas')
                        print('[3] - Editar Receitas')
                        print('[4] Listar depesa')
                        print('[5] Sair')
                        n1 = 0
                        n1 = int(input('Digite a opção escolhida:'))
                        if (n1 == 1):
                            criardespesas()
                        if (n1 == 2):
                                excluirdespesas()
                        if (n1 == 3):
                                menueditar2()
                        if(n1 ==4):
                            listardespesa()
                        if(n1 ==5):
                                menudespesas()
                def excluirdespesas():
                            print('Escolha a melhor opção:')
                            print('[1] - Excluir todas as contas: ')
                            print('[2] - Exluir uma especifica; ')
                            print('[3] - Sair')
                            contab = 0
                            e = int(input('Escolha a opção:'))
                            if (e == 1):
                                despesa.clear()
                            if (e == 2):
                                print(f'As contas são: {despesa} ')
                                nd = int(input('Digite o número da despesa que deseja excluir, começando em 0: '))
                                despesa.pop(nd)
                                print(despesa)
                                print('Exclusão completa')
                                return cadastrardespesas()
                            if (e == 3):
                                terminal1()
                def listardespesa():
                            print('Você deseja: '
                                  '\n [1] Listar Despesas;'
                                  '\n [2] Listar Despesas por tipo'
                                  '\n [3] Listar Despesas por data de recebimento;'
                                  '\n [4] Voltar;'
                                  )
                            ld = int(input('Insira o número da opção desejada:'))
                            if (ld == 1):
                                print(despesa)
                                return listardespesa()
                            if (ld == 2):
                                print('Escolha o tipo.:')
                                print('[1] Alimentação')
                                print('[2] Lazer')
                                print('[3] Moradia')
                                print('[4] Outros')
                                pcc = int(input('Digite a opção esoclhida: '))
                                if (pcc == 1):
                                    print(alimentação)
                                    return listardespesa()
                                if (pcc ==2):
                                    print(moradia)
                                    return listardespesa()
                                if(pcc==3):
                                    print(lazer)
                                    return listardespesa()
                                if(pcc ==4):
                                    print(outros1)
                                    return listardespesa()
                return terminal1()

def  menureceitas():
                print('Você deseja: '
                      '\n''[1] - Menu das receitas;'
                      '\n [2] - Listar receitas'
                      '\n [3] - Voltar')
                r =int((input('Que opção você deseja?')))
                if (r == 1):
                    cadastrarreceitas()
                if(r == 2):
                    listarreceitas()
                if(r ==3):
                    menu()

def cadastrarreceitas():
            print('Você quer:')
            print('[1] Cadastrar Receitas')
            print('[2] Voltar')
            r2 = int(input('Digite a opção escolhida:'))
            if (r2 == 1):
                criarreceitas()
            if (r2 == 2):
                menureceitas()

def criarreceitas():
            for i in range(n_receita):
                receita_name = input('Escreva o nome da receita: ')
                receita_desa = input('Escreva a descrição da receita: ')
                print('[1] Salário')
                print('[2] Presentes')
                print('[3] Prémio')
                print('[4] Outros')
                receita_tip = int(input('Escreva a opção do tipo da receita:'))
                receita_cont = int(input('Escreva o tipo da conta bancaria: '))
                receita_valor = float(input('Escreva o valor recebido dessa receita: '))
                receita_datap = int(input('Data que deve pagar '))
                receita_datape = int(input('Data que pagou: '))
                receita_dados = (
                'Nome:', receita_name, 'Descrição da receita: ', receita_desa, 'Tipo de Receita: ', receita_tip,
                'Conta Bancaria:',
                receita_cont, 'Valor da receita:R$', receita_valor, 'Data de pagamento esperado:',
                receita_datap, 'Data de pagamento:', receita_datape)
                receita.append(receita_dados)
                if (receita_tip == 1):
                    salário.append(receita_dados)
                    print(receita)
                    print(' \n Cadastro feito!')
                if (receita_tip == 2):
                    receita_dados = (
                    'Nome:', receita_name, 'Descrição da receita: ', receita_desa, 'Tipo de Receita: ', receita_tip,
                    'Conta Bancaria:',
                    receita_cont, 'Valor da receita:R$', receita_valor, 'Data de pagamento esperado:',
                    receita_datap, 'Data de pagamento:', receita_datape)
                    receita.append(receita_dados)
                    presente.append(receita_dados)
                    print(' \n Cadastro feito!')
                if (receita_tip == 3):
                    receita_dados = (
                    'Nome:', receita_name, 'Descrição da receita: ', receita_desa, 'Tipo de Receita: ', receita_tip,
                    'Conta Bancaria:',
                    receita_cont, 'Valor da receita:R$', receita_valor, 'Data de pagamento esperado:',
                    receita_datap, 'Data de pagamento:', receita_datape)
                    receita.append(receita_dados)
                    premio.append(receita_dados)
                    print(' \n Cadastro feito!')
                if (receita_tip ==4):
                    receita_dados = (
                        'Nome:', receita_name, 'Descrição da receita: ', receita_desa, 'Tipo de Receita: ', receita_tip,
                        'Conta Bancaria:',
                        receita_cont, 'Valor da receita:R$', receita_valor, 'Data de pagamento esperado:',
                        receita_datap, 'Data de pagamento:', receita_datape)
                    receita.append(receita_dados)
                    outros1.append(receita_dados)
                    print(' \n Cadastro feito!')
                def excluirreceitas():
                            print('Escolha a melhor opção:')
                            print('[1] - Excluir todas as receitas:  ')
                            print('[2] - Exluir uma especifica; ')
                            print('[3] - Sair')
                            contab = 0
                            e = int(input('Escolha a opção:'))
                            if (e == 1):
                                receita.clear()
                            if (e == 2):
                                print(f'As receitas são: {receita} ')
                                nd = int(input('Digite o número da receita que deseja excluir, começando em 0: '))
                                receita.pop(nd)
                                print(receita)
                                print('Exclusão completa')
                                return excluirreceitas()
                            if (e == 3):
                                terminal2()
                def menueditar():
                    print('VocÊ quer editar o que?')
                    print(' [1] Nome')
                    print(' [2] Descrição')
                    print(' [3] Tipo')
                    print(' [4] Conta')
                    print(' [5] Valor')
                    print(' [6] Data de Pagamento')
                    print(' [7] Data de recebimento')
                    print('[8] Sair')
                    edi = int(input('Escolha a opção'))
                    if (edi == 1):
                        editarreceitas1()
                    if (edi == 2):
                        editarreceitas2()
                    if (edi == 3):
                        editarreceitas3()
                    if(edi==4):
                        editarreceitas4()
                    if(edi ==5):
                        editarreceitas5()
                    if(edi ==6):
                        editarreceitas6()
                    if(edi ==7):
                        editarreceitas7()
                def editarreceitas1():
                        print(receita)
                        nr = int(input('Digite o número da receita que deseja editar: '))
                        nn = input('Digite o novo nome da receita: ')
                        receita_name = nn
                        receita_dados = (
                            'Nome:', receita_name, 'Descrição da receita: ',receita_desa, 'Tipo de Receita: ', receita_tip,
                            'Conta Bancaria:',
                            receita_cont, 'Valor da receita:R$', receita_valor, 'Data de pagamento esperado:',
                            receita_datap, 'Data de pagamento:', receita_datape)
                        receita.pop(nr)
                        receita.append(receita_dados)
                        print(receita)
                        return menueditar()
                def editarreceitas2():
                        print(receita)
                        nr = int(input('Digite o número da receita que deseja editar: '))
                        nn = input('Digite a nova descrição da receita: ')
                        receita_desa = nn
                        receita_dados = (
                            'Nome:', receita_name, 'Descrição da receita: ', receita_desa, 'Tipo de Receita: ', receita_tip,
                            'Conta Bancaria:',
                            receita_cont, 'Valor da receita:R$', receita_valor, 'Data de pagamento esperado:',
                            receita_datap, 'Data de pagamento:', receita_datape)
                        receita.pop(nr)
                        receita.append(receita_dados)
                        print(receita)
                        return menueditar()
                def editarreceitas3():
                    print(receita)
                    nr = int(input('Digite o número da receita que deseja editar: '))
                    nn = input('Digite a novo tipo da receita: ')
                    receita_tip = nn
                    receita_dados = (
                        'Nome:', receita_name, 'Descrição da receita: ', receita_desa, 'Tipo de Receita: ', receita_tip,
                        'Conta Bancaria:',
                        receita_cont, 'Valor da receita:R$', receita_valor, 'Data de pagamento esperado:',
                        receita_datap, 'Data de pagamento:', receita_datape)
                    receita.pop(nr)
                    receita.append(receita_dados)
                    print(receita)
                    return menueditar()
                def editarreceitas4():
                    print(receita)
                    nr = int(input('Digite o número da receita que deseja editar: '))
                    nn = int(input('Digite a nova conta da receita: '))
                    receita_cont = nn
                    receita_dados = (
                        'Nome:', receita_name, 'Descrição da receita: ', receita_desa, 'Tipo de Receita: ', receita_tip,
                        'Conta Bancaria:',
                        receita_cont, 'Valor da receita:R$', receita_valor, 'Data de pagamento esperado:',
                        receita_datap, 'Data de pagamento:', receita_datape)
                    receita.pop(nr)
                    receita.append(receita_dados)
                    print(receita)
                    return menueditar()
                def editarreceitas5():
                    print(receita)
                    nr = int(input('Digite o número da receita que deseja editar: '))
                    nn = float(input('Digite o novo valor da receita: '))
                    receita_valor = nn
                    receita_dados = (
                        'Nome:', receita_name, 'Descrição da receita: ', receita_desa, 'Tipo de Receita: ', receita_tip,
                        'Conta Bancaria:',
                        receita_cont, 'Valor da receita:R$', receita_valor, 'Data de pagamento esperado:',
                        receita_datap, 'Data de pagamento:', receita_datape)
                    receita.pop(nr)
                    receita.append(receita_dados)
                    print(receita)
                    return menueditar()
                def editarreceitas6():
                    print(receita)
                    nr = int(input('Digite o número da receita que deseja editar: '))
                    nn = input('Digite a nova data de pagamento da receita: ')
                    receita_datap = nn
                    receita_dados = (
                        'Nome:', receita_name, 'Descrição da receita: ', receita_desa, 'Tipo de Receita: ', receita_tip,
                        'Conta Bancaria:',
                        receita_cont, 'Valor da receita:R$', receita_valor, 'Data de pagamento esperado:',
                        receita_datap, 'Data de pagamento:', receita_datape)
                    receita.pop(nr)
                    receita.append(receita_dados)
                    print(receita)
                    return menueditar()
                def editarreceitas7():
                    print(receita)
                    nr = int(input('Digite o número da receita que deseja editar: '))
                    nn = input('Digite a nova data de recebimento da receita: ')
                    receita_datape = nn
                    receita_dados = (
                        'Nome:', receita_name, 'Descrição da receita: ', receita_desa, 'Tipo de Receita: ', receita_tip,
                        'Conta Bancaria:',
                        receita_cont, 'Valor da receita:R$', receita_valor, 'Data de pagamento esperado:',
                        receita_datap, 'Data de pagamento:', receita_datape)
                    receita.pop(nr)
                    receita.append(receita_dados)
                    print(receita)
                    return menueditar()
            def terminal2():
                            print('[1] - Cadastrar novamente')
                            print('[2] - Excluir as Receitas')
                            print('[3] - Editar Receitas')
                            print('[4] - Sair')
                            n1 = 0
                            n1 = int(input('Digite a opção escolhida:'))
                            if (n1 == 1):
                                criarreceitas()
                            if (n1 == 2):
                                excluirreceitas()
                            if (n1 == 3):
                                menueditar()
                            if (n1 == 4):
                                menureceitas()
            return terminal2()
def listarreceitas():
    print('Escolha a opção:')
    print('[1] Listar total de receitas')
    print('[2] Listar receitas por tipo')
    print('[3] Voltar' )
    pp = int(input('Digite a opção escolhida: '))
    if (pp == 1):
        print(receita)
    if (pp == 2):
        print('Em que tipo de conta queres cadastar?')
        print('[1] Salário')
        print('[2] Presentes')
        print('[3] Prémio')
        print('[4] Outros')
        pcc = int(input('Digite a opção desejada: '))
        if (pcc == 1):
            print(salário)
            return menureceitas()
        if (pcc == 2):
            print(premio)
            return menureceitas()
        if (pcc == 3):
            print(presente)
            return menureceitas()
        if (pcc == 4):
            print(outros2)
            return menureceitas()
    if (pp == 3):
        print(receita)
def menu():
    n=0
    while (n == 0):
            print('Digite o número referente a opção abaixo! ')
            print('[1] - Receitas')
            print('[2] - Despesas')
            print('[3] - Contas')
            print('[4] - Sair')
            n = int(input('Digite a opção escolhida:'))
    if (n == 1):
            menureceitas()
    if ( n ==2):
            menudespesas()
    if ( n ==3):
            contas()
    if (n == 4):
            print('Fim da consulta!')
            import sys

            sys.exit()
n = 0
while(n == 0) :
        print('Digite o número referente a opção abaixo! ')
        print('[1] - Receitas')
        print('[2] - Despesas')
        print('[3] - Contas')
        print('[4] - Sair')
        n=int(input('Digite a opção escolhida:'))
if (n == 1):
        menureceitas()
if(n==2):
        menudespesas()
if ( n == 3):
    contas()
if (n == 4):
        print('Fim da consulta!')
        import sys
        sys.exit()





