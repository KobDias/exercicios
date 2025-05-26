nums = []
for i in range(1, 11):
    nums.insert(i, int(input(f"Num {i}: ")))
nUser = int(input("Insira o numero que deseja verificar: "))
aparece = False
soma = 0
for k in range(0, 10):
    if nUser == nums[k]:
        soma += 1
        aparece = True
if aparece == False:
    print("Não existe")
else:
    print(f"{nUser} aparece {soma} vezes")