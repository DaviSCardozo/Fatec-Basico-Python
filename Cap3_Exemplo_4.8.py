#Escreva um programa que leia um número inteiro que representa um ano. Informe se esse ano é
#bissexto ou não.
#Regra: O ano é bissexto se cumprir uma das seguintes condições:
#a) ser múltiplo de 4 e ao mesmo tempo não ser múltiplo de 100
#b) ser múltiplo de 400

ano = int(input('Digite um ano aleatorio: '))
condicao_a = (ano % 4 == 0 and ano % 100 != 0)
condicao_b = (ano % 400 == 0)
if condicao_a or condicao_b:
    print(f'este {ano}, é Bissexto')
else:
    print(f'este {ano}, não é Bissexto')