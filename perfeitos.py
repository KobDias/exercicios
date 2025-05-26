n1 = int(input("Num: "))

soma = 0

for i in range(1, n1):
    if (n1%i==0): # é divisor?
        soma += i

if soma == n1:
    print("perfeito")
else:
    print("Não é")