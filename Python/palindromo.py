
def encontrarPalindromo(cadena):
    n = len(cadena)
    cadenaDos = ""
    palindromo = False
    for n in range(n-1, -1, -1):
        cadenaDos += cadena[n]
    
    if cadena == cadenaDos:
        palindromo = True
    
    
    return palindromo




def main():
    print('-'*21, 'Palindromo', '-'*21)
    cadena = input('Ingrese la cadena a buscar el palindromo:')
    esPalidromo  = encontrarPalindromo(cadena)
    print(f"La palabra ingresada: {cadena}. Es palidromo?: {esPalidromo}")
    


if __name__ == "__main__":
    main()