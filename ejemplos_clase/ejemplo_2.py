# Tipos de variables [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 3.0

# Ejemplos varialbles de texto
texto_1 = str(input("Ingrese nombre "))
texto_2 = str(input("Ingrese apellido "))

# Imprimimos los textos directo a consola
print(texto_1, texto_2)

# Vemos que los textos aparecen separadas en la consola
# Esto es porque el print agrega espacios entre cada
# variable o texto separada por coma

# Operación de unir textos (concatenar o sumar texto)
# Creamos una variable llamada suma que almacena
# el contenido de las variables texto_1 y texto_2
# separadas por un espacio

suma = texto_1 + texto_2  # Operamos la suma
# Imprimimos en consola el resultado
print('El resultado de la suma es', suma)

# Operación de unir textos (concatenar o sumar texto)
# Creamos una variable llamada mensaje que almacena
# el contenido de las variables texto_1 y texto_2
# separadas por un espacio

mensaje = texto_1 + ' ' + texto_2
print('El resultado de la suma sin espacio es', suma)
print("Ahora con espacio queda así", mensaje)

# Duplicando el texto
duplicar = int(input( "Cuantas veces desaes duplicar tu nombre"))
texto_duplicado = texto_1 * duplicar
print('Duplicar texto', texto_1, ':', texto_duplicado)
