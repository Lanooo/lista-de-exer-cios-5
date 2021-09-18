#Escreva um algoritmo para calcular o fatorial de um número. Se o usuário digitou, por exemplo, o valor 5, o resultado a ser exibido pelo algoritmo é: 5! é igual a 120

n = int(input("Fatorial de: ") )

r = 1
count = 1

while count <= n:
    r *= count
    count += 1

print(f"{n}! é igual a {r}")
