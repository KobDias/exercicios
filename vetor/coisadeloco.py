def maior(n1, n2, n3):
    """
    Retorna o maior entre três números.
    """
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    else:
        return n3

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

print("O maior número é:", maior(n1, n2, n3))