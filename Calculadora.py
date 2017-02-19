from tkinter import *
from tkinter import messagebox

class CalculadoraComum(object):
	def __init__(self):
		self.Janela = Tk()
		self.Janela.title("Calculator")
		self.Janela.resizable(False,False)
		self.Janela.geometry("500x500")
		self.Janela['bg'] = "black"
		self.Janela['cursor'] = "cross"
		self.DentroDaJanela = Label(self.Janela, text="Calculadora", font= "arial, 15", background='red') 
		self.DentroDaJanela.place( x= 210, y= 20)

                #Entrada(1,2) sao os campos brancos onde serao digitado os numeros
		self.Entrada1 = []
		self.Entrada2 = []

                #Focador1 é a borda vermelha que fica em torno da entrada(1,2)
		self.Focador1 = Label(self.Janela, width = 35, height= 2, bg = 'red')
		self.Focador1.place(x= 108, y= 67)

		self.AmostrarEntrada1 = Label(self.Janela, text= ''.join(self.Entrada1), font="Arial, 16", width= 20)
		self.AmostrarEntrada1.place(x= 110, y= 70)

		self.Focador2 = Label(self.Janela, width = 35, height= 2, bg = 'black')
		self.Focador2.place(x= 108, y= 107)

		self.AmostrarEntrada2 = Label(self.Janela, text= ''.join(self.Entrada2), font="Arial, 16", width= 20)
		self.AmostrarEntrada2.place(x= 110, y= 110)

		self.Resultado = Label(self.Janela, text= "Resultado", font= "Arial, 16", bg = "grey", fg= "red",  width= 20)
		self.Resultado.place(x= 110, y= 150)

		self.SimboloFoiClicado = False
		self.SinalUsado = None

		self.funcoes = [self.soma, self.subtracao, self.multiplicacao, self.divisao]
		self.Numeros = [self.Numero0, self.Numero1, self.Numero2, self.Numero3, self.Numero4, self.Numero5, self.Numero6, self.Numero7, self.Numero8, self.Numero9]

		ButaoDeletar = Button(self.Janela, text= "⌫", font= "Arial, 16", bg= "blue", activebackground= "dark blue", fg= "white", activeforeground= "grey", width= 3, borderwidth= '3', cursor= "dotbox", justify= LEFT, height= 2, command= self.Deletar).place(x= 360, y= 70)
		x, y= 110, 190

		for Caractere in [ 7, 8, 9, "C", "AC", 4, 5, 6, "+", "×", 1, 2, 3, "-", "÷", 0, ".", '=', "↑", "↓"]:
			OperacoesFundamentais = ["+","-","×","÷"]
			for Posicao in range(len(OperacoesFundamentais)):
				if Caractere == OperacoesFundamentais[Posicao]:
					Comando = self.funcoes[Posicao]
			for Posicao2 in range(10):
				if Caractere == Posicao2:
					Comando = self.Numeros[Posicao2]
			if Caractere == ".":
				Comando = self.PontoFinal
			elif Caractere == "AC":
				Comando = self.FuncaoAC
			elif Caractere == "C":
				Comando = self.FuncaoC
			elif Caractere == "=":
				Comando = self.SinalIgual
			elif Caractere == "↓":
				Comando = self.EscolhaDeLabelDeBaixo
			elif Caractere == "↑":
				Comando = self.EscolhaDeLabelDeCima
			Butoes = Button(self.Janela, width = 3, text = Caractere, borderwidth= '3', cursor= "dotbox", justify= LEFT, activebackground= 'dark blue', fg= "white", activeforeground= 'grey', font="Arial, 16", command = Comando)
			Butoes.place(x= x, y= y)
			Butoes['bg']= 'blue'
			x += 60
			if x== 410:
				x= 110
				y += 50
		self.CodidosDoTeclado = ["plus", "minus", "asterisk", "slash", "equal", "Return", "BackSpace", "Delete", "Left", "period", "Up", "Down", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
		self.FuncoesParaCodidosDoTeclado = [self.soma, self.subtracao, self.multiplicacao, self.divisao, self.SinalIgual, self.SinalIgual, self.Deletar, self.FuncaoC, self.FuncaoAC, self.PontoFinal, self.EscolhaDeLabelDeCima, self.EscolhaDeLabelDeBaixo, self.Numero0, self.Numero1, self.Numero2, self.Numero3, self.Numero4, self.Numero5, self.Numero6, self.Numero7, self.Numero8, self.Numero9]
		for CodigoDaTecla in self.CodidosDoTeclado:
			CodigoDaTecla
			self.Janela.bind_all("<KeyPress-"+CodigoDaTecla+">", self.AcaoVindaDoTeclado)
			self.Janela.bind_all("<KeyPress-Escape>", self.Sair)
		self.Janela.mainloop()

	def soma(self):
		global SimboloFoiClicado, SinalUsado
		Label(self.Janela, text= "+", bg= "black", fg= 'red', font= 'arial, 16').place(x= 80, y= 110)
		self.SimboloFoiClicado = True
		self.SinalUsado = "+"
		self.Focador1['bg'] = 'black'
		self.Focador2['bg'] = 'red'

	def subtracao(self):
		global SimboloFoiClicado, SinalUsado
		Label(self.Janela, text= "-", bg= "black", fg= 'red', font= 'arial, 20').place(x= 80, y= 102)
		self.SimboloFoiClicado = True
		self.SinalUsado = "-"
		self.Focador1['bg'] = 'black'
		self.Focador2['bg'] = 'red'

	def multiplicacao(self):
		global SimboloFoiClicado, SinalUsado
		Label(self.Janela, text= "×", bg= "black", fg= 'red', font= 'arial, 16').place(x= 80, y= 110)
		self.SimboloFoiClicado = True
		self.SinalUsado = "×"
		self.Focador1['bg'] = 'black'
		self.Focador2['bg'] = 'red'

	def divisao(self):
		global SimboloFoiClicado, SinalUsado
		Label(self.Janela, text= "÷", bg= "black", fg= 'red', font= 'arial, 16').place(x= 80, y= 110)
		self.SimboloFoiClicado = True
		self.SinalUsado = "÷"
		self.Focador1['bg'] = 'black'
		self.Focador2['bg'] = 'red'

	def Numero9(self):
		global SimboloFoiClicado
		if self.SimboloFoiClicado:
			self.Entrada2.append("9")
			self.AmostrarEntrada2['text'] = ''.join(self.Entrada2)
		else:
			self.Entrada1.append("9")
			self.AmostrarEntrada1['text'] = ''.join(self.Entrada1)

	def Numero8(self):
		global SimboloFoiClicado
		if self.SimboloFoiClicado:
			self.Entrada2.append("8")
			self.AmostrarEntrada2['text'] = ''.join(self.Entrada2)
		else:
			self.Entrada1.append("8")
			self.AmostrarEntrada1['text'] = ''.join(self.Entrada1)

	def Numero7(self):
		global SimboloFoiClicado
		if self.SimboloFoiClicado:
			self.Entrada2.append("7")
			self.AmostrarEntrada2['text'] = ''.join(self.Entrada2)
		else:
			self.Entrada1.append("7")
			self.AmostrarEntrada1['text'] = ''.join(self.Entrada1)

	def Numero6(self):
		global SimboloFoiClicado
		if self.SimboloFoiClicado:
			self.Entrada2.append("6")
			self.AmostrarEntrada2['text'] = ''.join(self.Entrada2)
		else:
			self.Entrada1.append("6")
			self.AmostrarEntrada1['text'] = ''.join(self.Entrada1)

	def Numero5(self):
		global SimboloFoiClicado
		if self.SimboloFoiClicado:
			self.Entrada2.append("5")
			self.AmostrarEntrada2['text'] = ''.join(self.Entrada2)
		else:
			self.Entrada1.append("5")
			self.AmostrarEntrada1['text'] = ''.join(self.Entrada1)

	def Numero4(self):
		global SimboloFoiClicado
		if self.SimboloFoiClicado:
			self.Entrada2.append("4")
			self.AmostrarEntrada2['text'] = ''.join(self.Entrada2)
		else:
			self.Entrada1.append("4")
			self.AmostrarEntrada1['text'] = ''.join(self.Entrada1)

	def Numero3(self):
		global SimboloFoiClicado
		if self.SimboloFoiClicado:
			self.Entrada2.append("3")
			self.AmostrarEntrada2['text'] = ''.join(self.Entrada2)
		else:
			self.Entrada1.append("3")
			self.AmostrarEntrada1['text'] = ''.join(self.Entrada1)

	def Numero2(self):
		global SimboloFoiClicado
		if self.SimboloFoiClicado:
			self.Entrada2.append("2")
			self.AmostrarEntrada2['text'] = ''.join(self.Entrada2)
		else:
			self.Entrada1.append("2")
			self.AmostrarEntrada1['text'] = ''.join(self.Entrada1)

	def Numero1(self):
		global SimboloFoiClicado
		if self.SimboloFoiClicado:
			self.Entrada2.append("1")
			self.AmostrarEntrada2['text'] = ''.join(self.Entrada2)
		else:
			self.Entrada1.append("1")
			self.AmostrarEntrada1['text'] = ''.join(self.Entrada1)

	def Numero0(self):
		global SimboloFoiClicado
		if self.SimboloFoiClicado:
			self.Entrada2.append("0")
			self.AmostrarEntrada2['text'] = ''.join(self.Entrada2)
		else:
			self.Entrada1.append("0")
			self.AmostrarEntrada1['text'] = ''.join(self.Entrada1)

	def PontoFinal(self):
		global SimboloFoiClicado
		if self.SimboloFoiClicado and "." not in self.Entrada2:
			self.Entrada2.append(".")
			self.AmostrarEntrada2['text'] = ''.join(self.Entrada2)
		elif not(self.SimboloFoiClicado) and "." not in self.Entrada1:
			self.Entrada1.append(".")
			self.AmostrarEntrada1['text'] = ''.join(self.Entrada1)
	
	def FuncaoAC(self):
		global SimboloFoiClicado, Resultado, Entrada1, Entrada2
		if self.SimboloFoiClicado:
			self.Entrada2 = []
			self.AmostrarEntrada2['text'] = ''.join(self.Entrada2)
		else:
			self.Entrada1 = []
			self.AmostrarEntrada1['text'] = ''.join(self.Entrada1)
		self.Resultado['text'] = "Resultado"

	def FuncaoC(self):
		global SimboloFoiClicado, Resultado, Entrada1, Entrada2, SinalUsado
		Label(self.Janela, text= "H", bg= "black", fg= 'black', font= 'arial, 16').place(x= 80, y= 110)
		self.SinalUsado = None
		self.Entrada1, self.Entrada2 = [], []
		self.AmostrarEntrada1['text'], self.AmostrarEntrada2['text'] = ''.join(self.Entrada1),''.join(self.Entrada2)
		self.Resultado['text'] = "Resultado"
		self.EscolhaDeLabelDeCima()

	def Deletar(self):
		global SimboloFoiClicado
		try:
			if self.SimboloFoiClicado:
				self.Entrada2.pop(-1)
				self.AmostrarEntrada2['text'] = ''.join(self.Entrada2)
			else:
				self.Entrada1.pop(-1)
				self.AmostrarEntrada1['text'] = ''.join(self.Entrada1)
		except IndexError:
				messagebox.showerror("Erro","O campo está vazio")

	def SinalIgual(self):
		global SinalUsado, Resultado, Entrada1, Entrada2
		if self.AmostrarEntrada1['text'] == '' or self.AmostrarEntrada1['text'] == '.':
			self.Entrada1 = ['0']
		if self.AmostrarEntrada2['text'] == '' or self.AmostrarEntrada2['text'] == '.':
			self.Entrada2 = ['0']
		if self.SinalUsado == "+":
			self.Resultado["text"] = float(''.join(self.Entrada1)) + float(''.join(self.Entrada2))
		elif self.SinalUsado == "-":
			self.Resultado["text"] = float(''.join(self.Entrada1)) - float(''.join(self.Entrada2))
		elif self.SinalUsado == "×":
			self.Resultado["text"] = float(''.join(self.Entrada1)) * float(''.join(self.Entrada2))
		elif self.SinalUsado == "÷":
			try:
				self.Resultado["text"] = float(''.join(self.Entrada1)) / float(''.join(self.Entrada2))
			except ZeroDivisionError:
				self.Resultado["text"] = "Erro"
				messagebox.showerror("Erro de Divisão","Não pode dividir números por 0.")
		if str(self.Resultado['text'])[-2:] == ".0":
			self.Resultado["text"] = int(self.Resultado["text"])
	
	def EscolhaDeLabelDeCima(self):
		global SimboloFoiClicado
		self.SimboloFoiClicado = False
		self.Focador1['bg'] = 'red'
		self.Focador2['bg'] = 'black'

	def EscolhaDeLabelDeBaixo(self):
		global SimboloFoiClicado
		self.SimboloFoiClicado = True
		self.Focador1['bg'] = 'black'
		self.Focador2['bg'] = 'red'
	
	def AcaoVindaDoTeclado(self, event):
		global CodidosDoTeclado, FuncoesParaCodidosDoTeclado
		for posicao in range(len(self.CodidosDoTeclado)):
			if event.keysym == self.CodidosDoTeclado[posicao]:
				self.FuncoesParaCodidosDoTeclado[posicao]()

	def Sair(self, event):
		self.Janela.destroy()

CalculadoraComum()
