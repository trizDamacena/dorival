def verificador():
    clientes = [15,20,8]

    for cliente in clientes:
        if cliente >= 18:
            print(f"O cliente com a idade de {cliente} anos pode assistir ao filme.")
        else:
            print(f"O cliente com a idade de {cliente} anos não pode asisstir ao filme.")

verificador()
