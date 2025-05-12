def fahrenheit():
    temperaturas = [temp1, temp2, temp3]

    for temperatura in temperaturas:
        fahren = (temperatura  * 9/5) + 32
        print(f"{temperatura}C° = {fahren}°F")
temp1 = 30.0
temp2 = 100.0
temp3 = 0.0

fahrenheit()