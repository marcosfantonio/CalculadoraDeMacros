# Imports
import tkinter as tk
from tkinter import ttk


class Application:
    def __init__(self):
        # Inicialização dos Recursos da Classe
        self.root = tk.Tk()
        self.frame_um = tk.Frame(self.root)
        self.frame_dois = tk.Frame(self.root)
        self.background_padrao = "#1d3557"
        self.fonte_padrao = "Terminal 16 bold"
        self.foreground_padrao = "#f1faee"
        self.foreground_highlight = "#e63946"
        self.interface_tela()
        self.root.mainloop()

    def interface_tela(self):
        # Janela Principal
        self.root.title("Calculadora de Macros")
        self.root.geometry("500x600")
        self.root.configure(background=self.background_padrao)
        self.root.resizable(False, False)
        self.root.iconbitmap("icon.ico")

        # Frames
        self.frame_um.configure(background=self.background_padrao, width=500, height=300, borderwidth=10, relief=tk.GROOVE)
        self.frame_dois.configure(background=self.background_padrao, width=500, height=300, borderwidth=10, relief=tk.GROOVE)

        # Variáveis
        self.var_calorias = tk.IntVar()
        self.var_carboidratos = tk.IntVar()
        self.var_proteinas = tk.IntVar()
        self.var_gorduras = tk.IntVar()
        self.sexoVar = tk.IntVar()

        # Labels
        self.label_peso = tk.Label(
            self.frame_um, text="Peso : ", font=self.fonte_padrao, foreground=self.foreground_padrao, background=self.background_padrao
        )
        self.label_altura = tk.Label(
            self.frame_um, text="Altura : ", font=self.fonte_padrao, foreground=self.foreground_padrao, background=self.background_padrao
        )
        self.label_idade = tk.Label(
            self.frame_um, text="Idade : ", font=self.fonte_padrao, foreground=self.foreground_padrao, background=self.background_padrao
        )
        self.label_sexo = tk.Label(
            self.frame_um, text="Sexo : ", font=self.fonte_padrao, foreground=self.foreground_padrao, background=self.background_padrao
        )
        self.label_atividade = tk.Label(
            self.frame_um, text="Atividade : ", font=self.fonte_padrao, foreground=self.foreground_padrao, background=self.background_padrao
        )
        self.label_objetivo = tk.Label(
            self.frame_um, text="Objetivo Atual : ", font=self.fonte_padrao, foreground=self.foreground_padrao, background=self.background_padrao
        )
        self.label_calorias_um = tk.Label(
            self.frame_dois, text="Você precisa consumir ", font=self.fonte_padrao, foreground=self.foreground_padrao, background=self.background_padrao
        )
        self.label_var_calorias = tk.Label(
            self.frame_dois, textvariable=self.var_calorias, font=self.fonte_padrao, foreground=self.foreground_highlight, background=self.background_padrao
        )
        self.label_calorias_dois = tk.Label(
            self.frame_dois, text="kcal/dia", font=self.fonte_padrao, foreground=self.foreground_padrao, background=self.background_padrao
        )
        self.label_macros = tk.Label(
            self.frame_dois, text="das quais são divididas em : ", font=self.fonte_padrao, foreground=self.foreground_padrao, background=self.background_padrao
        )
        self.label_var_proteinas = tk.Label(
            self.frame_dois, textvariable=self.var_proteinas, font=self.fonte_padrao, foreground=self.foreground_highlight, background=self.background_padrao
        )
        self.label_proteinas = tk.Label(
            self.frame_dois, text="g de proteinas (30% das calor)", font=self.fonte_padrao, foreground=self.foreground_padrao, background=self.background_padrao
        )
        self.label_var_carboidratos = tk.Label(
            self.frame_dois, textvariable=self.var_carboidratos, font=self.fonte_padrao, foreground=self.foreground_highlight, background=self.background_padrao
        )
        self.label_carboidratos = tk.Label(
            self.frame_dois, text="g de carboidratos (40% das kcal)", font=self.fonte_padrao, foreground=self.foreground_padrao, background=self.background_padrao
        )
        self.label_var_gorduras = tk.Label(
            self.frame_dois, textvariable=self.var_gorduras, font=self.fonte_padrao, foreground=self.foreground_highlight, background=self.background_padrao
        )
        self.label_gorduras = tk.Label(
            self.frame_dois, text="g de gorduras (30% das kcal)", font=self.fonte_padrao, foreground=self.foreground_padrao, background=self.background_padrao
        )

        # Entrys
        self.entry_peso = tk.Entry(self.frame_um, font=self.fonte_padrao, width=3, foreground=self.foreground_highlight)
        self.entry_altura = tk.Entry(self.frame_um, font=self.fonte_padrao, width=3, foreground=self.foreground_highlight)
        self.entry_idade = tk.Entry(self.frame_um, font=self.fonte_padrao, width=3, foreground=self.foreground_highlight)

        # Botoes
        self.botao_calcular = tk.Button(
            self.frame_um, text="Calcular", command=self.calcular_calorias, font=self.fonte_padrao, foreground=self.foreground_highlight
        )

        # Radios
        self.radio_sexo_um = tk.Radiobutton(
            self.frame_um, text="Masculino", value=1, variable=self.sexoVar, font=self.fonte_padrao, background=self.background_padrao,
            foreground=self.foreground_padrao, selectcolor=self.foreground_highlight
        )
        self.radio_sexo_dois = tk.Radiobutton(
            self.frame_um, text="Feminino", value=2, variable=self.sexoVar, font=self.fonte_padrao, background=self.background_padrao,
            foreground=self.foreground_padrao, selectcolor=self.foreground_highlight
        )

        # Comboboxes
        self.combobox_atividade = ttk.Combobox(
            self.frame_um, font=self.fonte_padrao, width=25, foreground=self.foreground_highlight
        )
        self.combobox_objetivo = ttk.Combobox(
            self.frame_um, font=self.fonte_padrao, width=20, foreground=self.foreground_highlight
        )
        itens_atividade = ("Sedentário", "Atividade Física Leve", "Atividade Física Moderada", "Atividade Física Intensa")
        itens_objetivo = ("Perder Peso", "Manter Peso", "Ganhar Peso")
        self.combobox_atividade["values"] = itens_atividade
        self.combobox_objetivo["values"] = itens_objetivo

        #Placement
        self.frame_um.pack()
        self.frame_dois.pack()
        self.label_peso.place(relx=0.04, rely=0.1)
        self.entry_peso.place(relx=0.22, rely=0.1)
        self.label_altura.place(relx=0.34, rely=0.1)
        self.entry_altura.place(relx=0.56, rely=0.1)
        self.label_idade.place(relx=0.68, rely=0.1)
        self.entry_idade.place(relx=0.88, rely=0.1)
        self.label_sexo.place(relx=0.04, rely=0.25)
        self.radio_sexo_um.place(relx=0.21, rely=0.25)
        self.radio_sexo_dois.place(relx=0.55, rely=0.25)
        self.label_atividade.place(relx=0.04, rely=0.4)
        self.combobox_atividade.place(relx=0.32, rely=0.4)
        self.combobox_objetivo.place(relx=0.435, rely=0.55)
        self.label_objetivo.place(relx=0.04, rely=0.55)
        self.botao_calcular.place(relx=0.5, rely=0.82, anchor="center")
        self.label_calorias_um.place(relx=0.1, rely=0.1)
        self.label_var_calorias.place(relx=0.6, rely=0.1)
        self.label_calorias_dois.place(relx=0.7, rely=0.1)
        self.label_macros.place(relx=0.1, rely=0.25)
        self.label_proteinas.place(relx=0.18, rely=0.4)
        self.label_var_proteinas.place(relx=0.1, rely=0.4)
        self.label_carboidratos.place(relx=0.18, rely=0.55)
        self.label_var_carboidratos.place(relx=0.1, rely=0.55)
        self.label_gorduras.place(relx=0.18, rely=0.7)
        self.label_var_gorduras.place(relx=0.1, rely=0.7)

    #Funções
    def calcular_calorias(self):
        self.peso = int(self.entry_peso.get())
        self.altura = int(self.entry_altura.get())
        self.idade = int(self.entry_idade.get())
        self.sexo = int(self.sexoVar.get())
        self.atividade = self.combobox_atividade.get()
        self.objetivo = self.combobox_objetivo.get()
        self.calcular_bmr()
        self.calcular_tdee()
        self.calcular_tdee_final()
        self.calcular_macros()
        self.atualizar_dados()

    def calcular_bmr(self):
        if self.sexo == 1:
            self.bmr = (88.4 + 13.4 * self.peso) + (4.8 * self.altura) - (5.68 * self.idade)
            return self.bmr
        elif self.sexo == 2:
            self.bmr = (447.6 + 9.25 * self.peso) + (3.10 * self.altura) - (4.33 * self.idade)
            return self.bmr

    def calcular_tdee(self):
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

    def calcular_tdee_final(self):
        if self.objetivo == "Perder Peso":
            self.tdeef = self.tdee - 500
            return self.tdeef
        elif self.objetivo == "Manter Peso":
            self.tdeef = self.tdee
            return self.tdeef
        elif self.objetivo == "Ganhar Peso":
            self.tdeef = self.tdee + 500
            return self.tdeef

    def calcular_macros(self):
        self.proteinas = (self.tdeef * 0.3) / 4
        self.carbos = (self.tdeef * 0.4) / 4
        self.gorduras = (self.tdeef * 0.3) / 9
        return self.proteinas, self.carbos, self.gorduras

    def atualizar_dados(self):
        self.var_calorias.set(round(self.tdeef))
        self.var_proteinas.set(round(self.proteinas))
        self.var_carboidratos.set(round(self.carbos))
        self.var_gorduras.set(round(self.gorduras))

Application()
