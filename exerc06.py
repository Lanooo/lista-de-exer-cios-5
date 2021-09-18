#Escreva um programa que receba o preço de dois produtos. Calcule um desconto de 8% no primeiro produto, 11% no segundo e apresente o valor final a ser pago.

n1 = int(input("Valor do primeiro produto: "))
n2 = int(input("Valor do segundo produto: "))

d1 = (n1*8)/100
d2 = (n2*11)/100

v1 = n1 - d1
v2 = n2 - d2
vf = v1 + v2

print (v1)
print (v2)
print ("O valor final a ser pago é: ", vf)
