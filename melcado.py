preco = float(input("Insira o preço: "))
qtd = int(input("Insira a quantidade: "))
con = True
valor = preco*qtd
while (con==True):
    print(f"Valor da compra: {valor}R$")
    preco = float(input("Insira o preço: "))
    if preco == 0:
        print("Fechando...")
        con = False
    else:
        qtd = int(input("Insira a quantidade: "))
        valor+=preco*qtd

