
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
    resultado_concatenado = 'Results\n=======\n'
    for char in word:
        valor_ascii = get_ascii(char)
        binario = get_binary(char)
        resultado_concatenado += f'ASCII character value of "{char}" is {valor_ascii}. Binary representation of "{char}" in a Byte is {binario}\n'
    return resultado_concatenado
