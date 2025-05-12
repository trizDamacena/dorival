def desconto():
    global produto1
    global produto2
    global produto3

    produto1 = produto1 - (produto1 * 10)/100
    produto2 = produto2 - (produto2 * 10) / 100
    produto3 = produto3 - (produto3 * 10) / 100

    print(f"Produto 1: R$ {produto1}")
    print(f"Produto 2: R$ {produto2}")
    print(f"Produto 3: R$ {produto3}")

produto1 = 50.00
produto2 = 120.00
produto3 = 200.00

desconto()