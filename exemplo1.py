from tkinter import *

class Application:
    def __init__(self, master=NONE):
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()
        
        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()
        
        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()
        
        self.lbl_numero1 = Label(self.primeiroContainer, text="Primeiro número: ")
        self.lbl_numero1.pack()
        
        self.entrada1 = Entry(self.primeiroContainer)
        self.entrada1.pack()
        
        self.lbl_numero2 = Label(self.segundoContainer, text="Segundo número: ")
        self.lbl_numero2.pack()
        
        self.entrada2 = Entry(self.segundoContainer)
        self.entrada2.pack()
        
        self.botaoSomar = Button(
            self.terceiroContainer,
            text="Somar",
            command=self.somar
        )
        self.botaoSomar.pack(pady=15)
        
        self.lbl_resultado = Label(self.terceiroContainer, text="Resultado: ")
        self.lbl_resultado.pack()
        
        
    def somar(self):
        n1 = float(self.entrada1.get())
        n2 = float(self.entrada2.get())
        
        resultado = n1 + n2
        
        self.lbl_resultado.config(text=f"Resultado: {resultado:.2f}")
        
root = Tk()
root.title("Calculadora")
root.geometry("500x300")
Application(root)
root.mainloop()