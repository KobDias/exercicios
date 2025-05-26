depressao = True
contador = 0
n = 10
while depressao:
    contador+=1
    centena = n // 100
    dezena = (n-(centena*100)) //10
    unidade = n - (centena*100)-(dezena*10)
    
    if unidade > dezena > centena:
        print(n)
    n+=1
    if contador > 999:
        depressao = False
        print("Acabou")