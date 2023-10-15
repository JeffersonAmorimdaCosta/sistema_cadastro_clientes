import pandas as pd
from datetime import datetime
import json

class Cliente:

    def __init__(self, nome: str, cpf: str, endereco: str, telefone: str) -> None:
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone


def ler_excel():
    arquivo = 'cadastro_clientes.xlsx'

    df = pd.read_excel(arquivo)
    return df

# Exibir cliente
def pesquisar_cliente(cpf: str):
    df = ler_excel()

    pesquisar_cpf = cpf
    linha_cliente = df[df['CLIENTE'].apply(lambda x: json.loads(x)['cpf']) == pesquisar_cpf]

    if not linha_cliente.empty:
        dados_cliente = json.loads(linha_cliente['CLIENTE'].values[0])
        return dados_cliente
    
    return None

# Transferindo para o excel
def transferir_para_excel(nome, cpf, endereco, telefone):
    df = ler_excel()
    nome_cliente = nome
    cpf_cliente = cpf
    endereco_cliente = endereco 
    valor_cliente = telefone

    if not pesquisar_cliente(cpf_cliente):

        cliente = Cliente(nome_cliente, cpf_cliente, endereco_cliente, valor_cliente)
        data = datetime.now()
        data_cadastro = data.strftime("%Y-%m-%d %H:%M:%S")

        cliente_json = json.dumps(cliente.__dict__)

        novo_cliente = pd.DataFrame({'CLIENTE': [cliente_json], 'DATA CADASTRO': [data_cadastro]})

        df = pd.concat([df, novo_cliente], ignore_index=True)
        df.to_excel('cadastro_clientes.xlsx', index=False)
        return True    
    
    return False

def alterar_dados(nome, cpf, endereco, telefone):
    df = ler_excel()

    pesquisar_cpf = cpf
    linha_cliente = df[df['CLIENTE'].apply(lambda x: json.loads(x)['cpf']) == pesquisar_cpf]

    if not linha_cliente.empty:
        dados_cliente = json.loads(linha_cliente['CLIENTE'].values[0])
        dados_cliente['nome'] = nome
        dados_cliente['endereco'] = endereco
        dados_cliente['telefone'] = telefone

        df.at[0, 'CLIENTE'] = json.dumps(dados_cliente)

        df.to_excel('cadastro_clientes.xlsx', index=False)
        return True
     
    return False 