# Programa que recebe um número, conte o número total de dígitos e mostre o resultado
print('\t ----Contagem de digitos---- ')
digitos = int(input('Digite um numero para contar seus digitos'))

contador = 0

while digitos != 0:
    digitos //= 10
    contador += 1

print("Total de dígitos=", contador)
