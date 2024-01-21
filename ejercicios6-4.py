"""
30. Ejercicio: Define una función que reciba una lista de cadenas y retorne la cadena más larga en la lista.
31. Ejercicio: Define una función que reciba un número entero n y retorne una lista con los n primeros números primos.
32. Ejercicio: Define una función que reciba una cadena y retorne la misma cadena pero con las palabras en orden inverso.
33. Ejercicio: Escribe una función que reciba una lista de tuplas y retorne una lista ordenada basada en el último elemento de cada tupla.
34. Ejercicio: Define una función que reciba una cadena y retorne la cantidad de letras vocales en la cadena.
35. Ejercicio: Define una función que reciba un número entero y retorne True si es un número primo, de lo contrario retorne False.
"""
#35
def esprimo(num):
  if num < 2:
    return False
  for i in range(2,num):
    if num % i ==0:
      return False

print(esprimo(10))
    


#34
def cantidad_vocales(cadena34):
    cadena=cadena34.lower()
    cont=0
    for i in cadena:
        if i in "aeiou":
            cont+=1
    return cont

cadena34="Hola que tal ooo"
print(cantidad_vocales(cadena34))
    

#33
def ordenarpor_ultimoelemento(tuplas):
   return sorted(tuplas, key=lambda x: x[-1])

tuplas=[(1,6,5),(4,8,8),(3,3,2)]
print(ordenarpor_ultimoelemento(tuplas))
    


#32
def cadena_inverso(cadena):
    palabras=cadena.split()  #divide en lista de palabras
    palabras_invertidas=palabras[::-1] #invierte el orden de las palabras en la lista
    cadena_invertida="".join(palabras_invertidas) #une las palabras en cadenas
    return cadena_invertida

cadena="Hola que tal"
print(cadena_inverso(cadena))

#31 primero chequeamos que sea numero primer y despues buscamos los n primos
def primo(num):
  if num < 2:
    return False
  for i in range(2,num):
    if num % i ==0:
      return False
    
  return True

def n_primos(n):
    num_primos = []
    i = 2
    while len(num_primos) < n:
        if primo(i):
            num_primos.append(i)
        i += 1
    return num_primos

n=10
print(n_primos(n))


#30
def cadena_maslarga(lista_cadenas):
    return max(lista_cadenas, key=len)

lista_cadenas=["hola","Belen","Python","Caminos"]
print(cadena_maslarga(lista_cadenas))

