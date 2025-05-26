v1, v2 = [], []
somas = 0
for i in range(0,3):
    v1.insert(i, int(input("Num: ")))
    v2.insert(i, int(input("Num: ")))
    somas += (v1[i])*(v2[i])
print(v1)
print(v2)
print(somas)


