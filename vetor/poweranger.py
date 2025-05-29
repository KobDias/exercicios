def E_Primo(n):
    """
    Verifica se um número é primo.
    """
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
de = int(input("Fala de: "))
ate = int(input("Fala até: "))
for i in range(de, ate + 1):
    if E_Primo(i):
        print(i, end=' ')