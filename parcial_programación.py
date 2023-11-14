def get_binary(char):
    binary_result = ""
    for i in char:
        ascii_value = ord(i)  
        binary_value = bin(ascii_value)[2:]  
        binary_result += binary_value.zfill(8)  
    return binary_result
