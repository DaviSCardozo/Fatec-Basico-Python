 #Escreva um programa que leia três números reais em objetos denominados A, B e C. O programa
#deve calcular e mostrar na tela os resultados das fórmulas a seguir, usando 3 casas decimais.
#Para testar seu programa considere: A = 22.65 B = –39.1 C = 18.115
#Resultado esperado: R1 = 1.665 R2 = –16042.916 R3 = –51.015 R4 = 0.555 R5 = –0.211 R6 = 2041.832
A = float (input(f'Digite um numero real para A: '))
B = float (input(f'Digite um numero real Negativo para B: '))
C = float (input(f'Digite um numero real com  3 casas decimais para C: '))
R1 = A+B+C
R2 = A*B*C
R3 = 2*(A+B) - C
R4 = (A+B+C) / 3
R5 = ((2*B) + (3*C)) / (5*A)
R6 = A**2 + B**2
print(f'o resultado de R1 = A+B+C = { R1:.3f}' )
print(f'o resultado de R2 = A*B*C = { R2:.3f}' )
print(f'o resultado de R3 = 2*(A+B) - C = { R3:.3f}' )
print(f'o resultado de R4 = (A+B+C) / 3 = { R4:.3f}' )
print(f'o resultado de R5 = ((2*B) + (3*C)) / (5*A) = { R5:.3f}' )
print(f'o resultado de R6 = A**2 + B**2 = { R6:.3f}' )
