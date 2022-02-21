# Programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
# Considerando 1 dólar = 5,26 reais

n = float(input("Quanto dinheiro você tem? \nR$"))
dolar = 5.26
conversao = n / dolar
print("Com R${} você pode comprar US$ {:.2f}.".format(n, conversao))
