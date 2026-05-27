#Classificação indicativa é um conceito que se aplica à faixa etária para a qual uma obra audiovisual
#se recomenda ou não. Suponha que um filme em cartaz no cinema tenha a Classificação de 16 anos.
#Escreva um programa que leia a idade de uma pessoa e mostre se está de acordo ou não com a
#classificação.

idade = int(input('Qual sua idade : '))

if idade < 10:
    categoria = 'Este filme não recomendado para menores 10 anos '
elif idade < 14:
    categoria = 'Este filme não recomendado para menores 14 anos'
elif idade < 16:
    categoria = 'Este filme não recomendado para menores 16 anos'
elif idade < 18:
    categoria = 'Este filme não recomendado para menores 18 anos'
else:
    categoria = 'Classificação LIVRE'

print(f'{categoria}!')

print('\nFim do programa')