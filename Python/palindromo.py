#Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida. | Y muestra si es palindromo
def encontrarPalindromo(cadena):
    n = len(cadena)
    cadenaDos = ""
    palindromo = False
    for n in range(n-1, -1, -1):
        cadenaDos += cadena[n]
    
    if cadena == cadenaDos:
        palindromo = True
    
    
    return palindromo, cadenaDos

#Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.
def correoElectronico(email):
    return(email[:email.find('@')] + '@ceu.es')

def main():
    print('-'*21, 'Palindromo', '-'*21)
    cadena = input('Ingrese la cadena a buscar el palindromo:')
    esPalidromo,cadenaInvertida  = encontrarPalindromo(cadena)

    print(f"La palabra ingresada: {cadena}, tiene una cadena invertida: {cadenaInvertida} . Es palidromo?: {esPalidromo}")

    print('-'*21, 'Correo Modificado', '-'*21)

    correo = input('Ingrese su correo Electronico: ')

    correoModificado = correoElectronico(correo)
    print(f"El correo electronico original es: {correo} | Y el institucional: {correoModificado}")
    


if __name__ == "__main__":
    main()