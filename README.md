# Parcial-herramientas

Integrantes: Valentina Feijoo(valenfei05), Cesar Zuluaga(zulu27), Isabella Erazo(bellasiv).

## Paso a Paso:
### 1. Crear un repositorio en github.
### 2. Clonar el repositorio.
Este comando se utiliza para obtener una copia completa de un repositorio, incluyendo su historial de versiones y todos los archivos de trabajo. La sintaxis básica del comando es la siguiente:
`git clone <URL_del_repositorio>`

![Captura de pantalla (34)](https://github.com/zulu27/Parcial-herramientas/assets/147516780/ba254862-d2e4-4a94-b6e1-530898df5322)

### 3.Crear el código de cada función.
![Captura de pantalla 2023-11-14 171522](https://github.com/zulu27/Parcial-herramientas/assets/147516780/40e8fdeb-460f-4eaf-9d53-a00cc480500c)

![Captura de pantalla 2023-11-14 174508](https://github.com/zulu27/Parcial-herramientas/assets/147516780/7f27b83f-479e-4b29-a6d1-bd692c5cd0f9)

![Captura de pantalla 2023-11-14 174559](https://github.com/zulu27/Parcial-herramientas/assets/147516780/085d8dac-8612-423b-b20b-d9c09a3a8741)

### 4. Subir cada archivo al repositorio de github.

### 5. Crear el archivo de Menu.

 
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
-Este código define una función llamada get_results que toma una palabra como entrada y realiza las siguientes operaciones para cada carácter en la palabra:

1.Obtiene la representación binaria del carácter utilizando la función get_binary.

2.Obtiene el valor ASCII del carácter utilizando la función get_ascii.

3.Imprime el valor ASCII y la representación binaria del carácter.

4.Agrega la representación binaria del carácter a una lista llamada lista_codigos.

5.Finalmente, imprime la lista de códigos binarios concatenados y separados por espacios, así como el total de la lista.

`# ejemplo de uso
word = "Hello"
get_results(word)
Ascii character value for H  is 72 . Binary representation of H  in a Byte is 01001000
Ascii character value for e  is 101 . Binary representation of e  in a Byte is 01100101
Ascii character value for l  is 108 . Binary representation of l  in a Byte is 01101100
Ascii character value for l  is 108 . Binary representation of l  in a Byte is 01101100
Ascii character value for o  is 111 . Binary representation of o  in a Byte is 01101111
Total: 01001000 01100101 01101100 01101100 01101111 
`
### Pull request:
-Se hicieron 4 pull request para actualizar el repositorio main, en las cuales se tuvo que hacer lo siguiente:

1.Acomodar las lineas de codigo para evitar los conflictos

2.Asegurarse de que funcionara de manera correcta el codigo

3.Confirmar que se sube el codigo de forma adecuada

-Se realizo 1 pull request para cambiar una función pues se subio la que no era, la función era get_results() pues estaba el codigo escrito de forma erronea

---
