dic = {}
def adicionar(c,v): #lili:  c = categoria e v = valor 
    dic[c] = []
    dic[c].append(v)
    return dic

def listar():
    
def atualizar():

def deletar(c,v): # lili: c = categoria e v = valor
    dic[c]= []
    dic[c].remove(v)
    return dic

def filtrar_categoria():

def extrato_categoria(c,v):# lili: c=categoria e v= valor
    dic[c] = []
    dic[c] = adicionar(sum(v)) # lili: natalia escolhe o dicionário/ categoria, que deseja retirar o extrato e aparece a soma do valor geral para ela.
    return dic

def funcionalidade_extra():

 #lili: precisa inicializar essa lista né??
despesa =['alimentação', 'saúde', 'lazer', 'transporte', 'boletos']

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
        valor = float(input('Digite o valor gasto:'))
        print(adicionar(despesa,valor))
    elif escolha=='2':
        listar()
    elif escolha=='3':
        atualizar()
    elif escolha=='4':
        valor = float(input('Digite o valor gasto:'))
        print(deletar(despesa,valor))
    elif escolha=='5':
        filtrar_categoria()
    elif escolha=='6':
        print(dic)
        print(extrato_categoria(despesa,valor)) # lili: eu fiquei em duvida se ao passar o loop ele continua armazenando no dic
    elif escolha=='7':
        funcionalidade_extra()
    elif escolha=='0':
        break
    else:
        print('Opção inválida.')
        