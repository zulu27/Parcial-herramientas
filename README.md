# Parcial-herramientas

## Operaciones

### get_ascii:

-Esta función toma un carácter como entrada y utiliza la función ord() de Python para obtener el valor ASCII correspondiente a ese carácter. Luego, devuelve ese valor ASCII. Además, se asigna el resultado de ord(text) a la variable valor. 

`# Ejemplo de uso
caracter = 'A'
valor_ascii = get_ascii(caracter)
print(f'El valor ASCII de "{caracter}" es: {valor_ascii}')
#El valor ASCII de "A" es: 65`

---
### get_binary:
-Esta función toma un string char como entrada, itera sobre cada carácter en el string, y para cada carácter, realiza lo siguiente:

1.ascii_value = ord(i): Utiliza la función ord() para obtener el valor ASCII del carácter actual (i).

2.binary_value = bin(ascii_value)[2:]: Convierte el valor ASCII a binario utilizando la función bin(). El resultado es una cadena que comienza con el prefijo '0b', por lo que se usa la indexación [2:] para eliminar ese prefijo.

3.binary_result += binary_value.zfill(8): Concatena el resultado binario al resultado acumulado (binary_result). La función zfill(8) asegura que cada representación binaria tenga exactamente 8 bits, rellenando con ceros a la izquierda si es necesario.

4.Finalmente, la función devuelve el resultado binario completo.

` # Ejemplo de uso
caracter = 'A'
resultado_binario = get_binary(caracter)
print(f'El resultado binario para "{caracter}" es: {resultado_binario}')
#Este código imprimirá el resultado binario para el carácter 'A', que es '01000001'`

---
### get_results:


---
