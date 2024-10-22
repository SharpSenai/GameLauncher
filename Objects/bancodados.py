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
    
    def salvarBanco(self):
        if self.Connex:
            self.Connex.commit()
            print("Banco de dados Salvo.")

    def inserirBanco(self, valores):
        query = f"INSERT INTO PerfilUsuario ()"
        
    def criarTabelas(self):
        
        self.Cursor.execute("""CREATE TABLE IF NOT EXISTS PerfilUsuario(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            senha TEXT NOT NULL
            )""")
        
        print("Tabela Criada.")
        
banco = BancoDeDados()
        
    
        
        
    