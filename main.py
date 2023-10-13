import customtkinter as ctk
from integracao_excel import transferir_para_excel
from tkinter import *
from tkinter import messagebox

ctk.set_appearance_mode('System')
ctk.set_default_color_theme('blue')

class App(ctk.CTk):

    def __init__(self) -> None:
        super().__init__()
        self.configuracao_layout()
        self.aparencia()
        self.sobrepostos()

    def configuracao_layout(self):
        self.title('Gestão de Clientes')
        self.geometry('700x500')
        self.resizable(False, False)

    def aparencia(self):
        self.aparencia_label = ctk.CTkLabel(self, text='Tema', bg_color='transparent', text_color=['#000', '#fff']).place(x=50, y=430)
        self.opcoes_aparencia = ctk.CTkOptionMenu(self, values=['Light', 'Dark', 'System'], command=self.mudar_aparencia).place(x=50, y=460)

    def sobrepostos(self):

         # Botões

        def cadastrar():
            nome = valor_nome.get()
            cpf = valor_cpf.get()
            endereco = valor_endereco.get()
            telefone = valor_telefone.get()

            transferir_para_excel(nome=nome, cpf=cpf, endereco=endereco, telefone=telefone)
            messagebox.showinfo('Sitema', 'Cliente cadastrado com sucesso!')
            limpar()

        def limpar():
            valor_nome.set('')
            valor_cpf.set('')
            valor_endereco.set('')
            valor_telefone.set('')

        # Frames

        frame_titulo = ctk.CTkFrame(self, width=700, height=50, corner_radius=0, bg_color='teal', fg_color='teal')
        frame_titulo.place(x=0, y=10)

        # Textos

        titulo = ctk.CTkLabel(frame_titulo, text='Gestão de Clientes', font=('Century Gothic bold', 24), text_color=['#000', '#fff'])
        titulo.place(relx=0.5, rely=0.5, anchor='center')

        lb_aviso = ctk.CTkLabel(self, text='Preencha todos os campos corretamente!', font=('Century Gothic bold', 13), text_color=['#000', '#fff'])
        lb_aviso.place(x=50, y=70)

        lb_nome = ctk.CTkLabel(self, text='Nome:', font=('Century Gothic bold', 13), text_color=['#000', '#fff'])
        lb_nome.place(x=50, y=120)

        lb_cpf = ctk.CTkLabel(self, text='CPF (só números):', font=('Century Gothic bold', 13), text_color=['#000', '#fff'])
        lb_cpf.place(x=400, y=120)

        lb_endereco = ctk.CTkLabel(self, text='Endereço:', font=('Century Gothic bold', 13), text_color=['#000', '#fff'])
        lb_endereco.place(x=50, y=220)

        lb_telefone = ctk.CTkLabel(self, text='Telefone com DDD (só números):', font=('Century Gothic bold', 13), text_color=['#000', '#fff'])
        lb_telefone.place(x=350, y=220)
        
        # Variaveis de Texto

        valor_nome = StringVar()
        valor_cpf = StringVar()
        valor_endereco = StringVar()
        valor_telefone = StringVar()

        # Entradas
        
        entrada_nome = ctk.CTkEntry(self, width=300, textvariable=valor_nome, font=('Century Gothic bold', 15), fg_color='transparent')
        entrada_nome.place(x=50, y=150)

        entrada_cpf = ctk.CTkEntry(self, width=250, textvariable=valor_cpf, font=('Century Gothic bold', 15), fg_color='transparent')
        entrada_cpf.place(x=400, y=150)

        entrada_endereco = ctk.CTkEntry(self, width=250, textvariable=valor_endereco, font=('Century Gothic bold', 15), fg_color='transparent')
        entrada_endereco.place(x=50, y=250)

        entrada_telefone = ctk.CTkEntry(self, width=200, textvariable=valor_telefone, font=('Century Gothic Bold', 15), fg_color='transparent')
        entrada_telefone.place(x=350, y=250)

        # Botões

        botao_cadastrar = ctk.CTkButton(self, width=200, height=50, text='Cadastrar', font=('Century Gothic Bold', 15), fg_color='teal', command=cadastrar)
        botao_cadastrar.place(x=250, y=340)

        botao_limpar = ctk.CTkButton(self, width=110, height=30, text='Limpar', font=('Century Gothic bold', 15), fg_color='teal', command=limpar)
        botao_limpar.place(x=470, y=360)

    def mudar_aparencia(self, nova_aparencia):
        ctk.set_appearance_mode(nova_aparencia)

    def enviar_dados(self):
        pass


app = App()
app.mainloop()

 