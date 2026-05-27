#Quando uma pessoa ou uma empresa realiza um investimento espera-se um retorno positivo (lucro),
#embora também possa ocorrer um retorno negativo (prejuízo). Uma forma inicial de avaliar o retorno
#é conhecida com Retorno sobre Investimento (ou ROI, uma sigla em inglês). Cálculo do ROI:
#𝑅𝑂𝐼 =
#𝑅𝑒𝑐𝑒𝑖𝑡𝑎 − (𝐶𝑢𝑠𝑡𝑜𝑠 + 𝐼𝑛𝑣𝑒𝑠𝑡𝑖𝑚𝑒𝑛𝑡𝑜)
#𝐶𝑢𝑠𝑡𝑜𝑠+𝐼𝑛𝑣𝑒𝑠𝑡𝑖𝑚𝑒𝑛𝑡𝑜
#. 100%
#Escreva um programa que leia 3 dados de entrada reais: Investimento, Custos e Receita, calcule o
#ROI usando a fórmula acima e exiba o resultado com uma casa decimal no formato mostrado abaixo.

Inv = float(input('digite o valor do investimento: R$ '))
Cus = float(input('digite o valor do custo: R$ '))
Rec = float(input('digite o valor do receita: R$ '))

#cal =  Rec - (Cus + Inv)
#cal1 = Cus + Inv
#cal2 = cal / cal1
Roi = ((Rec - (Cus + Inv)) / (Cus + Inv)) * 100
print(f'ROI = {Roi: .1f} %')