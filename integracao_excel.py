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

# Transferindo para o excel
def transferir_para_excel(nome, cpf, endereco, telefone):
    df = ler_excel()
    nome_cliente = nome
    cpf_cliente = cpf
    endereco_cliente = endereco 
    valor_cliente = telefone

    cliente = Cliente(nome_cliente, cpf_cliente, endereco_cliente, valor_cliente)
    data = datetime.now()
    data_cadastro = data.strftime("%Y-%m-%d %H:%M:%S")

    cliente_json = json.dumps(cliente.__dict__)

    novo_cliente = pd.DataFrame({'CLIENTE': [cliente_json], 'DATA CADASTRO': [data_cadastro]})

    df = pd.concat([df, novo_cliente], ignore_index=True)
    df.to_excel('cadastro_clientes.xlsx', index=False)

# Exibir cliente
def exibir_cliente(cpf):
    df = 1
    pesquisar_cpf = cpf
    print()
    linha_cliente = df[df['CLIENTE'].apply(lambda x: json.loads(x)['cpf'] if x else None) == pesquisar_cpf]
    dados_cliente = json.loads(linha_cliente['CLIENTE'].values[0])

    for key, dados in dados_cliente.items():
        print(f'{key}: {dados}')
    print(f'Data da última compra: {linha_cliente["ULTIMA COMPRA"].values[0]}')
    print()