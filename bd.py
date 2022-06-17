import sqlite3

# criar banco de dados

con = sqlite3.connect('dados.db')

cur = con.cursor()

# Criar Tabela 

cur.execute("create table if not exists agenda (id integer primary key autoincrement, nome text  not null, telefone text not null, dataregistro DATETIME DEFAULT(datetime('now','localtime')))")

con.commit()

# inserir dados 

def inserir (tipo,nome,telefone):
    if tipo == 1 and nome != "" and telefone != "":
    
        cur.execute("insert into agenda(nome,telefone) values ('{}','{}')".format(str(nome),str(telefone)))
        con.commit()




# Ver dados 

# CODIGO 0 nome 1 telefone 2

contatos = []

def consultar(tipo):
    if tipo == 1 :
        for linha in cur.execute("select * from agenda"):
            #print(linha)
            #print('Nome =' ,linha[1])
            contatos.append((f'{linha[0]}', f'{linha[1]}', f'{linha[2]}'))

    return contatos



            
# generate sample data
''''contatos = []
for n in range(1, 100):
    contatos.append((f'first {n}', f'last {n}', f'email{n}@example.com'))
'''


#inserir(True,'Guilherme B','2299885544')
#consultar(True)



