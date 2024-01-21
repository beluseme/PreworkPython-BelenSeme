"""
1. Ejercicio: Dado un número, imprime si es positivo o negativo.
#2. Ejercicio: Dado un número, imprime si es par o impar.
#3. Ejercicio: Dado tres números, encuentra y muestra el mayor de ellos. """
#1
num=-3
if num > 0:
  print("Es un numero positivo")
else:
  print("Es negativo")
#2
num2=13
if num2%2 ==0:
  print("Es par")
else:
  print("Es impar")
#3
numbers=[12,3,5]
i=0
for number in numbers:
  if number>i:
    i=number
print(i)