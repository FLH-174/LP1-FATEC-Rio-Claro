valores = {
    1: 'I',
    5: 'V',
    10:'X',
    50:'L',
}
def numeros_romanos(numero):
    inner_list = sorted(valores, reverse=True) # Dicionário
    roman = ''
    for value in inner_list:
        while numero > value:
            roman += valores.get(value)
            numero = numero - value 
    return roman

assert numeros_romanos(58) =='LVIII'
