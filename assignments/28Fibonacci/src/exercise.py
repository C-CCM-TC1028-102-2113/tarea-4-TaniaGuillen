
def main():
    #escribe tu código abajo de esta línea
    n = int(input('Numero: '))
    a, b = 0, 1
    for i in range (1, n):
        c = a + b
        a = b
        b = c
    print (b)
    pass

if __name__=='__main__':
    main()
