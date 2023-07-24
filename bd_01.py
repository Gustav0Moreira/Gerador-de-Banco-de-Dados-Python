import sqlite3


def ler():
    ler = open('bd', 'r')  
    for linha in ler:
        li = linha
    return li

def conv(nome):
    li = list(nome.split('-'))
    return li

def resultado(nome):
    con = sqlite3.connect(nome)
    cur = con.cursor()
    nome = nome
    control = None
    op = None
    while control != 1:
        op = int(input('Escolha a opção que deseja: \n1-Consultar uma chave específica. \n2-Consultar todas as chaves. \nDigite: '))
        if op == 1:
            print('Digite a chave que gostaria de consultar')
            key = input('Chave: ')
            res = cur.execute("SELECT %s FROM %s" % (key , nome))
            linha = res.fetchall()
            control = 1
        elif op == 2:
            res = cur.execute("SELECT * FROM %s" % nome)
            linha = res.fetchall()
            control = 1
        else:
            print('Valor inválido')
    return linha

def gravar(nome , chave):
    con = sqlite3.connect(nome)
    cur = con.cursor()
    key_q = int(chave)
    print('Seu banco possui a quantidade de: %d chaves' %key_q)
    print('Escolha os valores para gravar em suas chaves')
    if key_q == 2:
        key = [(input('Chave 1: ')), (input('Chave 2: '))]
        sql = ('INSERT INTO %s VALUES("%s", "%s")' %(nome, key[0], key[1]))
        cur.execute(sql)
        con.commit()
    elif key_q == 3:
        key = [(input('Chave 1: ')), (input('Chave 2: ')), (input('Chave 3: '))]
        sql = ('INSERT INTO %s VALUES("%s", "%s", "%s")' %(nome, key[0], key[1], key[2]))
        cur.execute(sql)
        con.commit()
    elif key_q == 4:
        key = [(input('Chave 1: ')), (input('Chave 2: ')), (input('Chave 3: ')),(input('Chave 4: ')) ]
        sql = ('INSERT INTO %s VALUES("%s", "%s", "%s", "%s")' %(nome, key[0], key[1], key[2], key[3]))
        cur.execute(sql)
        con.commit()
    elif key_q == 5:
        key = [(input('Chave 1: ')), (input('Chave 2: ')), (input('Chave 3: ')),(input('Chave 4: ')),(input('Chave 5: ')) ]
        sql = ('INSERT INTO %s VALUES("%s", "%s", "%s", "%s", "%s")' %(nome, key[0], key[1], key[2], key[3], key[4]))
        cur.execute(sql)
        con.commit()
    elif key_q == 6:
        key = [(input('Chave 1: ')), (input('Chave 2: ')), (input('Chave 3: ')),(input('Chave 4: ')),(input('Chave 5: ')), (input('Chave 6: '))  ]
        sql = ('INSERT INTO %s VALUES("%s", "%s", "%s", "%s", "%s", "%s")' %(nome, key[0], key[1], key[2], key[3], key[4], key[5]))
        cur.execute(sql)
        con.commit()
    print('Valores gravados com sucesso!')
        
        
    
    


