try:
    file2read = input("Ingrese nombre del archivo: ")
    f = open(file2read)
    for linea in f:
        print(linea.upper())
except:
    print("Error, archivo no existe")