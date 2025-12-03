import random

def gerar_primos_ate(limite_maximo=1000):
    """
    Gera uma lista de números primos usando a lógica de eliminação
    de múltiplos (Crivo de Eratotenes).
    """
    #  lista de booleanos, iniciam true
    #  0 e 1 são marcados como False (n são primos)
    eh_primo = [True] * (limite_maximo + 1)
    eh_primo[0] = eh_primo[1] = False

    numero_atual = 2
    while (numero_atual * numero_atual <= limite_maximo):
        if eh_primo[numero_atual]:
            # Marca todos os múltiplos como False
            for i in range(numero_atual * numero_atual, limite_maximo + 1, numero_atual):
                eh_primo[i] = False
        numero_atual += 1


    return [num for num, primo in enumerate(eh_primo) if primo]

def obter_primos_aleatorios():
    """
    Seleciona dois primos (p e q) distintos e maiores que 50
    para garantir segurança mínima na codificação ASCII.
    """
    todos_primos = gerar_primos_ate(1000)
    
    # apenas primos > 50 para garantir n > 255
    primos_validos = [x for x in todos_primos if x > 50]
    
    if len(primos_validos) < 2:
        raise ValueError("Não há primos suficientes neste intervalo.")

    # Sorteia p
    p = random.choice(primos_validos)
    
    # Sorteia q e garante que n seja igual a p
    q = random.choice(primos_validos)
    while q == p:
        q = random.choice(primos_validos)
        
    return p, q