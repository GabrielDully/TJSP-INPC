'''
    TESTES IMPLEMENTADOS PARA O CÁLCULO DE PREPARO
    RECURSAL RELATIVOS A PAGAMENTOS A PARTIR DE
    01/01/2016 (4% SOBRE O VALOR DA CAUSA).
'''

import unittest
import calculoCustaPreparo

class TestCalculoPreparo(unittest.TestCase):
    
    def test_calculoCustaPreparo(self):
        
        # valorCausa: inferior a 5 UFESPs
        # numAutores: inferior a 10 autores
        valorCausa = 120
        indiceDist = '01/07/2022' #89.014597  # 
        indiceAtt = '31/08/2023' #92.169515   # 31/08/2023
        Ufesp = 34.26
        numAutores = 1
        total_esperado = 171.30

        self.assertEqual(calculoCustaPreparo.calculoCustaPreparo(valorCausa,indiceDist,indiceAtt,Ufesp,numAutores), total_esperado)
'''
        # valorCausa: inferior a 5 UFESPs
        # numAutores: superior ou igual a 10 autores
        valorCausa = 134.26
        indiceDist = 71.741017  # 05/12/2019
        indiceAtt = 78.495531   # 06/05/2021	
        Ufesp = 29.09          
        numAutores = 12
        total_esperado = 727.25

        self.assertEqual(calculoCustaPreparo.calculoCustaPreparo(valorCausa,indiceDist,indiceAtt,Ufesp,numAutores), total_esperado)

        # valorCausa: entre 5 e 3000 UFESPs
        # numAutores: inferior a 10 autores
        valorCausa = 26854.96
        indiceDist = 67.046243  # 18/08/2017
        indiceAtt = 69.293660   # 02/08/2018
        Ufesp = 25.70	          
        numAutores = 6
        total_esperado = 1110.21

        self.assertEqual(calculoCustaPreparo.calculoCustaPreparo(valorCausa,indiceDist,indiceAtt,Ufesp,numAutores), total_esperado)

        # valorCausa: entre 5 e 3000 UFESPs
        # numAutores: superior ou igual a 10 autores
        valorCausa = 58964.50
        indiceDist = 68.316731  # 20/06/2018
        indiceAtt = 69.779110   # 12/12/2018	
        Ufesp = 25.70       
        numAutores = 26
        total_esperado = 3180.07

        self.assertEqual(calculoCustaPreparo.calculoCustaPreparo(valorCausa,indiceDist,indiceAtt,Ufesp,numAutores), total_esperado)

        # valorCausa: superior a 3000 UFESPs
        # numAutores: inferior a 10 autores
        valorCausa = 86789.35
        indiceDist = 73.271449  # 19/03/2020
        indiceAtt = 75.163517   # 12/11/2020	
        Ufesp = 27.61        
        numAutores = 2
        total_esperado = 3561.22

        self.assertEqual(calculoCustaPreparo.calculoCustaPreparo(valorCausa,indiceDist,indiceAtt,Ufesp,numAutores), total_esperado)

        # valorCausa: superior a 3000 UFESPs
        # numAutores: superior ou igual a 10 autores
        valorCausa = 126746.09
        indiceDist = 71.741017  # 03/12/2019
        indiceAtt = 85.375435   # 23/02/2022	
        Ufesp = 31.97        
        numAutores = 33
        total_esperado = 7312.17

        self.assertEqual(calculoCustaPreparo.calculoCustaPreparo(valorCausa,indiceDist,indiceAtt,Ufesp,numAutores), total_esperado)

'''
if __name__ == '__main__':
    unittest.main()