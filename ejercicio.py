file2read = input("Ingrese el nombre del archivo: ")
fhandle = open(file2read)
for linea in fhandle:
    print(linea.upper())
