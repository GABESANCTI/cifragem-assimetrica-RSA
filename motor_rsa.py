def calcular_mdc(x, y):
    """
    Algoritmo de Euclides para encontrar o
    Max Divisor Comum entre dois numeros.
    """
    while y:
        x, y = y, x % y
    return x

def calcular_inverso_multiplicativo(e, phi):
    """
    Calcula o expoente privado 'd' tal que (d * e) % phi == 1.
    Utiliza a função nativa pow(base, exp, mod) do Python.
    """
    try:
        # O -1 indica que queremos o inverso modular
        return pow(e, -1, phi)
    except ValueError:
        raise ValueError("Erro  'e' não é coprimo de 'phi'.")

def criar_chaves_rsa(p, q):
    """
    Gera as chaves publica e privada com base nos primos p e q.
    Retorna: ((e, n), (d, n))
    """
    #Calcular o módulo n
    n = p * q
    
    # Calcular a função totiente phi(n)
    phi = (p - 1) * (q - 1)
    
    # Escolher o expoente ppublico 'e'
    # Deve ser coprimo de phi (mdc=1) e 1 < e < phi.
    # Começamos de 3 e testamos ímpares.
    e = 3
    while calcular_mdc(e, phi) != 1:
        e += 2
        
    # Calcular o expoente privado 'd'
    d = calcular_inverso_multiplicativo(e, phi)
    
    # Retorna Chave publica, Chave Privada
    return ((e, n), (d, n))

def cifrar_mensagem(texto_original, chave_pub):
 
    e, n = chave_pub
    lista_cifrada = []
    
    for caractere in texto_original:
        #  caractere para numero inteiro tabela ASCII
        m = ord(caractere)
        
        # Verifica segurança básica do bloco
        if m >= n:
             raise ValueError(f"Erro: O módulo n ({n}) é muito pequeno para o caractere '{caractere}'.")

        # Aplica formula RSA
        c = pow(m, e, n)
        lista_cifrada.append(c)
        
    return lista_cifrada

def decifrar_mensagem(lista_numeros, chave_priv):
    """
    Decrypt  lista de numeros usando a formula: M = C^d mod n.
    """
    d, n = chave_priv
    texto_recuperado = ""
    
    for c in lista_numeros:
        # aplica formula inversa RSA
        m = pow(c, d, n)
        
        # Converte o numero resultante de volta para caractere
        texto_recuperado += chr(m)
        
    return texto_recuperado