veloMax = float(input("Velocidade Maxima: "))
veloV = float(input("Velocidae do veiculo: "))

if veloV <= veloMax:
    print("Dentro da velocidade. Dentro da lei.")
else:
    print(f"Acima da velocidade por {veloV-veloMax} km/h")