def avancar_recuar(numero4,numero7,numero10):
    if numero4 % 2 == 0 and numero7 % 2 == 0 and numero10 %2== 0:
        print("Avance")
    else:
        print("Recue")


numero4 = int(input("Digite o valor de 4: "))
numero7 = int(input("Digite o valor de 7: "))
numero10 = int(input("Digite o valor de 10: "))

avancar_recuar(numero4,numero7,numero10)