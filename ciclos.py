print ("\n=======Departamento de confecciones=======\n1. Ingresar producto a fabrica\n2. Mostrar inventario en fabrica\n0. Salir\n==========================================")

opcion = 100
listaProductos = []

while opcion != 0:
    opcion = int(input("Digita una opción: "))
    if opcion == 1:
        producto = input("Digita un producto que ingresa a fabricación: ")
        #Agregar un producto a la lista de productos
        listaProductos.append(producto)
        print (listaProductos[0])
    elif opcion == 2:
        print (f"Estamos mostrando la lista de inventario: {listaProductos}")
    elif opcion == 0:
        print ("Fin, hasta pronto...")
    else:
        print ("Opcion invalida...")