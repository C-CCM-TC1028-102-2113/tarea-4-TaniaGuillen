def main():
    #escribe tu código abajo de esta línea
    contador=0
suma=0
numero=1

while numero >=0:
    numero= float(input('Digite la calificacion:'))
    suma += numero
    contador += 1
    
if contador <0:
    print('Invalido: ')
else:
    promedio= suma/ contador
    
    print('El promedio de las {} calificaciones es igual a {}.'. format (contador, promedio))
    pass
if __name__=='__main__':
    main()
