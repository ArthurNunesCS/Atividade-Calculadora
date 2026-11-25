from tkinter import *
class Application:
    def __init__(self, master=NONE):
        self.num1 = None
        self.operacao = None
        self.novoNum = False
        
        self.visor = Entry(janela, width=11,  justify="right", font="Arial, 24")
        self.visor.grid(row=0,column=0, columnspan=4, pady=5)
        
        self.botaoC = Button(janela, text="C",height=2, width=6, command=self.limpar)
        self.botaoC.grid(row=1, column=0)
        
        self.botaoApagar = Button(janela, text="⌫",height=2, width=6, command=lambda: self.apagar())
        self.botaoApagar.grid(row=1, column=1)
        
        self.botaoDivisao = Button(janela, text="÷",height=2, width=6, command=lambda: self.operar("/"))
        self.botaoDivisao.grid(row=1, column=2)
        
        self.botaoMulti = Button(janela, text="x",height=2,  width=6, command=lambda: self.operar("*"))
        self.botaoMulti.grid(row=1, column=3)
        
        self.botao7 = Button(janela, text="7",height=2, width=6, command=lambda: self.digitar(7))
        self.botao7.grid(row=2, column=0)
        
        self.botao8 = Button(janela, text="8",height=2, width=6,command=lambda: self.digitar(8))
        self.botao8.grid(row=2, column=1)
        
        self.botao9 = Button(janela, text="9",height=2, width=6,command=lambda: self.digitar(9))
        self.botao9.grid(row=2, column=2)
        
        self.botaoMenos = Button(janela, text="-",height=2, width=6, command=lambda: self.operar("-"))
        self.botaoMenos.grid(row=2, column=3)
        
        self.botao4 = Button(janela, text="4",height=2, width=6,command=lambda: self.digitar(4))
        self.botao4.grid(row=3, column=0)
        
        self.botao5 = Button(janela, text="5",height=2, width=6,command=lambda: self.digitar(5))
        self.botao5.grid(row=3, column=1)
        
        self.botao6 = Button(janela, text="6",height=2, width=6,command=lambda: self.digitar(6))
        self.botao6.grid(row=3, column=2)
        
        self.botaoMais = Button(janela, text="+",height=2, width=6, command=lambda: self.operar("+"))
        self.botaoMais.grid(row=3, column=3)
        
        self.botao1 = Button(janela, text="1",height=2, width=6,command=lambda: self.digitar(1))
        self.botao1.grid(row=4, column=0)
        
        self.botao2 = Button(janela, text="2",height=2, width=6,command=lambda: self.digitar(2))
        self.botao2.grid(row=4, column=1)
                
        self.botao3 = Button(janela, text="3",height=2, width=6,command=lambda: self.digitar(3))
        self.botao3.grid(row=4, column=2)
        
        self.botaoIgual = Button(janela, text="=", height=5, width=6, command=lambda: self.resultado())
        self.botaoIgual.grid(row=4,rowspan=2, column=3) 
        
        self.botao0 = Button(janela, text="0",height=2, width=14,command=lambda: self.digitar(0))
        self.botao0.grid(columnspan=2, row=5, column=0)
        
        self.botaoPonto = Button(janela, text=".",height=2, width=6,command=lambda: (self.verificaPonto()))
        self.botaoPonto.grid(row=5, column=2)
        
    def digitar(self,numero):
        if self.novoNum:
            self.visor.delete(0, END)
            self.novoNum = False
         
        atual = self.visor.get()    
        if atual == "0" or atual == "Erro":
            if numero == "0":
                return
            self.limpar()
        self.visor.insert(END, numero)
        
    def limpar(self):
        self.visor.delete(0,END)
        self.num1 = None
        self.operacao = None
        self.novoNum = False
        
    def apagar(self):
        self.visor.delete(len(self.visor.get()) - 1,END)
        
    def verificaPonto(self):
        if self.novoNum:
            self.visor.delete(0, END)
        self.novoNum = False

        atual = self.visor.get()
        if "." in atual:
            return
        if atual == "":
            self.visor.insert(END, "0.")
        else:
            self.visor.insert(END, ".")
           
    def operar(self, op):
        atual = self.visor.get()
        if atual == "":
            return
        
        if self.operacao is not None and not self.novo_numero:
            if not self.calcular():
                return
            
        self.num1 = float(self.visor.get())
        self.operacao = op
        self.novoNum = True
        
    def calculo(self):
        try:
            num2 = float(self.visor.get())
            if self.operacao == "+":
                resultado = self.num1 + num2
            elif self.operacao == "-":
                resultado = self.num1 - num2
            elif self.operacao == "/":
                resultado = self.num1 / num2
            elif self.operacao == "*":
                resultado = self.num1 * num2
            else:
                return False
            
            self.mostrar(f"{resultado:.10g}")
            self.num1 = resultado
            return True    
            
        except (SyntaxError, ZeroDivisionError):
            self.num1 = None
            self.operacao = None
            self.novo_numero = True
            self.visor.delete(0, END)
            self.mostrar("Erro")
        
    def resultado(self):
        texto = self.visor.get()
        if self.operacao is None or texto == "" or texto == "Erro" or self.novoNum:
            return
        if self.calculo():
            self.operacao = None
            self.novoNum = True    
        
    def mostrar(self, texto):
        self.visor.delete(0,END)
        self.visor.insert(END, texto)
        
janela = Tk()
janela.title("Calculadora")
Application(janela)
janela.mainloop()