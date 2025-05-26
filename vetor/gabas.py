#pegar o gabas
soma = 0
for i in range(1, 11):
    questao = input("Insira a alternativa").upper
    if questao == "A" or questao == "B" or questao == "C" or questao=="D" or questao=="E":
        questao.insert(i, input("gabas: "))
cond = False
while cond:
 resposta = int(input("resposta: "))
# testar cada resposta com o gabas
 for k in range(1, 11):
  if (questao[k] == resposta):
   print("resposta correta")
   Soma+=1
  print("Nota ", soma)