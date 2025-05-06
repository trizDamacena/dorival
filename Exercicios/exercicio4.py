import random
lista = [1,2,3,4,5,6,7,8,9,10]
numero = random.choice(lista)

for i in range(1,11):
    numero = random.choice(lista)
    if i == 4 or i == 7 or i == 10 and numero % 2== 0 :
        print("Avance")
    else:
        print("Recua")
        