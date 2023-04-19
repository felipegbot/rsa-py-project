from encrypt import *
from decrypt import *
def main():
    flag=0
    while(flag==0):
        # O usuário escolhe a opção desejada
        print("\n--- RSA ---")
        print("1 - Criptografar")
        print("2 - Descriptografar")
        print("3 - Sair")
        option = input("Insira a opção desejada: ")
        print('\n')

        # O sistema redireciona para a função desejada
        if(option == "1"):
            encrypt()
        elif(option == "2"):
            decrypt()
        elif(option == "3"):
            flag=1
            exit()
        else:
            print("Opção inválida, tente novamente")


main()