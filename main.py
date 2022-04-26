import os

n1 = int(input("Digite um número: "))
os.system('clear')

if (n1 >=100 and n1 <= 200):
  print("Está no intervalo de 100 a 200")
elif(n1 > 200):
  print("O número é maior que 200")
elif(n1 < 100):
  print("O número é menor que 100")