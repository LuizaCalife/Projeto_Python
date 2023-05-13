BANCO_DE_DADOS='transacoes.txt'

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

