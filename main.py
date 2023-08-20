from tkinter import *

#Janela
root = Tk()
root.title("Calculadora de Macros")
root.geometry("500x500")

#Textos
pesoLabel = Label(root, text="Peso : ", font = "Calibri 24 bold")
pesoLabel.grid(row=0, column=0)

#Entrada
pesoEntry = Entry(root)
pesoEntry.grid(row=0, column=1)
calculoBotao = Button(root, text="Calcular")
calculoBotao.grid(row=1, column=0)
#Loop Principal
root.mainloop()