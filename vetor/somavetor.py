v1, v2, soma = [], [], []
for i in range(0, 10):
    v1.insert(i, int(input(f"Num {i} do vetor 1: ")))
    v2.insert(i, int(input(f"Num {i} do vetor 1: ")))    
    soma.insert(i, (v1[i]+v2[i]))   
print(f"Soma {soma}")
print(f"v1: {v1} e v2 {v2}")