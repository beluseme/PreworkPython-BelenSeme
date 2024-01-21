"""
11.Define una función que tome una cadena y determine si es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
12. Ejercicio: Escribe un programa que imprima los números del 1 al 50, pero para múltiplos de tres imprima “Fizz” en lugar del número y para los múltiplos de cinco imprima “Buzz”. Para números que son múltiplos de tanto tres como cinco imprima “FizzBuzz”.
13. Ejercicio: Define una función que tome una lista y retorne la lista ordenada en orden ascendente.
14. Ejercicio: Define una función que reciba una lista de palabras y un entero n, y retorne la lista de palabras que son más largas que n.
15. Ejercicio: Define una función que tome un número y calcule su serie de Fibonacci.
16. Ejercicio: Define una función que tome una lista de números y retorne el número más grande de la lista.
17. Ejercicio: Define una función que reciba un número y retorne la suma de sus dígitos al cubo.
18. Ejercicio: Define una función que reciba una lista de números y retorne el segundo número más grande de la lista.
19. Ejercicio: Define una función que tome dos listas y retorne True si tienen al menos un miembro en común, de lo contrario, retorne False.
20. Ejercicio: Define una función que tome una lista y retorne una nueva lista con los elementos de la lista original en orden inverso.

"""
#20
def listainversa(lista20):
    lista_inversa= lista20[::-1]
    return lista_inversa

lista20=[1, 4, 3, 4,6,9,3,5,2]
print(listainversa(lista20))

#19
# bool() para convertir el resultado a un valor booleano
def miembro_encomun(lista19,lista19a):
    return bool(set(lista19)&set(lista19a))

lista1=[1, 4, 3, 4]
lista2=[7, 9, 2, 2]

resultado= miembro_encomun(lista1,lista2)
if resultado:
  print("Tienen miembros en comun")
else:
  print("No tiene miembros en comun") 

#18
#set elimina duplicados y sorted ordena la lista
def segundo_mayor(lista18):
  list_ordenada= sorted(set(lista18), reverse=True)
  return list_ordenada[1]

lista18= [1,3,2,7,5,9,23,14]
print(segundo_mayor(lista18))


#17
def calculo(num17):
  strnum=str(num17)
  suma_cubo= sum(int(digito)**3 for digito in strnum)
  return suma_cubo

print(calculo(10))

#16
def nunmax(lista16):
  return max(lista16)

print(nunmax([2,6,4,3,8,6,9]))

#15
def fibonacci(num1):
  if num1 <= 0: 
    return "no hay serie"
  elif num1==1: 
    return [0]
  
  fibo = [0,1]
  while len(fibo) < num1:
    fibo.append(fibo[-1] + fibo[-2])
  return fibo

print(fibonacci(10))


#14
def maslarga_n(lista3,n):
  palabras_maslargas=[]
  for palabra in lista3:
    if len(palabra) > n:
      palabras_maslargas.append(palabra)
  return palabras_maslargas
      
    
print(maslarga_n(["hola","belen","visualcode","thepower"],4))

    

#13
def ordenar_lista(list):
  lista_ord= sorted(list)
  return lista_ord

print(ordenar_lista([2,1,5,8,3,5,4]))    

#12
for i in range (1,51):
  if i%3==0 and i%5==0:
    print("FizzBuzz")
  elif i%3==0:
    print("Fizz")
  elif i%5==0:
    print("Buzz")
  else:
    print(i)


#11
def es_palindromo(cadena):
  cadena2=cadena[::-1]
  if cadena2==cadena:
    print("Es polindromo")
    return True
  else:
    print("No es polidromo")
    return False
  
print(es_palindromo("asa"))
