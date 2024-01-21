"""
Bucles
1. Ejercicio: Imprime los números del 1 al 10 usando un bucle for .
2. Ejercicio: Imprime los números pares del 1 al 20 usando un bucle while .
3. Ejercicio: Usa un bucle para calcular la suma de los números del 1 al 100.
"""
#1
numbers=[1,2,3,4,5,6,7,8,9,10]
for number in numbers:
  print(number)

#2
i=0
while i<21:
  i+=1
  if i%2==0:
    print(i)
#3
e=0
suma=0
while e<101:
  suma+=e
  e+=1
  
else:
  print("La suma total es",suma)  