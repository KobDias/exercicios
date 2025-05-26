menor = 10
maior = 0
for i in range(1, 10):
    media = float(input(f"Media {i}: "))
    if (media >10 or media<0):
            print("Erro")
    else:
        if media > maior:
            maior = media
        if media < menor:
            menor = media