x = []
somar = 0
for i in range(1, 11):
    num = int(input(f"Num {i}: "))
    x.insert(i, num)
    somar += num
print(f"A soma entre {x} dá {somar}")
