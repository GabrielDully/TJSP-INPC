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
    
    csv_path = 'datas.csv'

    def __init__(self):
        self.df = atualizacao_monetaria.carregar_df()
        self.df_datas = pd.read_csv(atualizacao_monetaria.csv_path)


    def consultar(self, data: str): # Espera-se o padrão DD/MM/YYYY.

        componentes = data.split('/')[::-1]
        mes_ano = componentes[1].zfill(2) + '/' + componentes[0]
        dia_atualizacao = int(self.df_datas.loc[self.df_datas['mes'] == mes_ano, 'dia'].values[0])

        if int(componentes[2]) < dia_atualizacao:
            id_linha = self.df_datas.loc[self.df_datas['mes'] == mes_ano].index[0]
            mes_ano = self.df_datas.at[id_linha - 1, 'mes']
            componentes = mes_ano.split('/')[::-1]

        indice = self.df[componentes[0]][int(componentes[1]) - 1]

        return atualizacao_monetaria.formatar(indice)


    def atualizar_df(self):
        atualizacao_monetaria.download_pdf()
        atualizacao_monetaria.gerar_df()
        self.df = atualizacao_monetaria.carregar_df()


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
            

    @staticmethod
    def formatar(indice: str):
        indice = indice.replace('.', '')
        indice = indice.replace(',', '.')
        return float(indice)


# Exemplo de uso do módulo.

indices = atualizacao_monetaria()

i_1 = indices.consultar('03/03/2024')
print(i_1)

i_2 = indices.consultar('09/03/1998')
print(i_2)

i_3 = indices.consultar('09/02/2024')
print(i_3)