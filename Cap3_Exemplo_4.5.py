#Escreva um programa que leia a idade de uma pessoa e indique qual sua classe eleitoral:
#a) menor que 16 anos -> não eleitor
#b) entre 18 completos e 65 anos incompletos -> eleitor obrigatório
#c) entre 16 anos completos e 18 anos incompletos ou 65 anos completos -> eleitor facultativo
Idade = int(input('Qual sua idade: '))

if Idade < 16:
    print('não eleitor')
elif Idade < 18 or Idade >= 65:
    print('eleitor facultativo')
else:
    print('Eleitor obrigatório')

print('Fim do Programa')