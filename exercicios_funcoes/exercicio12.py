def fatorial():
    fatoriais = [3,7,9,25,26]

    for numero in fatoriais:
        fatorial = 1
        for i in range(numero):
            fatorial += fatorial * i
        print(f"{numero}! = {fatorial}")
fatorial()