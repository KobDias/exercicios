a, b, c= [], [], []
for i in range(0, 20):
    if i > 9:
        b.insert(i, int(input("B: ")))
    else:
        a.insert(i, int(input("A: ")))
for k in range(0, 10):
    # teste dos indices de a
    for w in range(0, 10):
        #testes dos indices de b
        if a[k] == b[w]:
            c.insert(w, a[k])
print(f"A intersecção de A e B é {c}")