import tkinter as tk
from tkinter import ttk
class Application():
    def __init__(self):
        self.root = tk.Tk()
        self.frameUm = tk.Frame(self.root)
        self.frameDois = tk.Frame(self.root)
        self.backPadrao = ("#EAD7D1")
        self.fontePadrao = ("Terminal 16 bold")
        self.forePadrao = ("#1F1A38")
        self.interfaceTela()
        self.root.mainloop()

    def interfaceTela(self):

        #Janela Principal
        self.root.title("Calculadora de Macros")
        self.root.geometry("500x500")
        self.root.configure(background=self.backPadrao)
        self.root.resizable(False, False)
        self.root.iconbitmap("icon.ico")

        #Frames
        self.frameUm.configure(background=self.backPadrao, width=500, height=300, borderwidth=10, relief=tk.GROOVE)
        self.frameDois.configure(background=self.backPadrao, width=500, height=200, borderwidth=10, relief=tk.GROOVE)

        #Labels
        self.pesoLabel = tk.Label(
            self.frameUm, text="Peso : ", font=self.fontePadrao, foreground=self.forePadrao, background=self.backPadrao
        )
        self.alturaLabel = tk.Label(
            self.frameUm, text="Altura : ", font=self.fontePadrao, foreground=self.forePadrao, background=self.backPadrao
        )
        self.idadeLabel = tk.Label(
            self.frameUm, text="Idade : ", font=self.fontePadrao, foreground=self.forePadrao, background=self.backPadrao
        )
        self.sexoLabel = tk.Label(
            self.frameUm, text="Sexo : ", font=self.fontePadrao, foreground=self.forePadrao, background=self.backPadrao
        )
        self.atividadeLabel = tk.Label(
            self.frameUm, text="Atividade : ", font=self.fontePadrao, foreground=self.forePadrao, background=self.backPadrao
        )
        self.objetivoLabel = tk.Label(
            self.frameUm, text="Objetivo Atual : ", font=self.fontePadrao, foreground=self.forePadrao, background=self.backPadrao
        )
        self.caloriasLabel = tk.Label(
            self.frameDois, text="Atualmente você precisa consumir : ", font=self.fontePadrao, foreground=self.forePadrao, background=self.backPadrao
        )
        self.caloriasCounter = tk.IntVar()
        self.caloriasCounterLabel = tk.Label(
            self.frameDois, textvariable=self.caloriasCounter, font=self.fontePadrao, foreground=self.forePadrao, background=self.backPadrao
        )
        self.caloriasLabelDois = tk.Label(
            self.frameDois, text="kcal para atingir seu objetivo", font=self.fontePadrao, foreground=self.forePadrao, background=self.backPadrao
        )

        #Entrys
        self.pesoEntry = tk.Entry(self.frameUm, font=self.fontePadrao, width=3, foreground=self.forePadrao)
        self.alturaEntry = tk.Entry(self.frameUm, font=self.fontePadrao, width=3, foreground=self.forePadrao)
        self.idadeEntry = tk.Entry(self.frameUm, font=self.fontePadrao, width=3, foreground=self.forePadrao)

        #Botoes
        self.calcularBotao = tk.Button(
            self.frameUm, text="Calcular", command=self.calcularCalorias, font=self.fontePadrao, foreground=self.forePadrao
        )

        #Radios
        self.sexoVar = tk.IntVar()
        self.sexoRadioUm = tk.Radiobutton(
            self.frameUm, text="Masculino", value=1, variable=self.sexoVar, font=self.fontePadrao, background=self.backPadrao,
            foreground=self.forePadrao, selectcolor="White"
        )
        self.sexoRadioDois = tk.Radiobutton(
            self.frameUm, text="Feminino", value=2, variable=self.sexoVar, font=self.fontePadrao, background=self.backPadrao,
            foreground=self.forePadrao, selectcolor="White"
        )

        #Comboboxes
        self.atividadeCombobox = ttk.Combobox(
            self.frameUm, font=self.fontePadrao, width=25, foreground=self.forePadrao
        )
        self.objetivoCombobox = ttk.Combobox(
            self.frameUm, font=self.fontePadrao, width=20, foreground=self.forePadrao
        )
        atividadeItens = ("Sedentário", "Atividade Física Leve", "Atividade Física Moderada", "Atividade Física Intensa")
        objetivoItens = ("Perder Peso", "Manter Peso", "Ganhar Peso")
        self.atividadeCombobox["values"] = atividadeItens
        self.objetivoCombobox["values"] = objetivoItens

        #Placement
        self.frameUm.pack()
        self.frameDois.pack()
        self.pesoLabel.place(relx=0.04, rely=0.1)
        self.pesoEntry.place(relx=0.22, rely=0.1)
        self.alturaLabel.place(relx=0.34, rely=0.1)
        self.alturaEntry.place(relx=0.56, rely=0.1)
        self.idadeLabel.place(relx=0.68, rely=0.1)
        self.idadeEntry.place(relx=0.88, rely=0.1)
        self.sexoLabel.place(relx=0.04, rely=0.25)
        self.sexoRadioUm.place(relx=0.21, rely=0.25)
        self.sexoRadioDois.place(relx=0.55, rely=0.25)
        self.atividadeLabel.place(relx=0.04, rely=0.4)
        self.atividadeCombobox.place(relx=0.32, rely=0.4)
        self.objetivoCombobox.place(relx=0.435, rely=0.55)
        self.objetivoLabel.place(relx=0.04, rely=0.55)
        self.caloriasLabel.place(relx=0.5, rely=0.3, anchor="center")
        self.caloriasCounterLabel.place(relx=0.5, rely=0.5, anchor="center")
        self.caloriasLabelDois.place(relx=0.5, rely=0.7, anchor="center")
        self.calcularBotao.place(relx=0.5, rely=0.82, anchor="center")

    def calcularCalorias(self):
        self.peso = int(self.pesoEntry.get())
        self.altura = int(self.alturaEntry.get())
        self.idade = int(self.idadeEntry.get())
        self.sexo = int(self.sexoVar.get())
        self.atividade = self.atividadeCombobox.get()
        self.objetivo = self.objetivoCombobox.get()
        self.calcularBmr()
        self.calcularTdee()
        self.calcularTdeeF()
        self.atualizarDados()

    def calcularBmr(self):
        if self.sexo == 1:
            self.bmr = (88.4 + 13.4 * self.peso) + (4.8 * self.altura) - (5.68 * self.idade)
            return self.bmr
        elif self.sexo == 2:
            self.bmr = (447.6 + 9.25 * self.peso) + (3.10 * self.altura) - (4.33 * self.idade)
            return self.bmr

    def calcularTdee(self):
        if self.atividade == "Sedentário":
            self.tdee = self.bmr * 1.1
            return self.tdee
        elif self.atividade == "Atividade Física Leve":
            self.tdee = self.bmr * 1.275
            return self.tdee
        elif self.atividade == "Atividade Física Moderada":
            self.tdee = self.bmr * 1.35
            return self.tdee
        elif self.atividade == "Atividade Física Intensa":
            self.tdee = self.bmr * 1.525
            return self.tdee

    def calcularTdeeF(self):
        if self.objetivo == "Perder Peso":
            self.tdeef = self.tdee - 500
            return self.tdeef
        elif self.objetivo == "Manter Peso":
            self.tdeef = self.tdee
            return self.tdeef
        elif self.objetivo == "Ganhar Peso":
            self.tdeef = self.tdee + 500
            return self.tdeef

    def atualizarDados(self):
        self.caloriasCounter.set(round(self.tdeef))

Application()
