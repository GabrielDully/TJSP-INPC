import pandas as pd
import requests
import tabula
import colorama
from colorama import Fore
colorama.init(autoreset=True)

url = "https://www.tjsp.jus.br/Download/Tabelas/TabelaDebitosJudiciais.pdf"

def download_pdf():
    resposta = requests.get(url)

    if resposta.status_code == 200:
        with open('TabelaDebitosJudiciais.pdf', 'wb') as arquivo_pdf:
            arquivo_pdf.write(resposta.content)
        print('Download concluído com sucesso.')
    else:    
        print(f"{Fore.RED}Falha ao baixar arquivo em: {Fore.RESET}'{url}'")

def gerar_df():

    def validar_coluna(nome_coluna):
        caracteres = nome_coluna.split()

        if all(caractere.isdigit() for caractere in caracteres):
            return (True, ''.join(caracteres))
        else:
            return (False,)

    try:
        tabelas = tabula.read_pdf('TabelaDebitosJudiciais.pdf', pages='all')

        df = pd.DataFrame()
        for tabela in tabelas:
            for nome_coluna in tabela.columns:
                tupla = validar_coluna(nome_coluna)
                if tupla[0] == True:
                    df[tupla[1]] = tabela[nome_coluna]
        
        print(df)

    except FileNotFoundError:
        print(f"{Fore.RED}Falha ao carregar arquivo: {Fore.RESET}'TabelaDebitosJudiciais.pdf'")

download_pdf()
gerar_df()