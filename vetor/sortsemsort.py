num = float(input("Insira num 1"))
maior = num
menor = num
vetor = []
vetor[0] = num
for i in range(1, 10):
    num = float(input(f"Insira num {i}: "))
    vetor.insert(i, num)
    if num > maior:
        maior=num
    if num < menor:
        menor = num
print(f"Maior: {maior}, menor: {menor}, vetor: {vetor}")