BANCO_DE_DADOS='transacoes.csv'

def menu():
    print(f'{" ":^5}\033[1m~Despesas de Natália~\033[m')
    print('\033[4mMenu de transações:\033[m')
    print('1. Adicionar transação')
    print('2. Atualizar transação')
    print('3. Listar transações')
    print('4. Listar transações por categoria')
    print('5. Extrato por categoria')
    print('6. Funcionalidade extra')
    print('7. Deletar transação')
    print('0. Sair')
    escolha=int(input('Selecione uma opção:'))
    return escolha

def adicionar(transacoes):
    cont=len(transacoes) +1
    nome=input('Nome da transação:').lower().strip()
    categoria=input('Categoria da transação:').lower().strip()
    valor=float(input('Valor da transação:'))
    transacoes[cont]={"nome": nome, "categoria": categoria, "valor":valor}
    salvar(transacoes)
    print('A transação foi adicionada com sucesso!')

def listar(transacoes, categoria=None):
    print('Lista de transações:')
    for cont, transacoes in transacoes.items():
        if not categoria or transacoes['categoria']==categoria:
            print(f"{cont}. {transacoes['nome']} ({transacoes['categoria']}): R$ {transacoes['valor']}")

def atualizar(transacoes):
    cont=int(input('Número da transação:'))
    if cont in transacoes:
        nome=input('Digite o novo nome da transação, caso não deseje alterá-lo, pressione Enter:')
        print('\033[4mCategorias:\033[m')
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
        confirmar=int(input(f'Deseja mesmo deletar a transação{cont}?\n[1]-sim [2]-não\nDigite:'))
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
    print('\033[4mCategoria:\033[m')
    print('-Alimentos;\n-Bem-estar;\n-Lazer;\n-Transporte;\n-Boletos.\n')
    categoria=input('Digite a categoria:')
    total=0
    print(f'Extrato da categoria: {categoria}:')
    for cont, transacao in transacoes.items():
        if transacao["categoria"]==categoria:
            print(f"{transacao['nome']}: R$ {transacao['valor']}")
            total+=transacao['valor']
    print(f'Total: R${total}')

def salvar(transacoes):
    with open(BANCO_DE_DADOS, 'w', encoding='utf8') as f:
        for cont, transacoes in transacoes.items():
            f.write(f"{cont};{transacoes['nome']};{transacoes['categoria']};{transacoes['valor']}\n")

def carregar_transacoes():
    transacoes={}
    try:
        with open(BANCO_DE_DADOS, 'r', encoding='utf8') as f:
            for line in f:
                cont, nome, categoria, valor=line.strip().split(";")
                transacoes[int(cont)]={"nome": nome, "categoria": categoria, "valor": float(valor)}
    except FileNotFoundError:
        pass
    return transacoes

transacoes=carregar_transacoes()

while True:
    escolha=menu()
    if escolha==1:
        print('\033[4mCategorias:\033[m')
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
    elif escolha==7:
        deletar(transacoes)
    elif escolha==0:
        print('Programa encerrado.')
        break
    else:
        print('Opção inválida.')
