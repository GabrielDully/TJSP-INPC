import pandas as pd
import requests
import tabula
from pathlib import Path
import colorama
from colorama import Fore
colorama.init(autoreset=True)

class DownloadError(Exception):
    pass

class atualizacao_monetaria(object):

    url = "https://www.tjsp.jus.br/Download/Tabelas/TabelaDebitosJudiciais.pdf"
    pkl_path = 'indices_INPC.pkl'
    pdf_path = 'TabelaDebitosJudiciais.pdf'

    def __init__(self):
        self.df = atualizacao_monetaria.carregar_df() 

    def consultar(self, data: str):
        try:
            # Espera-se o padrão DD/MM/YYYY.
            componentes = data.split('/')
            indice = self.df[componentes[2]][int(componentes[1]) - 1]
            indice = indice.replace('.', '')
            indice = indice.replace(',', '.')
            return float(indice)
        
        except IndexError:
            raise IndexError(f"{Fore.RED}Formato de data não correspondente.{Fore.RESET}\nFormato fornecido: '{data}'\nFormato esperado: 'DD/MM/YYYY'")
        
        except KeyError:
            raise KeyError(f"{Fore.RED}Ano ou mês inválidos.")


    @classmethod
    def carregar_df(cls):
        try:
            return pd.read_pickle(atualizacao_monetaria.pkl_path)
        
        except FileNotFoundError:
            if not Path(atualizacao_monetaria.pdf_path).exists():
                atualizacao_monetaria.download_pdf()
            atualizacao_monetaria.gerar_df()
            return atualizacao_monetaria.carregar_df()


    @classmethod
    def download_pdf(cls):
        resposta = requests.get(cls.url)
        if resposta.status_code == 200:
            with open(cls.pdf_path, 'wb') as arquivo_pdf:
                arquivo_pdf.write(resposta.content)
        else:    
            raise DownloadError(f"Falha no download de: '{cls.url}'") 


    @classmethod
    def gerar_df(cls):

        def validar_coluna(nome_coluna):
            caracteres = nome_coluna.split()
            if all(caractere.isdigit() for caractere in caracteres):
                return (True, ''.join(caracteres))
            else:
                return (False,)

        try:
            tabelas = tabula.read_pdf(cls.pdf_path, pages='all')
            df = pd.DataFrame()
            for tabela in tabelas:
                for nome_coluna in tabela.columns:
                    tupla = validar_coluna(nome_coluna)
                    if tupla[0] == True:
                        df[tupla[1]] = tabela[nome_coluna]
            df.to_pickle(cls.pkl_path)

        except FileNotFoundError:
            cls.download_pdf()


# Exemplos de uso do módulo.
x = atualizacao_monetaria().consultar('11/12/1964')
print(x)

# Exemplo de uso do módulo.
y = atualizacao_monetaria()

indice1 = y.consultar('03/02/2024')
print(indice1)

indice2 = y.consultar('09/03/1998')
print(indice2)