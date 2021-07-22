def main():
    #escribe tu código abajo de esta línea
    subtotal = 0
    for producto in range(4):
        precio = float(input("Dame el precio "))
        subtotal += precio
    total = subtotal * 0.85
    print("El total es de: $ ", total)

if __name__ == '__main__':
    main()
