#Escreva um programa que leia um número inteiro que representa uma quantidade de tempo em
#segundos. Calcule e mostre na tela a quantidade de horas, minutos e segundos.

segundos_total = int(input("Digite a quantidade de segundos: "))
horas = segundos_total // 3600
segundos_restantes = segundos_total % 3600
minutos = segundos_restantes // 60
segundos = segundos_restantes % 60
print(f"{horas} hora(s), {minutos} minuto(s), {segundos} segundo(s)")