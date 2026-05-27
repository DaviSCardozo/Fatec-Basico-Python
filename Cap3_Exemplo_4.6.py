#Escreva um programa para uma fábrica de calçados que leia o código LL de um calçado, que é um
#número inteiro com 2 dígitos. Exiba na tela a linha do calçado, conforme a tabela a seguir. Se o
#número fornecido não estiver na tabela, deve-se exibir a mensagem "Código inválido"

Codigo = int(input('Digite o tamanho LL: '))
if Codigo == 16:
    Linha = 'Bebê'
elif Codigo == 23:
    Linha = 'Infantil feminino'
elif Codigo == 25:
    Linha = 'Infantil masculino '
elif Codigo == 29:
    Linha = 'Infantil esportivo '
elif Codigo == 42:
    Linha = 'Masculino formal'
elif Codigo == 43:
    Linha = 'Masculino casual '
elif Codigo == 49:
    Linha = 'Masculino esportivo'
elif Codigo == 52:
    Linha = 'Feminino formal salto baixo'
elif Codigo == 53:
    Linha = 'Feminino formal salto alto'
elif Codigo == 55:
    Linha = 'Feminino casual salto baixo'
elif Codigo == 56:
    Linha = 'Feminino casual salto alto'
elif Codigo == 59:
    Linha = 'Feminino esportivo'
else:
    Linha ='Código inválido'

print(f'\nO código LL {Codigo} é de um calçado da Linha: {Linha}')

