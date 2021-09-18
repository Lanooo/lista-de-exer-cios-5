#Escreva um algoritmo que receba 10 valores digitados pelo usuário e no final exiba o maior número.

cont = 1
maior = 0
while cont <= 10:
    valor = int(input("Digite um valor:"))
    cont = cont + 1
    if valor > maior:
        maior = valor
print ("O maior número é", maior)
