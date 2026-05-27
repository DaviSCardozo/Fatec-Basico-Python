#Uma empresa comercial trabalha com 3 vendedores externos e os remunera com R$ 1200,00 fixos
#mais comissão de 6% sobre o valor total vendido no mês. Escreva um programa que leia o nome e o
#total vendido pelos 3 vendedores, calcule e exiba na tela a mensagem de saída conforme o exemplo
#a seguir. Exiba os valores numéricos com duas casas decimais.
#Exemplo vendedor José Carlos Santos vendeu R$ 43759.35 e faz jus a uma comissão de R$ 3825.56
#de saída: vendedor Manoel Guimarães vendeu R$ 61417.81 e faz jus a uma comissão de R$ 4885.07
#vendedor Plínio Pereira vendeu R$ 39336.87 e faz jus a uma comissão de R$ 3560.21

nome1 = input('Digite o nome primiero vendedor: ')
vendas1 = float(input(f'Digite o valor vendido para vendedor {nome1}: R$ '))
nome2 = input('Digite o nome segundo vendedor: ')
vendas2 = float(input(f'Digite o valor vendido para vendedor  {nome2}: R$ '))
nome3 = input('Digite o nome terceiro vendedor: ')
vendas3 = float(input(f'Digite o valor vendido para vendedor {nome3}  R$ '))

salario_fixo = 1200

Cm1 = vendas1 * 0.06
Cm2 = vendas2 * 0.06
Cm3= vendas3 * 0.06

total_a_receber1 = salario_fixo + Cm1
total_a_receber2 = salario_fixo + Cm2
total_a_receber3 = salario_fixo + Cm3

print(f'\nvendedor {nome1} vendeu {vendas1} e faz jus a uma comissão de {total_a_receber1:.2f}')
print(f'vendedor {nome2} vendeu {vendas2} e faz jus a uma comissão de {total_a_receber2:.2f}')
print(f'vendedor {nome3} vendeu {vendas3} e faz jus a uma comissão de {total_a_receber3:.2f}')