valores = [50.00, 120.00, 200.00]
i = 1
for valor in valores:
    desconto = valor - (valor*10)/100
    print(f"Produto {i}: R$ {desconto}")