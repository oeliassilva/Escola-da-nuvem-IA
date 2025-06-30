temp = float(input("Digite a temperatura: "))
origem = input("Digite a unidade de origem da temperatura (C, F ou K): ").upper() #upper() converte para maiúsculas
destino = input("Digite para qual unidade de temperatura deseja converter (C, F ou K): ").upper()

if origem == destino:
    resultado = temp
elif origem == "C":
    if destino == "F":
        resultado = temp * 9/5 + 32
    else: 
        resultado = temp + 273.15
elif origem == "F":
    if destino == "C":
        resultado = (temp - 32) * 5/9
    else:  
        resultado = (temp - 32) * 5/9 + 273.15
elif origem == "K":
    if destino == "C":
        resultado = temp - 273.15
    else:  
        resultado = (temp - 273.15) * 9/5 + 32
else:
    resultado = None

if resultado is not None:
    print(f"{temp}°{origem} equivalem a {resultado:.2f}°{destino}")
else:
    print("Unidade inválida.")
