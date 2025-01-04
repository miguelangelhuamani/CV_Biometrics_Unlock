morse_dict = {
    '11111': '0',
    '01111': '1',
    '00111': '2',
    '00011': '3',
    '00001': '4',
    '00000': '5',
    '10000': '6',
    '11000': '7',
    '11100': '8',
    '11110': '9'
}

def traductor_morse(binario):
    if binario in morse_dict.keys():
        return morse_dict[binario]
    else:
        return None

def procesar_binario(binario, valid_binario):
    if len(binario) == 5 and valid_binario:
        numero = traductor_morse(binario)
        if numero:
            print('NUMERO ES:', numero)
            binario = ""  
            return numero, binario, True
        else:
            print("NUMERO INTRODUCIDO NO VALIDO")
            return None, binario, False
    elif not valid_binario:
        return None, "", True  

    return None, binario, valid_binario