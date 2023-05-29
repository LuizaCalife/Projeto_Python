BANCO_DE_DADOS = 'transacoes.csv'

def menu():
    print('\n')
    print(f'\033[4mDespesas de Natália\033[m')
    print(f'\033[1;36mMenu de transações:\033[m')
    print('\033[1;36m1.\033[m Adicionar transação')
    print('\033[1;36m2.\033[m Atualizar transação')
    print('\033[1;36m3.\033[m Listar transações')
    print('\033[1;36m4.\033[m Listar transações por categoria')
    print('\033[1;36m5.\033[m Extrato')
    print('\033[1;36m6.\033[m Meta financeira mensal')
    print('\033[1;36m7.\033[m Deletar transação')
    print('\033[1;36m0.\033[m Sair')
    escolha = int(input('Selecione uma opção:'))
    print('\n')
    return escolha


def adicionar(transacoes):
    cont=len(transacoes) +1
    nome=input('Nome da transação:').lower().strip()
    categoria=input('Categoria da transação:').lower().strip()
    valor=float(input('Valor da transação:'))
    transacoes[cont]={"nome": nome, "categoria": categoria, "valor": valor}
    salvar(transacoes)
    print('A transação foi adicionada com sucesso!')


def listar(transacoes, categoria=None):
    print('\033[1mLista de transações:\033[m')
    for cont, transacoes in transacoes.items():
        if not categoria or transacoes['categoria']==categoria:
            print(f"{cont}. {transacoes['nome']} ({transacoes['categoria']}): R${transacoes['valor']}")


def atualizar(transacoes):
    cont=int(input('Número da transação:'))
    if cont in transacoes:
        nome=input('Digite o novo nome da transação, caso não deseje alterá-lo, pressione Enter:')
        print('\033[4mCategorias disponíveis:\033[m')
        print('-Alimentos;\n-Bem-estar;\n-Lazer;\n-Transporte;\n-Boletos.\n')
        categoria=input('Digite o nova categoria da transação, caso não deseje alterá-la, pressione Enter:')
        valor=input('Digite o novo valor da transação, caso não deseje alterá-lo, pressione Enter:')
        if nome:
            transacoes[cont]["nome"]=nome
        if categoria:
            transacoes[cont]["categoria"]=categoria
        if valor:
            transacoes[cont]["valor"]=float(valor)
        salvar(transacoes)
        print('A transação foi atualizada!')
    else:
        print('Transação não encontrada.')


def deletar(transacoes):
    cont=int(input('Digite o número da transação para deletá-la:'))
    if cont in transacoes:
        confirmar=int(input(f'Deseja mesmo deletar a transação {cont}?\n[\033[33m1\033[m]-sim \n[\033[33m2\033[m]-não\nDigite:'))
        if confirmar==1:
            del transacoes[cont]
            salvar(transacoes)
            print('Transação deletada!')
        elif confirmar==2:
            print('Você será redirecionado ao menu!')
            menu()
    else:
        print('Transação não encontrada.')


def filtrar_categoria(transacoes):
    categoria=input('Digite a categoria:')
    listar(transacoes, categoria)


def extrato(transacoes):
    total_por_categoria=0
    print('\033[1mTipos de extrato:\033[m')
    tipo_do_extrato=int(input('[\033[33m1\033[m]-Extrato por categoria \n[\033[33m2\033[m]-Extrato geral\nDigite o número:'))
    if tipo_do_extrato==1:
        print('\033[4mCategoria:\033[m')
        print('-Alimentos;\n-Bem-estar;\n-Lazer;\n-Transporte;\n-Boletos.\n')
        categoria=input('Digite a categoria:')
        print(f'Extrato da categoria: {categoria}:')
        for cont, transacao in transacoes.items():
            if transacao["categoria"]==categoria:
                print(f"{transacao['nome']}: R${transacao['valor']}")
                total_por_categoria+=transacao['valor']
        print(f'Total:R${total_por_categoria}')
    elif tipo_do_extrato==2:
        total=0
        for transacao in transacoes.values():
            total+=transacao['valor']
        print(f'Total de todas as transações: R${total:.2f}')


def salvar(transacoes):
    with open(BANCO_DE_DADOS, 'w', encoding='utf8') as f:
        for cont, transacoes in transacoes.items():
            f.write(f"{cont};{transacoes['nome']};{transacoes['categoria']};{transacoes['valor']}\n")


def carregar_transacoes():
    transacoes={}
    try:
        with open(BANCO_DE_DADOS, 'r', encoding='utf8') as f:
            for line in f:
                cont, nome, categoria, valor = line.strip().split(";")
                transacoes[int(cont)]={"nome": nome, "categoria": categoria, "valor": float(valor)}
    except FileNotFoundError:
        pass
    return transacoes


transacoes=carregar_transacoes()


def meta_financeira_mensal(transacoes):
    total=0

    saldo=float(input('Digite seu saldo: '))
    meta_financeira_mensal=float(input('Digite sua meta para esse mês: '))
    print()

    for transacao in transacoes.values():
        total+=transacao['valor']
        print(f'Total de todas as transações: R${total:.2f}')

    if meta_financeira_mensal>total:
        restante=meta_financeira_mensal-total
        print(f'Você possui R${restante} referente a sua meta mensal.')
        print(f'Faltam R$ {meta_financeira_mensal-restante} para você atingir a sua meta mensal.')

    elif meta_financeira_mensal<total:
        resto=saldo-meta_financeira_mensal
        print('Você ultrapassou a meta desse mês.')
        print(f'Porém, você tem R${resto}, como saldo final.')

    else:
        print('Você atingiu sua meta mensal')
        
while True:
    escolha=menu()
    if escolha==1:
        print('\033[1m Categorias disponíveis:\033[m')
        print('-Alimentos;\n-Bem-estar;\n-Lazer;\n-Transporte;\n-Boletos.\n')
        adicionar(transacoes)
    elif escolha==2:
        atualizar(transacoes)
    elif escolha==3:
        listar(transacoes)
    elif escolha==4:
        filtrar_categoria(transacoes)
    elif escolha==5:
        extrato(transacoes)
    elif escolha==6:
        meta_financeira_mensal(transacoes)
    elif escolha==7:
        deletar(transacoes)
    elif escolha==0:
        print('Programa encerrado.')
        break
    else:
        print('Opção inválida.')
