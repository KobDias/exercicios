c = int(input("Codigo "))
n = int(input("Horas trabalhadas: "))


if n > 50:
    exc = n - 50
    
    salarioexc=exc*20
    salariototal = (50*10)+salarioexc
else:
    salarioexc = 0
    salariototal = n*10

print(f"Salario excedente: {salarioexc}")
print(f"Salario total: {salariototal}")
