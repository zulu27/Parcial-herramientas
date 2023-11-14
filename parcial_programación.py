 
def get_results(word):
    lista_codigos = ""
    for char in word:
        
        binario = get_binary(char)
        codigo = get_ascii(char)
        print ("Ascii character value for ", char, " is" ,codigo,". Binary representation of ",char," in a Byte is",binario)
        lista_codigos += binario
        lista_codigos += " "
    print("Total:",lista_codigos)
