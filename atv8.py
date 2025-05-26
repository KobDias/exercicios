n = int(input("Num: "))
soma = 1
if n > 0:
    for i in range(2, n+1):
        div = 1/i
        print(f"1/{i} = {div}")
        soma+=div
    print(f"e isso dá {soma}")
else:
    print("no")