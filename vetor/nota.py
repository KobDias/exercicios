astigmatismo = True
idades = []
while astigmatismo:
    n1 = int(input("Idade, vadia: "))
    if n1 == 0:
        astigmatismo = False
        idades.sort()
        tamanho = len(idades)
        print(f"menor: {idades[0]}, maior: {idades[tamanho-1]}")
    else:
        idades.append(n1)
