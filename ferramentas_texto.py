import binascii

def string_para_hexadecimal(texto):
    # Converte string para bytes -> bytes para hex -> decode para string limpa
    bytes_texto = texto.encode('utf-8')
    bytes_hex = binascii.hexlify(bytes_texto)
    return bytes_hex.decode('utf-8')