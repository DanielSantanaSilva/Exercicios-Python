# programa em que lê um valor inteiro e mostra a tabuada de 1 a 10 do valor lido
print('\t ----tabuada---- ')
numero = int(
    input('Informe um numero para ver a tabuada correspondente a este numero: '))
print('\n Tabuada do', numero, ':')
for i in range(1, 11):
    print(numero, 'X', i, '=', (numero*i))
