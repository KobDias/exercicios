n = int(input("Numero: "))

if n>999 or n<100:
    print("Não posso")
else:
    centena = n//100
    dezena = (n - (centena*100)) // 10
    unidade = n - (centena*100) - (dezena*10)
    print(f"Centena: {centena}, Dezena: {dezena} e Unidade: {unidade}")