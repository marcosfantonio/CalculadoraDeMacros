from tkinter import *

root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.labelsTela()
        self.entrysTela()
        self.botoesTela()
        root.mainloop()
    def tela(self):
        self.root.title("Calculadora de Macros")
        self.root.geometry("500x500")
        self.root.resizable(False, False)
        self.root.configure(background="#F18A85")
    def labelsTela(self):
        pesoLabel = Label(root, text="Peso : ", font="Calibri 24 bold", background="#F18A85")
        pesoLabel.grid(row=0, column=0)
    def entrysTela(self):
        pesoEntry = Entry(root)
        pesoEntry.grid(row=0, column=1)
    def botoesTela(self):
        calculoBotao = Button(root, text="Calcular")
        calculoBotao.grid(row=1, column=0)

Application()
