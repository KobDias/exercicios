for i in range(1000, 10000):
    primeiros = i // 100
    ultimos = i - (primeiros*100)
    # print(primeiros)
    # print(ultimos)
    soma = primeiros+ultimos
    if (soma**2 == i):
        print(i)