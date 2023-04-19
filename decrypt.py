from aux import *
import random as Random

def decrypt():
    flagChave = 0
    flagN = 0
    # O usuário insere o texto a ser descriptografado
    text = input("Insira o texto a ser descriptografado: ")

    # O usuário insere o valor da chave
    while(flagChave == 0):
        # É usado um try/except para garantir que o valor inserido seja numérico
        try:
            chave = int(input("Insira o valor da chave (D): "))
            flagChave = 1
        except:
            print("a chave não é numérica\n")

    # O usuário insere o valor de N
    while(flagN == 0):
        # É usado um try/except para garantir que o valor inserido seja numérico
        try:
            n = int(input("Insira o valor de N: "))
            flagN = 1
        except:
            print("N não é numérico\n")

    # O texto é descriptografado usando uma função auxiliar
    textoDescriptografado = decryptText(text, chave, n)

    # Imprime o texto descriptografado na tela
    print("\n --- Resultado ---")
    print("Texto descriptografado: " + textoDescriptografado)
