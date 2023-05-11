#def adicionar():
#def listar():
#def atualizar():
#def deletar():
#def filtrar_categoria():
#def extrato_categoria():
#def funcionalidade_extra():

# dicionario={'key':'value'}
despesas=['alimentação', 'saúde', 'lazer', 'transporte', 'boletos']

while True:
    print('~Despesas de Natália~')
    print('Menu de transações:')
    print('1. Adicionar transação')
    print('2. Listar transações')
    print('3. Atualizar transação')
    print('4. Deletar transação')
    print('5. Filtrar transações por categoria')
    print('6. Extrato por categoria')
    print('7. Funcionalidade extra')
    print('0. Sair')
    escolha=input('Selecione uma opção:')

    if escolha=='1':
        adicionar()
    elif escolha=='2':
        listar()
    elif escolha=='3':
        atualizar()
    elif escolha=='4':
        deletar()
    elif escolha=='5':
        filtrar_categoria()
    elif escolha=='6':
        extrato_categoria()
    elif escolha=='7':
        funcionalidade_extra()
    elif escolha=='0':
        break
    else:
        print('Opção inválida.')
        