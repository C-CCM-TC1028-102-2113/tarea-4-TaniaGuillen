
def main():
    #Escribe tu código debajo de esta línea
    n= int(input('Escribe la altura del triangulo: '))
    a=n
    asterisco=0
    for i in range (1, n+1, 1):
        asterisco= '*' *i ##TE FALTÓ IMPRIMIR ESPACIOS PARA ALINEAR EL TRIANGULO A LA DERECHA
        print(asterisco) 
        a= a-1
        pass


if __name__=='__main__':
    main()
