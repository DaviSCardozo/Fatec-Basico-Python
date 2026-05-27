#Escreva um programa que leia um número inteiro e mostre na tela se ele é divisível por 10 ou não.
Numero = int(input('Digite um numero: '))
cal = Numero % 10

if cal == 0:
    print('E divisivel por 10')
else:
    print('Não é divisivel por 10')
