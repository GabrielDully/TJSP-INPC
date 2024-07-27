import math as m
from atualizacao_monetaria import atualizacao_monetaria

class calculo(object):

    indices = atualizacao_monetaria()


    def __init__(self, base_de_calculo: float, data_distribuicao: str, data_atualizacao: str, num_autores: int, data_recolhimento: str, valor_recolhido: float, valor_litisconsorcio: float):
        
        if type(base_de_calculo == float):
            self.base_de_calculo = base_de_calculo
        else:
            pass # Algoritmo de cálculo da base conforme 

        self.data_distribuicao = data_distribuicao
        self.data_atualizacao = data_atualizacao
        self.num_autores = num_autores
        self.data_recolhimento = data_recolhimento
        self.valor_recolhido = valor_recolhido
        self.valor_litisconsorcio = valor_litisconsorcio


    def preparo_recursal(self, ufesp):

        indiceDist = calculo.indices.consultar(self.data_distribuicao)
        indiceAtt = calculo.indices.consultar(self.data_atualizacao)

        corrigido=round(self.base_de_calculo/indiceDist*indiceAtt,2)
        valor=round(corrigido*0.04,2)
        adicional=0
        if self.num_autores>=10:
            adicional=round(ufesp*10*m.ceil(self.num_autores/10),2)
        if valor < round(ufesp*5,2):
            return round(ufesp*5+adicional,2)
        elif valor > round(3000*ufesp,2):
            return round(3000*ufesp+adicional,2)
        else:
            return valor+adicional


    def calculoCustaComDeducao(primeiroValor,indiceRecolhido,valorRecolhido,indiceAtual,Litisconsorcio):
        segundoValor=indiceAtual*(valorRecolhido+Litisconsorcio)/indiceRecolhido
        return round(primeiroValor-segundoValor,2)


# EXEMPLO DE USO
    
calc = calculo(
    base_de_calculo=120,
    data_distribuicao='01/07/2022',
    data_atualizacao='31/08/2023',
    num_autores = 1,
    data_recolhimento = '05/01/2024',
    valor_recolhido = 63.50,
    valor_litisconsorcio = 80.60
)

print(calc.preparo_recursal(34.26))
