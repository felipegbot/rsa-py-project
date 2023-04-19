
def verificaPrimo(n):
    if n <= 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def encryptText(text: str, valorD: int, valorN: int):
    result = ""
    for i in range(len(text)):
        # Pega o código ASCII do caractere
        charCode = int(ord(text[i]))
        # calcula (TEXTO ORIGINAL ^ E) mod N
        charCodeCriptografado = pow(charCode, valorD, valorN)
        # Converte o código ASCII para caractere e concatena com o resultado
        result += chr(charCodeCriptografado)
    return result

def decryptText(text: str, valorE: int, valorN: int):
    result = ""

    for i in range(len(text)):
        charCode = int(ord(text[i]))
        # calcula (TEXTO CRIPTOGRAFADO ^ D) mod N
        charCodeDescriptografado = pow(charCode, valorE, valorN)
        result += chr(charCodeDescriptografado)
    return result


def calculaMDC(num1: int, num2: int):
    # Algoritmo de Euclides para encontrar o MDC entre dois números
    # De maneira recursiva realiza divisões sucessivas até encontrar o maior divisor comum
    if num2 == 0:
        return num1
    return calculaMDC(num2, num1 % num2)

def calculaCoprimos(primeiroNumero: int):
    coprimos = []
    for i in range(1, primeiroNumero):
        # Se o MDC entre os dois números for 1, então são primos entre si
        if len(coprimos) > 200:
            break
        if calculaMDC(primeiroNumero, i) == 1:
            coprimos.append(i)
    return coprimos

def calculaE(d: int, z: int) -> int:
    # Inicializa a variável E
    e = 0
    # Calcula E, onde E * D mod Z = 1
    for i in range(1, z):
        if (i * d) % z == 1:
            e = i
            break
    return e

