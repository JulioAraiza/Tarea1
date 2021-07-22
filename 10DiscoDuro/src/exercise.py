def main():
    #escribe tu código abajo de esta línea
    gb = float(input("Capacidad en Gb "))

    mb = 1024 * gb
    kb = 1024 * mb
    b = 1024 * kb
    print("MB:", mb)
    print("KB:",kb)
    print("bytes:",b)

if __name__ == '__main__':
    main()
