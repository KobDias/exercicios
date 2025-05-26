idade = int(input("Idade: "))
contador = 1
soma=idade
media=0
while idade != 0:
    idade = int(input("Idade: "))
    soma += idade
    contador += 1
    media = (soma/contador)
    print(f"A média é {media}")