numeros = [3,7,9,25,26]

for numero in numeros:
    fatorial = 1
    for i in range(numero):
        fatorial += fatorial * i
    print(f"{numero}! = {fatorial}")