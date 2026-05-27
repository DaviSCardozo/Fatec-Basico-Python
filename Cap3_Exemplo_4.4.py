#Escreva um programa que leia o nome de um aluno e as notas obtidas em três avaliações. A média
#final é a média aritmética das três notas e a pessoa estará aprovada se essa média for maior ou igual
#a 7.0. Mostre na tela o nome, a média e a situação que será "Aprovado" ou "Reprovado"

Nome = input('Digite seu nome: ')
Prova1 = float(input('Digite a nota da prova A: '))
Prova2 = float(input('Digite a nota da prova B: '))
Prova3 = float(input('Digite a nota da prova C: '))

Soma = (Prova1 + Prova2 +Prova3)/3

if Soma >= 7.0:
    print(f'\nParabens sua mèdia foi {Soma:.1f}, está APROVADO!!')
else:
    print(f'\nInfelizmente sua média foi {Soma:.1f}, está Reprovado')
