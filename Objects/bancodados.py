from libs import *

class BancoDeDados:
    
    def __init__(self):
        self.iniciarBanco()
        print("Iniciado")
    
    def iniciarBanco(self):
        try:
            self.Connex = Lib_SQLite3.connect("sistemaBD.db")
            self.Cursor = self.Connex.cursor()
            self.criarTabelas()
        except Lib_SQLite3.Error as err:
            print(err)
    
    def desconectarBanco(self):
        if self.Connex:
            self.Connex.close()
            print("Banco de dados desconectado.")
        
    def criarTabelas(self):
        self.Cursor.execute("CREATE TABLE PerfilUsuario(nome, email, senha)")
        self.desconectarBanco()
        print("Tabela Criada.")
        
banco = BancoDeDados()
        
    
        
        
    