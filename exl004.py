# Programa que recebe o salário atual de um funcionário e calcule o valor do novo salário reajustado de acordo com a tabela abaixo:
# abaixo de R$500, reajuste 15%
# de R$500 até R$1.000, reajuste 10%
# acima de R$1.000, reajuste 5%

print('\t ----Calculo do novo salário----')
salario_atual = float(input('Informe o salário atual: '))

if (salario_atual < 500):
    salario_novo = salario_atual + (salario_atual*0.15)
    print('Salário com reajuste' '=', salario_novo)

if ((salario_atual > 500) and (salario_atual <= 1000)):
    salario_novo = salario_atual + (salario_atual*0.10)
    print('Salário com reajuste' '=', salario_novo)

if (salario_atual > 1000):
    salario_novo = salario_atual + (salario_atual*0.05)
    print('Salário com reajuste' '=', salario_novo)
