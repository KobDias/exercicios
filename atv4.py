peso = float(input("Ta pesando quanto "))

if peso > 50:
    exc = peso - 50
    print(f"Houve excedente de {exc} quilos, ou seja, a multa será de {exc*4.00}R$")
else:
    print("Sem multa po")