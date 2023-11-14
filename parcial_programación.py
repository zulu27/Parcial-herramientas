from parcial_programación import get_ascii, get_binary, get_resuts
import sys

menu=int(input('Menu\n=====\n1. Character\n2. Word'))
if menu > 2 or menu < 0:
    while menu > 2 or menu < 0:
        print("por favor de una opción valida")
        menu = int(input('Menu\n=====\n1. Character\n2. Word'))

if (menu==1):
    char=input('Enter a character:')
    lenchar = len(char)
    while lenchar > 1:
        print("da un solo caracter")
        char = input("enter a character: ")
        lenchar = len(char)
    word=char
    get_result(word)
elif (menu==2):
    word=input('Enter a word:')
    lenword = len(word)
    while lenword = 1:
        print("de una solo palabra")
        word = input("enter a word: ")
        lenword = len(word)
    get_result(word)
else:
    sys.exit()

results= get_results(word)
print('Total: {0}.format(results)')
          
