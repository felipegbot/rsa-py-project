from aux import *
import random as Random

def encrypt():
    # São inicializadas duas flags para verificar se os números inseridos são válidos
    flagP = 0
    flagQ = 0

    while(flagP == 0):
        # É usado um try/except para garantir que o valor inserido seja numérico
        try:
            p = int(input("Digite um número primo para P: "))
            # Verifica se o número é primo
            if(not verificaPrimo(p)):
                print("P não é primo\n")
            else:
            # Se o número for primo, a flag é alterada para 1, quebrando o loop
                flagP = 1
        except:
            print("P não é numérico\n")

    while(flagQ == 0):
        # É usado um try/except para garantir que o valor inserido seja numérico
        try:
            q = int(input("Digite um número primo para Q: "))
            # Verifica se o número é primo
            if(not verificaPrimo(q)):
                print("Q não é primo\n")
            else:
            # Se o número for primo, a flag é alterada para 1, quebrando o loop
                flagQ = 1
        except:
            print("Q não é numérico\n")

    # Calcula N e Z
    n = p * q
    # Aqui é usado o totiente de Euler para calcular Z
    z = (p - 1) * (q - 1)

    # Imprime os valores de P e Q na tela
    print("\n --- Valores ---")
    print("P = " + str(p))
    print("Q = " + str(q))

    # Imprime os valores de N e Z na tela
    print("N = " + str(n))
    print("Z = " + str(z))

    # Seleciona D, sendo D proveniente dos números coprimos de Z
    coprimos = calculaCoprimos(z)
    # Escolhe um número coprimo de Z aleatoriamente
    coprimoEscolhido = Random.choice(coprimos)
    # Imprime o número coprimo de Z escolhido
    print("D = " + str(coprimoEscolhido))

    # Calcula E
    e = calculaE(coprimoEscolhido, z)
    # Imprime o valor de E na tela
    print("E = " + str(e))

    # O usuário insere o texto a ser criptografado
    text = input("\nInsira o texto a ser criptografado: ")
    # O texto é criptografado usando uma função auxiliar
    textoCriptografado = encryptText(text, e, n)

    # Imprime o texto criptografado na tela
    print("\n --- Resultado ---")
    print("Texto criptografado: " + textoCriptografado)