def get_results(word):
    resultado_concatenado = 'Results\n=======\n'
    for char in palabra:
        valor_ascii = get_ascii(char)
        binario = get_binary(char)
        resultado_concatenado += f'ASCII character value of "{char}" is {valor_ascii}. Binary representation of "{char}" in a Byte is {binario}\n'
    return resultado_concatenado
