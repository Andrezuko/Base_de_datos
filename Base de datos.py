#Favor de leer el codigo de abajo hacia arriba

inventario = []
ventas = []


def formato(texto): # Para poder cambiar casos de inputs de "MoNeDa" o "moneda" a "Moneda"
    texto_strip = texto.strip()
    texto_min = texto_strip.casefold()
    texto_caps = texto_min.capitalize()
    return texto_caps


def isdigit(num): # Este de aquí ayuda a identidicar si el input es un número y que no se rompa cuando le metamos algo más
    while not num.isdigit():
        num = input("")
        if num.isdigit() == True:
            break
        print("No es una opción. Vuelva a intentarlo")
    return(num)


def salir(): # la acción realizada al salir del código
    #print(f"Cantidad de acciones realizadas: {cont}")
    print("Saliendo...")



def accion1():
    x = "y"
    while x == "y" or x == "yes": # este while es para volver a preguntarle al usuario si quiere repetir su acción para que no tenga que volver a pasar por el menu
        vendedor = input("Persona que realizó la venta:\n")
        vend = formato(vendedor)
        articulo = input("Artículo vendido:\n")
        art = formato(articulo)
        exists = False

        for i in inventario: # Checa si el 
            if i[0] == art:
                cant = ""
                while not cant.isdigit():
                    cant = input("Cantidad de " + str(art) + " que vendió?:\n")
                    if cant.isdigit() == True:
                        break
                    print("No es un número. Vuelva a intentarlo.")
                está = False

                for i in ventas:
                    if i[0] == vend:
                        if i[1] == art:
                            i[2] += cant
                            está = True
                            break
                    else:
                        break
                
                if not está:
                    ventas.append([vend, art, cant])
                
            else:
                break

        if not exists: # mensaje de error por si el vendedor no fue encontrado en la base de datos
            print("El artículo que fue vendido no fue encontrado en la base de datos. Favor de volverlo a intentar con otro artículo")

        y = str(input("Desea agregar otra venta? (Y/N):\n"))
        x = y.casefold()



def accion2():
    x = "y"
    while x == "y" or x == "yes":
        articulo = input("Ingrese artículo a inventario:\n")
        art = formato(articulo)
        cant = ""
        while not cant.isdigit():
            cant = input("Ingrese cuantos de este artículo quiere ingresar a inventario:\n")
            if cant.isdigit() == True:
                break
            print("No es un número. Vuelva a intentarlo.")

        está = False

        for i in inventario:
            if i[0] == art:
                i[1] += cant
                está = True
                break
            else:
                break
          
        if not está:
            inventario.append([art, cant])

        y = str(input("Desea agregar otro artículo? (Y/N):\n"))
        x = y.casefold()



def accion3():
    print("Hay " + str(len(inventario)) + " artículos en el inventario:")
    for i in inventario:
        print(i[1], i[0])



def accion4():
    print("Hay " + str(len(ventas)) + " ventas registradas:")
    for i in ventas:
        print(i[0],":", i[2], i[1])



def accion5():
    print("""Filtrar por vendedor o por artículo?
  1)  Vendedor
  2)  Artículo""")
    
    filt = ""
    filtro = isdigit(filt)

    if filtro == "1":
        vendedor = input("Que vendedor busca?\n")
        vend = formato(vendedor)
        está = False

        for i in ventas:
            if i[0] == vend:
                print(i)
                está = True
                break

        if not está:
            print("Su vendedor no está registrado en la base de datos.")
    

    if filtro == "2":
        articulo = input("Que artículo busca?:\n")
        art = formato(articulo)
        está = False

        for i in ventas:
            if i[1] == art:
                print(i)
                está = True
                break

        if not está:
            print("El artículo que usted busca no está registrado en la base de datos.")


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()




def leer_opcion(opciones):
    while (a := input("Opción: ")) not in opciones:
        print("Carácter no válido: vuelva a intentarlo")
    return a



def mostrar_menu(opciones):
    print("Eliga una opción: ")
    for i in sorted(opciones):
        print(f" {i}) {opciones[i][0]}")



def generar_menu(opciones, salida):
    opcion = None
    while opcion != salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()

    


def menu_principal():
    opciones = {
        "1": ["Registrar ventas", accion1],
        "2": ["Registrar llegada de artículos", accion2],
        "3": ["Consultar inventario", accion3],
        "4": ["Consultar ventas", accion4], 
        "5": ["Reportes de ventas", accion5],
        "6": ["Salir", salir],
    }

    generar_menu(opciones, "6")



menu_principal()
