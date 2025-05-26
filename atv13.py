toxico = True
maior = 0
menor = 100
while toxico:

    idade = int(input("idade: "))

    if idade == 0:
        toxico = False
    else:
        if idade > maior:
            maior = idade
        if idade < menor:
            menor = idade
print(f"Maior idade: {maior} e menor: {menor}")