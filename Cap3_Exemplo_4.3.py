#Uma empresa financeira concede empréstimos a pessoas físicas quando o valor da parcela é menor
#que 8% do salário da pessoa. Escreva um programa que leia dois números reais: o valor do salário e
#o valor da parcela e informe se o empréstimo será concedido ou não.
Salario = float(input('Informe seu salario: R$ '))
Emprestimo = float(input('Qual o valor do emprestimo desejado? R$ '))
Parcela =  int(input('Em quantas Parcelas: '))
ValorParcela = Emprestimo / Parcela
Difereca = (Salario * 0.08)

if ValorParcela > Difereca:
    print(f'\nDescupe seu empretimo não foi concedido sua parcela ficou R${ValorParcela:.2f}\nportanto maior que 8% do seu salario R${Salario:.2f}')
else:
    print(f'\nParabens seu emprestimo foi concedido sua parcela ficou de {ValorParcela} ')

print('Fim do programa')