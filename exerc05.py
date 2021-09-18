n = int(input("Fatorial de: ") )

r = 1
count = 1

while count <= n:
    r *= count
    count += 1

print(r)