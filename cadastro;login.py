from tkinter import *
import sqlite3
janela = Tk()
janela["background"] = "gray"

fonte1 = ("arial", "15")
def cadastrando_db():
    global ed1,ed2,msg
    conn = sqlite3.connect("cadastro.db")
    cursor = conn.cursor()
    usuario = ed1.get()
    senha = ed2.get()
    
    cursor.execute("""INSERT INTO cadastro(usuario,senha)VALUES(?,?)""",(usuario,senha))
    conn.commit()
    conn.close()
    msg.destroy()
    msg = Label(janela,text="Cadastrado",font=fonte1)
    msg.grid(row=7,column=0)
def validando():
    global ed1,ed2,msg
    conn = sqlite3.connect("cadastro.db")
    lista = []
    cursor = conn.cursor()
    usuario = ed1.get()
    senha = ed2.get()
    cursor.execute("""SELECT usuario,senha FROM cadastro;""")
    for linha in cursor.fetchall():
        if usuario in linha:
            if senha in linha:
                lista.append(1)
        else:
            lista.append(0)
    if 1 in lista:
        import Calculator_7
    else:
        msg.destroy()
        msg = Label(janela,font=fonte1,text="Conta inválida")
        msg.grid(row=7,column=0)
        
        
    
        
        
    
    
def criar_login(): 
    
    global lb,lb1,lb2,ed1,ed2,bt1,bt2,lb3
    
    lb1 = Label(janela,text="LOGIN",font=("arial","20"), background="gray")
    lb2 = Label(janela,text="Usuário:",font=fonte1 ,background="gray")
    lb3 = Label(janela,text="Senha:",font=fonte1 ,background="gray")

    ed1 = Entry(janela,width=10,font=fonte1)
    ed2 = Entry(janela,width=10,font=fonte1,show='*')

    bt1 = Button(janela,text="Acessar",font=fonte1,background="blue",command=validando)
    bt2 = Button(janela,text="Cadastrar",font=fonte1,background="blue",command=cadastrar)

    lb1.grid(row=1,column=1)
    lb2.grid(row=2,column=0)
    lb3.grid(row=6,column=0)
    ed1.grid(row=2,column=1)
    ed2.grid(row=6,column=1)
    bt1.place(x=100,y=150)
    bt2.place(x=92,y=200)

def criar_cadastro():
    
    global lb,lb1,lb2,lb3,ed1,ed2,bt1,bt2,msg
    
    lb1 = Label(janela,text="CADASTRO",font=("arial","20"),background="gray")
    lb2 = Label(janela,text="Usuário",font = fonte1, background="gray")
    lb3 = Label(janela,text="Senha",font = fonte1, background="gray")
    
    ed1= Entry(janela,font=fonte1)
    ed2= Entry(janela,font=fonte1,show="*")

    bt1= Button(janela,text="Cadastrar",font=fonte1,width=10,bg="blue",command=cadastrando_db)
    bt2= Button(janela,text="Voltar",font=fonte1,width=10,command=voltar, bg="blue")
    msg = Label(janela,text="Aguardando..",font=fonte1)
    
    lb1.grid(row=1,column=0)
    lb2.grid(row=3,column=0)
    lb3.grid(row=4,column=0)
    ed1.grid(row=3,column=1)
    ed2.grid(row=4,column=1)
    bt1.grid(row=6,column=1)
    bt2.grid(row=6,column=0)
    msg.grid(row=7,column=0)

def criar_menu():
    global lbEscolha,lb,lb1,lb2,lb3,ed1,ed2,bt1,bt2
    lb1 = Label(janela,text='CALCULATOR', font=("arial","20"), bg="gray")
    lbEscolha = Label(janela,text='Menu das calculadoras', font=fonte1, bg="gray")
    lb2 = Label(janela,text='CALCULATOR',font=("Times","15"),background="gray")
    lb3 = Label(janela,text='CALCULATOR-7',font=("Times","15"),background="gray")
    bt1 = Button(janela,text='Acessar',font=fonte1,command=abrir_calculator, background="blue")
    bt2 = Button(janela,text='Acessar',font=fonte1,command=login, background="blue")

    lb1.place(x=50,y=10)
    lbEscolha.place(x=45,y=50)
    lb2.place(x=5,y=100)
    lb3.place(x=150,y=100)
    bt1.place(x=25,y=130, width="100", height="30")
    bt2.place(x=170,y=130, width="100", height="30")

def abrir_calculator():
    global lb,lb1,lb2,lb3,ed1,ed2,bt1,bt2
    janela.destroy()
    import Calculadora

def abrir_calculator7():
    global lb,lb1,lb2,lb3,ed1,ed2,bt1,bt2
    janela.destroy()
    import Calculator_7


def destruir_cadastro():
    global lb,lb1,lb2,lb3,ed1,ed2,bt1,bt2,lbEscolha
    lb1.destroy()
    lb2.destroy()
    lb3.destroy()
    ed1.destroy()
    ed2.destroy()
    bt1.destroy()
    bt2.destroy()
    lbEscolha.destroy()

def destruir_login():
    global lb,lb1,lb2,lb3,ed1,ed2,bt1,bt2,lbEscolha
    lb1.destroy()
    lb2.destroy()
    lb3.destroy()
    ed1.destroy()
    ed2.destroy()
    bt1.destroy()
    bt2.destroy()
    lbEscolha.destroy()

def destruir_menu():
    global lb,lb1,lb2,lb3,ed1,ed2,bt1,bt2,lbEscolha
    lb1.destroy()
    lb2.destroy()
    lb3.destroy()
    bt1.destroy()
    bt2.destroy()
    lbEscolha.destroy()

def menu():
    global lb,lb1,lb2,lb3,ed1,ed2,bt1,bt2,lbEscolha
    criar_menu()

def voltar():
    global lb,lb1,lb2,lb3,ed1,ed2,bt1,bt2,lbEscolha
    destruir_cadastro()
    criar_login()

def cadastrar():
    global lb,lb1,lb2,lb3,ed1,ed2,bt1,bt2,lbEscolha
    destruir_login()
    criar_cadastro()


def login():
    global lb,lb1,lb2,lb3,ed1,ed2,bt1,bt2,lbEscolha
    destruir_menu()
    criar_login()


menu()
janela.geometry("315x270")   
janela.resizable(False,False)
janela.title("CALCULATOR")
janela.mainloop()
