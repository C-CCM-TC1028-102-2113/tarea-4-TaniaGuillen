

def main():
    #Escribe tu código debajo de esta línea
    x=0
    raiz= 0
    z= 0
    a=0
    import math

    x = int(input('Escribe un numero: '))
    raiz = (math.sqrt(x))
    z = raiz+1
    a = z*z
    if (a>x):
        print(z) ##El resultado debería ser un número entero.
        pass

if __name__=='__main__':
    main()
