BANCO_DE_DADOS='transacoes.csv'

def menu():
    print(f'{" ":^5}\033[1m~Despesas de Natália~\033[m')
    print('\033[4mMenu de transações:\033[m')
    print('1. Adicionar transação')
    print('2. Listar transações')
    print('3. Atualizar transação')
    print('4. Deletar transação')
    print('5. Filtrar transações por categoria')
    print('6. Extrato por categoria')
    print('7. Funcionalidade extra')
    print('0. Sair')
    escolha=int(input('Selecione uma opção:'))
    return escolha

def adicionar(transacoes):
    cont=len(transacoes) + 1
    nome=input('Nome da transação:').lower().strip()
    categoria=input('Categoria da transação:').lower().strip()
    valor=float(input('Valor da transação:'))
    transacoes[cont]={"nome": nome, "categoria": categoria, "valor": valor}
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
        del transacoes[cont]
        salvar(transacoes)
        print('Transação deletada!')
    else:
        print('Transação não encontrada.')

def filtrar_categoria(transacoes):
    categoria=input('Digite a categoria:')
    listar(transacoes, categoria)

def extrato(transacoes):
    categoria=input('Digite a categoria:')
    total=0
    print(f'Extrato da categoria: {categoria}:')
    for cont, transacao in transacoes.items():
        if transacao["categoria"]==categoria:
            print(f"{transacao['nome']}: R$ {transacao['valor']}")
            total+=transacao['valor']
    print(f'Total: R${total}')

def salvar(transacoes):
    with open(BANCO_DE_DADOS, 'w', encoding='utf8') as f: #w= escrever o file
        for cont, transacoes in transacoes.items():
            f.write(f"{cont};{transacoes['nome']};{transacoes['categoria']};{transacoes['valor']}\n")

def carregar_transacoes():
    transacoes={}
    try:
        with open(BANCO_DE_DADOS, 'r', encoding='utf8') as f: #r= ler o file
            for line in f:
                cont, nome, categoria, valor=line.strip().split(";")
                transacoes[int(cont)] = {"nome": nome, "categoria": categoria, "valor": float(valor)}
    except FileNotFoundError:
        pass
    return transacoes

transacoes = carregar_transacoes()

while True:
    escolha=menu()
    if escolha==1:
        print('\033[4mCategorias:\033[m')
        print('-Alimentação;\n-Saúde;\n-Lazer;\n-Transporte;\n-Boletos.\n')
        adicionar(transacoes)
    elif escolha==2:
        listar(transacoes)
    elif escolha==3:
        atualizar(transacoes)
    elif escolha==4:
        deletar(transacoes)
    elif escolha==5:
        filtrar_categoria(transacoes)
    elif escolha==6:
        extrato(transacoes)
    elif escolha==0:
        print('Programa encerrado.')
        break
    else:
        print('Opção inválida.')

#falta: total do extrato, saldo, entrada de dinheiro, acento nas categorias e funcionalidade extra.