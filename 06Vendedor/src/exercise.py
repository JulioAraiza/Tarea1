def main():
    #escribe tu código abajo de esta línea
    total_ventas = 0
    comision = 0
    for i in range(3):
        venta = float(input("Valor de la venta: "))
        total_ventas += venta  # Esto es lo mismo que poner total_ventas + venta = total_ventas
    comision = total_ventas * 0.1

    print("La comision es de: $", comision)


    #otra posible solucion es la siguiente
'''    
    a = float(input("Valor de la venta: "))
    b = float(input("Valor de la venta: "))
    c = float(input("Valor de la venta: "))

    comision = (a + b + c) * .1
    print("La comision es de: $", comision)
'''

if __name__ == '__main__':
    main()