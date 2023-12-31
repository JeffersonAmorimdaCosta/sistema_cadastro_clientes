import customtkinter as ctk
from integracao_excel import transferir_para_excel, pesquisar_cliente, alterar_dados
from tkinter import *
from tkinter import messagebox, ttk

ctk.set_appearance_mode('System')
ctk.set_default_color_theme('blue')

class App(ctk.CTk):

    def __init__(self) -> None:
        super().__init__()
        self.configuracao_layout()
        self.criar_abas()

    def configuracao_layout(self):
        self.title('Gestão de Clientes')
        self.geometry('700x500')
        self.resizable(False, False)

    def verificar_letras(self, dado):
        if dado.replace(' ', '').isalpha() or dado == '':
            return True
        return False

    def verificar_numeros(self, dado):
        if dado.isdigit() or dado == '':
            return True
        return False


    def criar_abas(self):

        self.abas = ttk.Notebook(self)

        self.aba_cadastrar = ttk.Frame(self.abas,)
        self.aba_pesquisar = ttk.Frame(self.abas)

        self.abas.add(self.aba_cadastrar, text="Cadastrar Clientes")
        self.abas.add(self.aba_pesquisar, text="Pesquisar Clientes")

        self.abas.pack(expand=1, fill='both')

        self.sobrepostos_aba_cadastrar()
        self.sobrepostos_aba_pesquisar()

    def sobrepostos_aba_cadastrar(self):

        # Botões
        def limpar():
            valor_nome.set('')
            valor_cpf.set('')
            valor_endereco.set('')
            valor_telefone.set('')

        def cadastrar():
            nome = valor_nome.get()
            cpf = valor_cpf.get()
            endereco = valor_endereco.get()
            telefone = valor_telefone.get()

            if nome == '' or cpf == '' or endereco == '' or telefone == '': 
                messagebox.showerror('Sistema', 'Preencha todos os campos!')
                return
            
            elif not len(cpf) == 11:
                messagebox.showerror('Sistema', 'O CPF deve ter 11 dígitos!')
                return
            
            confirmar = messagebox.askyesno('Sistema', f'Confirme o CPF: {cpf}\nO CPF após ser cadastrado não poderá ser alterado!\nDeseja continuar?')

            if confirmar:
                if transferir_para_excel(nome=nome, cpf=cpf, endereco=endereco, telefone=telefone):
                    messagebox.showinfo('Sistema', 'Cliente cadastrado com sucesso!')
                    limpar()                
                else:
                    messagebox.showerror('Sistema', 'Ja existe cliente cadastrado com esse CPF.')
                    valor_cpf.set('')
            else:
                valor_cpf.set('')

        # Frames

        frame_titulo = ctk.CTkFrame(self.aba_cadastrar, width=700, height=50, corner_radius=0, bg_color='teal', fg_color='teal')
        frame_titulo.place(x=0, y=10)

        # Textos

        titulo = ctk.CTkLabel(frame_titulo, text='Gestão de Clientes', font=('Century Gothic bold', 24), text_color=['#000', '#fff'])
        titulo.place(relx=0.5, rely=0.5, anchor='center')

        lb_aviso = ctk.CTkLabel(self.aba_cadastrar, text='Preencha todos os campos corretamente!', font=('Century Gothic bold', 13), text_color=['#000', '#fff'])
        lb_aviso.place(x=50, y=70)

        lb_nome = ctk.CTkLabel(self.aba_cadastrar, text='Nome:', font=('Century Gothic bold', 13), text_color=['#000', '#fff'])
        lb_nome.place(x=50, y=120)

        lb_cpf = ctk.CTkLabel(self.aba_cadastrar, text='CPF:', font=('Century Gothic bold', 13), text_color=['#000', '#fff'])
        lb_cpf.place(x=400, y=120)

        lb_endereco = ctk.CTkLabel(self.aba_cadastrar, text='Endereço:', font=('Century Gothic bold', 13), text_color=['#000', '#fff'])
        lb_endereco.place(x=50, y=220)

        lb_telefone = ctk.CTkLabel(self.aba_cadastrar, text='Telefone com DDD:', font=('Century Gothic bold', 13), text_color=['#000', '#fff'])
        lb_telefone.place(x=350, y=220)
        
        # Variaveis de Texto

        valor_nome = StringVar()
        valor_cpf = StringVar()
        valor_endereco = StringVar()
        valor_telefone = StringVar()

        # Entradas
        vcmd_letras = (self.aba_cadastrar.register(self.verificar_letras), '%P')
        vcmd_numeros = (self.aba_cadastrar.register(self.verificar_numeros), '%P')

        entrada_nome = ctk.CTkEntry(self.aba_cadastrar, width=300, textvariable=valor_nome, font=('Century Gothic bold', 15), fg_color='transparent')
        entrada_nome.place(x=50, y=150)
        entrada_nome.configure(validate='key', validatecommand=vcmd_letras)

        entrada_cpf = ctk.CTkEntry(self.aba_cadastrar, width=250, textvariable=valor_cpf, font=('Century Gothic bold', 15), fg_color='transparent')
        entrada_cpf.place(x=400, y=150)
        entrada_cpf.configure(validate='key', validatecommand=vcmd_numeros)

        entrada_endereco = ctk.CTkEntry(self.aba_cadastrar, width=250, textvariable=valor_endereco, font=('Century Gothic bold', 15), fg_color='transparent')
        entrada_endereco.place(x=50, y=250)

        entrada_telefone = ctk.CTkEntry(self.aba_cadastrar, width=200, textvariable=valor_telefone, font=('Century Gothic Bold', 15), fg_color='transparent')
        entrada_telefone.place(x=350, y=250)
        entrada_telefone.configure(validate='key', validatecommand=vcmd_numeros)

        # Botões

        botao_cadastrar = ctk.CTkButton(self.aba_cadastrar, width=200, height=50, text='Cadastrar', font=('Century Gothic Bold', 15), fg_color='teal', command=cadastrar)
        botao_cadastrar.place(x=250, y=340)

        botao_limpar = ctk.CTkButton(self.aba_cadastrar, width=110, height=30, text='Limpar', font=('Century Gothic bold', 15), fg_color='teal', command=limpar)
        botao_limpar.place(x=470, y=360)

    def sobrepostos_aba_pesquisar(self):
        
        def bloquear():
            entrada_nome.configure(state='readonly')
            entrada_endereco.configure(state='readonly')
            entrada_telefone.configure(state='readonly')

        def limpar():
            valor_nome.set('')
            valor_cpf.set('')
            valor_endereco.set('')
            valor_telefone.set('')

        def salvar_dados():
            nome = valor_nome.get()
            cpf = valor_cpf.get()
            endereco = valor_endereco.get()
            telefone = valor_telefone.get()

            resultado = alterar_dados(nome, cpf, endereco, telefone)

            if resultado:
                messagebox.showinfo('Sistema', 'Alterações feitas com sucesso.')
            else:
                messagebox.showerror('Sistema', 'CPF não encontrado.')

            limpar()
            bloquear()
            
        def alterar():
            entrada_nome.configure(state='normal')
            entrada_endereco.configure(state='normal')
            entrada_telefone.configure(state='normal')

        def mostrar_dados(nome, endereco, telefone):
            valor_nome.set(nome)
            valor_endereco.set(endereco)
            valor_telefone.set(telefone)
        
        def procurar_cliente():
            cpf = valor_cpf.get()
            if cpf == '':
                messagebox.showinfo('Sistema', 'Digite um CPF') 
                return
            
            dict_dados = pesquisar_cliente(cpf)

            if dict_dados == None:
                messagebox.showinfo('Sistema', 'CPF não encontrado no banco de dados.')
                
            else:
                nome = dict_dados['nome']
                endereco = dict_dados['endereco']
                telefone = dict_dados['telefone']

                mostrar_dados(nome, endereco, telefone)
            

        valor_nome = StringVar()
        valor_cpf = StringVar()
        valor_endereco = StringVar()
        valor_telefone = StringVar()

        # Frames

        frame_titulo = ctk.CTkFrame(self.aba_pesquisar, width=700, height=50, corner_radius=0, bg_color='teal', fg_color='teal')
        frame_titulo.place(x=0, y=10)

        # Textos

        lb_titulo = ctk.CTkLabel(frame_titulo, text='Pesquisar Clientes', font=('Century Gothic bold', 24), text_color=['#000', '#fff'])
        lb_titulo.place(relx=0.5, rely=0.5, anchor='center')

        lb_cpf = ctk.CTkLabel(self.aba_pesquisar, text='CPF:', font=('Century Gothic bold', 13), text_color=['#000', '#fff'])
        lb_cpf.place(x=50, y=100)

        lb_endereco = ctk.CTkLabel(self.aba_pesquisar, text='Endereço:', font=('Century Gothic bold', 13), text_color=['#000', '#fff'])
        lb_endereco.place(x=50, y=270)

        lb_telefone = ctk.CTkLabel(self.aba_pesquisar, text='Telefone:', font=('Century Gothic bold', 13), text_color=['#000', '#fff'])
        lb_telefone.place(x=50, y=340)

        lb_nome = ctk.CTkLabel(self.aba_pesquisar, text='Nome:', font=('Century Gothic bold', 13), text_color=['#000', '#fff'])
        lb_nome.place(x=50, y=200)

        # Entradas

        vcmd_letras = (self.aba_pesquisar.register(self.verificar_letras), '%P')
        vcmd_numeros = (self.aba_pesquisar.register(self.verificar_numeros), '%P')

        entrada_cpf = ctk.CTkEntry(self.aba_pesquisar, width=240, textvariable=valor_cpf, font=('Century Gothic bold', 15), fg_color='transparent')
        entrada_cpf.place(x=50, y=130)
        entrada_cpf.configure(validate='key', validatecommand=vcmd_numeros)

        # Entradas mudança
        entrada_nome = ctk.CTkEntry(self.aba_pesquisar, width=300, textvariable=valor_nome, font=('Century Gothic bold', 15), fg_color='transparent', state='readonly')
        entrada_nome.place(x=50, y=230)
        entrada_nome.configure(validate='key', validatecommand=vcmd_letras)

        entrada_endereco = ctk.CTkEntry(self.aba_pesquisar, width =250, textvariable=valor_endereco, font=('Century Gothic bold', 15), fg_color='transparent', state='readonly')
        entrada_endereco.place(x=50, y=300)

        entrada_telefone = ctk.CTkEntry(self.aba_pesquisar, width=200, textvariable=valor_telefone, font=('Century Gothic Bold', 15), fg_color='transparent', state='readonly')
        entrada_telefone.place(x=50, y=370)
        entrada_telefone.configure(validate='key', validatecommand=vcmd_numeros)

        # Botões
        botao_pesquisar = ctk.CTkButton(self.aba_pesquisar, width=100, height=28, text='Pesquisar', font=('Century Gothic bold', 15), fg_color='teal', command=procurar_cliente)
        botao_pesquisar.place(x=320, y=130)

        botao_alterar = ctk.CTkButton(self.aba_pesquisar, width=100, height=28, text='Alterar', font=('Century Gothic bold', 15), fg_color='teal', command=alterar)
        botao_alterar.place(x=350, y=370)

        botao_salvar = ctk.CTkButton(self.aba_pesquisar, width=100, height=28, text='Salvar', font=('Century Gothic bold', 15), fg_color='teal', command=salvar_dados)
        botao_salvar.place(x=470, y=370)


app = App()
app.mainloop()

