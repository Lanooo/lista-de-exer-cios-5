#Escreva um algoritmo que receba um nome e três notas e atenda exiba uma mensagem diferente para cada um dos casos a seguir:
#A) Se a média for maior que 7, exiba a mensagem "Parabéns (nome)! Você foi aprovado.";
#B) Se a média for menor que 7 e maior que 5, exiba a mensagem "Você ficou com média (media) e está de recuperação.";
#C) Se a média for menor que 5, exiba a mensagem "(Nome), você está reprovado.".

nome = str(input("Insira seu nome: "))
n1 = int(input("1ª nota: ")) 
n2 = int(input("2ª nota: "))
n3 = int(input("3ª nota: "))

m = (n1 + n2 + n3)/3

if (m >= 7) and (m <= 10):
    print (f"Parabéns {nome}! Você foi aprovado.")
elif (m >= 5) and (m < 7):
    print (f"Você ficou com média {m} e está de recuperação.")
elif m < 5:
    print (f"{nome} você foi reprovado.")
