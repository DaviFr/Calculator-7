usuario = str(input("digite o nome do user: "))
senha = input("digite sua senha: ")
lista_user = ["andre","lucas","bale"]
lista_senha = ["ifall","ufall","balle"]

    
def cadastro_user(usuario):
    while len(usuario) < 5:
        if len(usuario) >= 5:
            lista_user.append(usuario)
        else:
            print("Digite um nome com no minimo 5 letras")
            usuario = str(input("digite o nome do user: "))
    
    lista_user.append(usuario)
    print("usuario salvo")

def cadastro_pass(senha):

    while len(senha) < 5:
        if len(senha) >= 5:
            lista_senha.append(senha)
        else:
            print("Digite a senha no minino com 5 digitos")
            senha = input("digite sua senha: ")
    lista_senha.append(senha)

def login():
    usuario = str(input("digite o nome do user: "))
    senha = input("digite sua senha: ")

    codi_user = 1
    codi_senha = 2
    
    if usuario not in lista_user:
        codi_user = 0
        print("usuario invalido!")
    if senha not in lista_senha:
        codi_senha = 1
        print("senha invalida!")
    a = 0
    if codi_user == 1 and codi_senha == 2: 
        while a < len(lista_user):
            if usuario == lista_user[a]:
                if senha == lista_senha[a]:
                    print("usuario e senhas corretas!")
                else:
                    print("senha invalida")
            a+=1
        
cadastro_user(usuario)
cadastro_pass(senha)
#print(lista_user)
#print(lista_senha)
login()
