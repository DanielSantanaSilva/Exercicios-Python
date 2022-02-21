# Programa que recebe um valor inteiro e informa se o número é positivo, negativo ou neutro
print('\t ----A dança dos números---- ')
x = int(input("Informe um numero para brincar: "))
if x < 0:
    print('É um numero negativo ')

elif x == 0:
    print('É um numero neutro')

elif x > 0:
    print('É um numero positivo')
