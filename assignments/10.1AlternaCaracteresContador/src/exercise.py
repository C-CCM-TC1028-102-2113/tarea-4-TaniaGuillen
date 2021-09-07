def main():
    #escribe tu código abajo de esta línea
    n= 0
for conta in range (1, n+1):
    n=int(input('Dame un numero: '))
    if (n%2==0):
        print (n,'-%')
    else:
        print(n, '-#')
    pass

if __name__=='__main__':   
    main()
