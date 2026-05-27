#Escreva um programa que leia 3 números inteiros e mostre na tela uma das seguintes opções:
#a) "Os três valores são iguais"
#b) "Há dois valores iguais e um diferente"
#c) "Os três valores são diferentes"

numero = int(input('Digite primeiro numero inteiro: '))
numero2 = int(input('Digite segundo numero inteiro: '))
numero3 = int(input('Digite terceiro numero inteiro: '))

if numero == numero2 and numero == numero3 and numero2 == numero3 :
    print('\nOs três valores são iguais')

elif (numero == numero2 and numero != numero3 or
      numero2 == numero3 and numero2 != numero or
      numero3 == numero and numero3 != numero2):
    print('\nHá dois valores iguais e um diferente')

else:
    print('\nOs três valores são diferentes')

print('\nFim do programa')