def criar():
    print('Você escolheu a criação de um novo banco')

    control = None
    control_2 = None
    control_3 = None


    while control_3 != 1:
        control = None
        while control != 's':
            nome = input('\nDigite o nome do banco: ').upper()
            control = input('O nome escolhido para o banco foi %s. Você está certe deste nome? (s/n):' % nome)

        ler = open('bd', 'r')
        
        for linha in ler:
            li = linha
            
        txt = li

        key_quant = None
        
        if nome in txt:
            print('Banco de dados com o mesmo nome já criado')
        else:
            control_3 = 1
            
    con = sqlite3.connect('%s' % nome)
    cur = con.cursor()
    print('\nEscolha a quantidade de chaves para seu banco: ')
    
    while control_2 != 1:
        key = int(input('2 Chaves \n3 Chaves \n4 Chaves \n5 Chaves \n6 Chaves: \n'))
        if key == 2:
            print('Digite o nome das chaves')
            row = [(input('Nome 1:')),(input('Nome 2:'))]
            sql = ('CREATE TABLE %s(%s text, %s text)' %(nome, row[0], row[1]))
            cur.execute(sql)
            con.commit()
            key_quant = '2'
            print('BD criado com sucesso!')
            control_2 = 1
        elif key == 3:
            print('Digite o nome das chaves')
            row = [(input('Nome 1:')),(input('Nome 2:')),(input('Nome 3:'))]
            sql = ('CREATE TABLE %s(%s text, %s text, %s text)' %(nome, row[0], row[1], row[2]))
            cur.execute(sql)
            con.commit()
            key_quant = '3'
            print('BD criado com sucesso!')
            control_2 = 1
        elif key == 4:
            print('Digite o nome das chaves')
            row = [(input('Nome 1:')),(input('Nome 2:')),(input('Nome 3:')),(input('Nome 4:'))]
            sql = ('CREATE TABLE %s(%s text, %s text, %s text, %s text)' %(nome, row[0], row[1], row[2], row[3]))
            cur.execute(sql)
            con.commit()
            key_quant = '4'
            print('BD criado com sucesso!')
            control_2 = 1
        elif key == 5:
            print('Digite o nome das chaves')
            row = [(input('Nome 1:')),(input('Nome 2:')),(input('Nome 3:')),(input('Nome 4:')), (input('Nome 5:'))]
            sql = ('CREATE TABLE %s(%s text, %s text, %s text, %s text, %s text)' %(nome, row[0], row[1], row[2], row[3], row[4]))
            cur.execute(sql)
            con.commit()
            key_quant = '5'
            print('BD criado com sucesso!')
            control_2 = 1
        elif key == 6:
            print('Digite o nome das chaves')
            row = [(input('Nome 1:')),(input('Nome 2:')),(input('Nome 3:')),(input('Nome 4:')), (input('Nome 5:')), (input('Nome 6:'))]
            sql = ('CREATE TABLE %s(%s text, %s text, %s text, %s text, %s text, %s text)' %(nome, row[0], row[1], row[2], row[3], row[4], row[5]))
            cur.execute(sql)
            con.commit()
            key_quant = '6'
            print('BD criado com sucesso!')
            control_2 = 1
        else:
            print('Valor inválido, escolha novamente')
                
    arquivo = open('bd', 'a')
    arquivo.write('-%s%s-' % (nome , key_quant))
    arquivo.close
    print('Banco de Dados: %s' % nome)






control = None


while control != 4:

    print('\n1 - Criar BD \n2 - Gravar em BD já existente \n3 - Consultar BD \n4 - Desligar')
    control = int(input('Digite uma das opções acima: '))


    if control == 1:
       criar()
       lista_bd = ler()
       lista_bd_re = conv(lista_bd)
       print(lista_bd_re)
       
        
        
    elif control == 2:
        lista_bd = ler()
        lista_bd_re = conv(lista_bd)
        
        print(lista_bd_re)
        print('OBS: O nome do banco deve ser utilizado sem o número no final.')
        print('OBS: O número no final do nome representa a quantidade de chaves no banco.')
        
        print('Por gentileza, informe os dados de seu banco')
        nome = input('Nome do banco:').upper()
        quant = int(input('Quantas chaves o banco possui: '))
        bd_nome = str('%s%d' %(nome, quant))
        
        if bd_nome in lista_bd_re:
            print('Banco localizado com sucesso!')
            gravar(nome, quant)
            
        else:
            print('Banco não localizado. Retornando ao menu.')
            


    
    elif control == 3:
        lista_bd = ler()
        lista_bd_re = conv(lista_bd)
        print(lista_bd_re)
        print('OBS: O nome do banco deve ser utilizado sem o número no final.')
        print('OBS: O número no final do nome representa a quantidade de chaves no banco.')
        
        print('Por gentileza, informe os dados de seu banco')
        nome = input('Nome do banco:').upper()
        quant = int(input('Quantas chaves o banco possui: '))
        bd_nome = str('%s%d' %(nome, quant))

        if bd_nome in lista_bd_re:
            print('Banco localizado com sucesso!')
            re = resultado(nome)
            print(re)
             
        else:
            print('Banco não localizado. Retornando ao menu.')

    
    else:
        print('Valor inválido, escolha novamente')
