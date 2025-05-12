def palindromos():
    titulos = ["Ana Ana", "1DSTB-SENAI", "Subi no Onibus" ]

    for titulo in titulos:
        verificando = titulo[::-1]
        verificando = verificando.lower()
        verificando = verificando.replace(" ", "")

        titulo_original = titulo.lower()
        titulo_original = titulo_original.replace(" ", "")

        if verificando == titulo_original:
            print(f"O título {titulo} é palíndromo")
        else:
            print(f"O título {titulo} não é palíndromo")

palindromos()