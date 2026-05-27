#Escreva um programa que leia um número real e mostre na tela os valores de 25%, 50%, 75% do
#valor lido usando o formato com 3 casas decimais mostrado abaixo:
X = float(input('Digite um numero : '))
A = X * 0.25
B = X * 0.5
C = X * 0.75
print(f'25% -> {A:.3f}  -  50% -> {B:.3f}  - 75% -> {C:.3f}')