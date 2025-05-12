def dificuldade():
    numeros = [3,9, 12]
    for numero in numeros:
        if numero <= 3:
            print("Dificuldade Pequena.")
        elif numero <= 9:
            print("Dificuldade Média.")
        else:
            print("Dificuldade Grande.")

dificuldade()