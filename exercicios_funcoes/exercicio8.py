def quantidade_letras():
    quant_1 = len(palavra1)
    quant_2 = len(palavra2)
    quant_3 = len(palavra3)

    return quant_1, quant_2, quant_3

palavra1 = "casa"
palavra2 = "paralelepipedo"
palavra3 = "python"

print(f"A quantidade de letras em {palavra1}: {quantidade_letras()[0]}")
print(f"A quantidade de letras em {palavra2}: {quantidade_letras()[1]}")
print(f"A quantidade de letras em {palavra3}: {quantidade_letras()[2]}")