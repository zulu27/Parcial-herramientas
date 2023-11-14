
from parcial_programación import get_ascii, get_binary, get_resuts
import sys

def get_ascii(char):
    valor = ord(char)
    return valor
    
def get_binary(char):
    binary_result = ""
    for i in char:
        ascii_value = ord(i)  
        binary_value = bin(ascii_value)[2:]  
        binary_result += binary_value.zfill(8)  
    return binary_result
  
 
def get_results(word):
    lista_codigos = ""
    for char in word:
        
        binario = get_binary(char)
        codigo = get_ascii(char)
        print ("Ascii character value for ", char, " is" ,codigo,". Binary representation of ",char," in a Byte is",binario)
        lista_codigos += binario
        lista_codigos += " "
    print("Total:",lista_codigos)

menu=int(input('Menu\n=====\n1. Character\n2. Word'))
if menu > 2 or menu < 0:
    while menu > 2 or menu < 0:
        print("por favor de una opción valida")
        menu = int(input('Menu\n=====\n1. Character\n2. Word'))

if menu==1:
    char=input('Enter a character:')
    lenchar = len(char)
    while lenchar > 1:
        print("da un solo caracter")
        char = input("enter a character: ")
        lenchar = len(char)
    word=char
    get_results(word)
elif menu==2:
    word=input('Enter a word:')
    lenword = len(word)
    while lenword == 1:
        print("de una solo palabra")
        word = input("enter a word: ")
        lenword = len(word)
    get_results(word)
else:
    sys.exit()

print('Total: {0}.format(results)')
=======
