goon=True
while goon:
    op = input("Insira a operação(+, -, /, *, #): ")
    if(op=="#"):
        goon = False
    else:
        n1 = float(input("N1: "))
        n2 = float(input("N2: "))

        if (op=="+"):
            print(f"A soma é {n1+n2}")

        if (op=="-"):
            print(f"A subtração é {n1-n2}")

        if(op=="/"):
            print(f"A divisao é {n1/n2}")
        if(op=="*"):
            print(f"A multiplicação é {n1*n2}")