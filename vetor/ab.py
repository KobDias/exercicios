a, b, d= [], [], []
for i in range(0, 10):
    if i > 4:
        b.insert(i, int(input("B: ")))
    else:
        a.insert(i, int(input("A: ")))
c = a
for k in range(0, 5):
    for l in range(0, 5):
        if b[k] != a[l]:
            c.insert(k, b[k])
print(b)
        

print(f"A intersecção de A e B é {c}")