from libs import *

""""
TODO: {
    
    - Fazer o BackEnd (Thaue, José e Adrian)
    - Fazer o FrontEnd (Lucas, Adrian)
    - Instalar todas as Dependencias
    - Planejar certinho todo o projeto nosso
    
    BACKEND {
    
        Sistema da DataBase:
            - Login/cadastro
            - Registro de Jogos (Nome, Descrição, Imagem, Preço, Tamanho, Categoria, Tipo)
            - Armazenamento de jogos
    }
    
    FRONT-END {
        Registro de Usuario { 
            - Tudo relacionado ao cadastro + Tab switch de registro pra login
        }
        
        O USO DE TAB SWITCH VAI SER NECESSÁRIO PRA FAZER AS TROCAS DE FRAMES TELAS
        
    }
}

"""

# rascunho de login/cadastro 

class registro():
    def __init__(self):

        _nome = input("Digite seu Nome: ") 
        _nome_usuario = input ("digite seu nome de usuario ")  
        _email = input ("digite se Email")
        _data_Nascimento = input ("digite sua data de nascimento ")
        _senha = input ("digite sua senha ")
        _senha_confirm = input("Digite novamente sua senha")


        self.nome= _nome 
        self.nome_usuario = _nome_usuario
        self.email = _email
        self.data_Nascimento = _data_Nascimento
        self.senha=_senha
        self.senha_confirm=_senha_confirm
        


def main():
    pass

