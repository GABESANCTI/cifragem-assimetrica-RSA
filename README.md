#Algoritmo RSA

Este projeto foi desenvolvido para a disciplina de Seguranca em Sistemas de Computacao. O objetivo e demonstrar o funcionamento pratico da criptografia assimetrica RSA, desde a geração matematica dos primos ate a cifragem de mensagens.



## Estrutura do Projeto

O sistema foi dividido em 4 móulos para facilitar a compreensão e organização, sendo: 3 de funções e 1 para execução.

### main.py

Arquivo principal do sistema. Ele e responsavel por interagir com o usuario, chamar as funções dos outros modulos e exibir os resultados na tela (geracao de chaves, mensagem em hexadecimal, texto cifrado e decifrado).

### matematica_primos.py
Lógica envolvendo numeros primos.
- gerar_primos_ate: implementa o Crivo de Eratostenes para encontrar primos ate um limite.
- obter_primos_aleatorios: utiliza o crivo para selecionar aleatoriamente dois primos distintos (p e q) necessarios para o RSA.

### motor_rsa.py
Parte matematica e as operacoes de criptografia.

- calcular_mdc: algoritmo de Euclides para o maximo divisor comum.
- calcular_inverso_multiplicativo: encontra o expoente privado 'd'.
- criar_chaves_rsa: calcula o modulo n, o totiente phi e gera o par de chaves publica e privada.
- cifrar_mensagem: aplica a formula matematica C = M^e mod n.
- decifrar_mensagem: aplica a formula matematica M = C^d mod n.

### ferramentas_texto.py
Modulo auxiliar para manipulacao de strings.

- string_para_hexadecimal: converte a mensagem de texto para sua representacao em base hexadecimal, conforme solicitado nos requisitos do trabalho.

