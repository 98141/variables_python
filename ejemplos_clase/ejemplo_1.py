# Tipos de variables [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 3.0

# Ejemplos varialbles numéricas (números enteros --> int)
# 1- Crearemos una variable llamada numero_1 que almacene
# el valor entero 2
# 2- Crearemos una variable llamada numero_2 que almacene
# el valor entero 4
numero_1 = int(input("Ingrese primer numero " ))
numero_2 = int(input("Ingrese segundo numero " ))

# Realizar la suma de las dos variables
suma = numero_1 + numero_2   # Operamos la suma

# Imprimimos en consola el resultado
print('El resultado de la suma es', suma)

# Realizar la resta de las dos variables
resta = numero_1 - numero_2  # Operamos la resta

# Imprimimos en consola las variables y el resultado,
# separando el texto y las variables con comas
# ej:
print('El resultado de restar', numero_1, 'y', numero_2, 'es', resta)


# Ahora realizaremos ejemplos con números decimales --> float
print("Ahora vamos hacer ejemplos con float")
numero_3 = float(input("Ingrese tercer numero " ))
numero_4 = float(input("Ingrese cuarto numero " ))

suma = numero_3 + numero_4  # Operamos la suma

# Imprimimos en consola el resultado
print('El resultado de la suma es', suma)

resta = numero_4 - numero_3  # Operamos la resta
# Imprimimos en consola el resultado
print('El resultado de restar', numero_4, 'y', numero_3, 'es', resta)

# Ahora realizaremos un ejemplo numérico mixto
# (enteros --> int y decimales --> float)

suma = numero_3 + numero_1   # Operamos la suma
# Imprimimos en consola el resultado
print('El resultado sumar', numero_3, 'y', numero_1, 'es', suma)

resta = numero_3 - numero_1  # Operamos la resta

# Imprimimos en consola el resultado
print('El resultado de restar', numero_3, 'y', numero_1, 'es', resta)

# Ensayo de división de números enteros
division = numero_1 / numero_2
print('El resultado dividir', numero_1, 'y', numero_2, 'es', division)
