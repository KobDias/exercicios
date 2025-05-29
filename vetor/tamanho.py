def tamanho(n):
    """
    Retorna o tamanho de uma lista.
    """
    soma = 1
    while n/10>= 1:
        n = n // 10
        soma += 1
    return soma
n = int(input("Fala: "))
print(tamanho(n))
