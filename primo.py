n1 = int(input("Num: "))

divisores = []

for i in range(1, n1+1):
    if (n1%i==0):
        contador+=1
if contador == 2:
    print("primo")
else:
    print("Não é primo")