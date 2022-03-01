import sqlite3
from sqlite3 import Error

menu=input('''Qual opção você deseja realizar?
            [1] Criar tabela.
            [2] Inserir valores.
            [3] Deletar algum valor.
            [4] Atualizar algum valor.
            [5] Consultar.
''')



def ConexaoBanco():
    banco_dados = "SEU BANCO DE DADOS"
    conector = None
    try:
        conector = sqlite3.connect(banco_dados)
    except Error as ex: 
        print(ex)
    return conector  

vcon = ConexaoBanco()   

if menu == '1':


    def criarTabela(conexao, sql):
        try:
            c = conexao.cursor()
            c.execute(sql)
            print('Tabela criada')

        except Error as ex: 
            print(ex)
    
    nome_tabela = input('Qual o nome da tabela a ser criada? ').title().replace(" ", "_")
    nova_tabela = f"""CREATE TABLE {nome_tabela} (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    idade TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL )"""
    
    criarTabela(vcon,nova_tabela)

elif menu == '2':
    def Inserir(conexao, sql):
        try:
            c = conexao.cursor()
            c.execute(sql)
            conexao.commit()
            print('Inserido com sucesso')
        except Error as ex: 
            print(ex)

    
    nome = input('Qual o seu nome? ').title()
    idade = input('Qual sua idade? ')
    email = input('Qual seu email? ') 
         
    
    inserir = f"INSERT INTO pessoas (nome,idade,email)VALUES('{nome}','{idade}','{email}')"       
    Inserir(vcon,inserir)          

                       

elif menu == '3':

    def Deletar(conexao, sql):
        try:
            c = conexao.cursor()
            c.execute(sql)
            conexao.commit()
            
        except Error as ex: 
            print(ex)
        finally:
            print('Deletado com sucesso.') 
            
    deleta_id = input('Qual id você deseja excluir? ')
    deleta_valores = f"DELETE FROM pessoas WHERE id = {deleta_id} " 
    Deletar(vcon,deleta_valores)           

elif menu == '4':

    def Atualizar(conexao, sql):
        try:
            c = conexao.cursor()
            c.execute(sql)
            conexao.commit()
            
        except Error as ex: 
            print(ex)
        finally:
            print('Atualizado com sucesso')

    atualizar_nome = input('Qual nome  você deseja atualizar? ')
    atualizar_id = input('Qual id você deseja atualizar? ')        

    atualizar_valores = f"UPDATE pessoas SET nome = '{atualizar_nome}' WHERE id = {atualizar_id}"  
    Atualizar(vcon,atualizar_valores)


elif menu == '5':
    def Consultar(conexao, sql):
        
        c = conexao.cursor()
        c.execute(sql)
        resultado = c.fetchall()
        return resultado

    selecionar_valores = "SELECT * FROM pessoas"  
    resposta = Consultar(vcon,selecionar_valores)
    for r in resposta:
        print(r)

else:
    print('Somente opções do menu inicial')          
    
vcon.close() 