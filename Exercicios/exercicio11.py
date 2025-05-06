
titulos = ["Ana Ana", "1DSTB-SENAI", "Subi no Onibus"]

for titulo in titulos:
    new_titulo = titulo [::-1]

    new_titulo = new_titulo.lower()
    new_titulo = new_titulo.replace(" ", "")

    tituloo = str (titulo.lower())
    tituloo = tituloo.replace(" ", "")

    if new_titulo == tituloo:
        print(f"Título {titulo} é palíndromo.")
    else:
        print(f"Título {titulo} não é palidromo.")