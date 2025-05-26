indice = float(input("Insira o indice de poluicao: "))

if indice >= 0.05 and indice <= 0.25:
    print("Aceitavel")
else:
    if indice >=0.3:
        print("Grupo 1 deve suspender suas atividades")
    if indice >=0.4:
        print("Grupo 2 deve suspender suas atividades")
    if indice>=0.5:
        print("Grupo 3 deve suspender suas atividades")