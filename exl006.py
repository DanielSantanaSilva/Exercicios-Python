# Programa que recebe um número digitado pelo usuário e calcula a soma de todos os números de 1 até ao número digitado.
soma_numeros = 0
numero = int(input('Por favor, digite um numero: '))
for i in range(1, numero + 1, 1):
    soma_numeros += i
print('A soma é =', soma_numeros)
