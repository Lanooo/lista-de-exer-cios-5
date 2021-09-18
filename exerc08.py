nome = str(input("Insira seu nome: "))
n1 = int(input("1ª nota: ")) 
n2 = int(input("2ª nota: "))
n3 = int(input("3ª nota: "))

m = (n1 + n2 + n3)/3

if m >= 7:
    print (f"Parabéns {nome}! Você foi aprovado.")
elif (m >= 5) and (m < 7):
    print (f"Você ficou com média {m} e está de recuperação.")
elif m < 5:
    print (f"{nome} você foi reprovado.")