from libs import *
from Objects import bancodados

# rascunho de login/cadastro 

usuariosRegistrados = {}
class registro1():
    def __init__(self):
        self.TipoCadastro = None

        def iniciarCadastro():
            self.TipoCadastro = input("Digite 1 para Registrar\nDigite 2 Para fazer Login.")
        
        match self.TipoCadastro:
            case "1":
                Cadastro()
                
            case "2":
                _email = input ("digite se Email")
                _senha = input ("digite sua senha ")
                _senha_confirm = input("Digite novamente sua senha")
                
            case _:
                print("Digite um número válido.")
                iniciarCadastro()

        def Cadastro():
            _nome = input("Digite seu Nome: ") 
            _nome_usuario = input ("digite seu nome de usuario ")  
            _email = input ("digite se Email")
            _data_Nascimento = input ("digite sua data de nascimento ")
            Senha()
            
            self.nome= _nome 
            self.nome_usuario = _nome_usuario
            self.email = _email
            self.data_Nascimento = _data_Nascimento
        
        def Login():
            _email = input ("digite seu Email")
            if input("Digite a senha correta: ") == self.senha:
                print("Você logou")

    
        def Senha():
            self.senha = input("Digite sua senha: ")
            if input("Digite novamente sua senha: ") != self.senha:
                Senha()




# exemplo de login , caso o usuario ja tenha  conta 
        def Login():
            _email = input ("digite seu Email")
            if input("Digite a senha correta: ") == self.senha:
                print("Você logou")
