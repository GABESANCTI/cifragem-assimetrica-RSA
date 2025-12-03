import sys
from matematica_primos import obter_primos_aleatorios
from motor_rsa import criar_chaves_rsa, cifrar_mensagem, decifrar_mensagem
from ferramentas_texto import string_para_hexadecimal

def main():
    print("RSA: Rivest-Shamir-Adleman")

    # gera os primos pelo crivo
    print("\n[1] buscando numeros primos aleatorio")
    primo_p, primo_q = obter_primos_aleatorios()
    print(f"primo 'p': {primo_p}")
    print(f"primo 'q': {primo_q}")

    # gera as chaves
    print("\n[2] gerando par de chaves")
    chave_publica, chave_privada = criar_chaves_rsa(primo_p, primo_q)
    
    # mostra detalhes das chaves
    e, n = chave_publica
    d, _ = chave_privada
    
    print(f"modulo n: {n}")
    print(f"totiente phi: {(primo_p-1)*(primo_q-1)}")
    print(f"chave publica: ({e}, {n})")
    print(f"chave privada: ({d}, {n})")
    
    #  entrada
    mensagem = input("\ndigite a mensagem pra criptografar: ")
    
    # visulizacao em hexa
    vis_hex = string_para_hexadecimal(mensagem)
    print(f"\n[3] representacao hexadecimal")
    print(f"{vis_hex}")

    # criptografia
    print(f"\n[4 aplicando criptografia")
    dados_criptografados = cifrar_mensagem(mensagem, chave_publica)
    print(f"vetor cifrado: {dados_criptografados}")
    
    # mostra hex dos blocos cifrados
    blocos_hex = ' '.join([hex(num)[2:].upper() for num in dados_criptografados])
    print(f"blocos cifrados (hex): {blocos_hex}")

    # decrypt
    print(f"\n[5] fazendo a descriptografia")
    mensagem_recuperada = decifrar_mensagem(dados_criptografados, chave_privada)
    print(f"mensagem restaurada: {mensagem_recuperada}")

    if mensagem_recuperada == mensagem:
        print("\n a mensagem voltou igual a original :D")
    else:
        print("\nerro: a mensagem ta diferente")

if __name__ == "__main__":
    main()