import math as m
from atualizacao_monetaria import atualizacao_monetaria

class calculo(object):

  indices = atualizacao_monetaria()

  def preparo_recursal(valorCausa,dataDist,dataAtt,Ufesp,numAutores):

    indiceDist = calculo.indices.consultar(dataDist)
    indiceAtt = calculo.indices.consultar(dataAtt)

    
    corrigido=round(valorCausa/indiceDist*indiceAtt,2)
    valor=round(corrigido*0.04,2)
    adicional=0
    if numAutores>=10:
      adicional=round(Ufesp*10*m.ceil(numAutores/10),2)
    if valor < round(Ufesp*5,2):
      return round(Ufesp*5+adicional,2)
    elif valor > round(3000*Ufesp,2):
      return round(3000*Ufesp+adicional,2)
    else:
      return valor+adicional


  def calculoCustaComDeducao(primeiroValor,indiceRecolhido,valorRecolhido,indiceAtual,Litisconsorcio):
    segundoValor=indiceAtual*(valorRecolhido+Litisconsorcio)/indiceRecolhido
    return round(primeiroValor-segundoValor,2)



