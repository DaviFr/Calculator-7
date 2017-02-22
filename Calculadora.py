from tkinter import *

def click():
    if(str(ed1.get()).isnumeric() and str(ed2.get()).isnumeric()): 
        num1 = int(ed1.get())
        num2 = int(ed2.get())
        lb['text'] = num1+num2
    else:
        lb['text'] = "Valores informados inválidos."
def click1():
    if(str(ed1.get()).isnumeric() and str(ed2.get()).isnumeric()):
        num1 = int(ed1.get())
        num2 = int(ed2.get())
        lb['text'] = num1-num2
    else:
        lb['text'] = "Valores informados inválidos."

def click2():
    if(str(ed1.get()).isnumeric() and str(ed2.get()).isnumeric()):
        num1 = int(ed1.get())
        num2 = int(ed2.get())
        lb['text'] = num1/num2
    else:
        lb['text'] = "Valores informados inválidos."
  

def click3():
    if(str(ed1.get()).isnumeric() and str(ed2.get()).isnumeric()):
        num1 = int(ed1.get())
        num2 = int(ed2.get())
        lb['text'] = num1*num2
    else:
        lb['text'] = "Valores informados inválidos."

calc = Tk()
calc.title("Calculadora")

ed1 = Entry(calc)
ed1.place(x=180, y=100)

ed2 = Entry(calc)
ed2.place(x=180, y=130)

lb1 = Label(calc, text="Bem-vindo a tabuada virtual")
lb1.place(x=165,y=40)

lb2 = Label(calc, text="Digite dois numeros e escolha a operação.")
lb2.place(x=140,y=60)

lb3 = Label(calc, text=">>> Numero 1")
lb3.place(x=50,y=100)

lb4 = Label(calc, text=">>> Numero 2")
lb4.place(x=50,y=130)

lb5 = Label(calc, text=">>> Resultado : ")
lb5.place(x=50,y=230)

but = Button(calc, text="Soma", width=15,command=click)
but.place(x=5,y=170)

but1 = Button(calc, text="Subtração", width=15,command=click1)
but1.place(x=123,y=170)

but2 = Button(calc, text="Divisão", width=15,command=click2)
but2.place(x=241,y=170)

but3 = Button(calc, text="Multiplicação", width=15,command=click3)
but3.place(x=360,y=170)

lb = Label(calc, text="")
lb.place(x=140,y=230)

calc.geometry("480x280+300+300")
calc.mainloop()
