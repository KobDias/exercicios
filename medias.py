menor = 10
maior = 0
# for i in range(1, 11):
    
# print(f"Maior: {maior}, menor: {menor}")
ain = True
contador=0
while ain == True:
    contador+=1
    if contador == 11:
            ain = False
            print(f"Maior: {maior}, menor: {menor}")
    else:
        media = float(input(f"Media {contador}: "))
        if (media >10 or media<0):
            ain = False
            print("Erro")
        else:
            if media > maior:
                maior = media
            if media < menor:
                menor = media
    

