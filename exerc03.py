#Escreva um algoritmo que leia o ano de nascimento de dez pessoas e no final mostre quantas pessoas são maiores de idade.

cont = 1
acumulador = 0
while cont <= 10:
    ddn = int(input("Digite sua data de nascimento: "))
    cont = cont + 1
    idade = 2021 - ddn
    if idade > 18:
        acumulador = acumulador + 1
print (acumulador,"pessoas são maiores de idade.")
