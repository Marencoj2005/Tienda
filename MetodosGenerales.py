import Tablet, Computador

class MetodosGenerales():
    def __init__(self):
        pass
    
    def ingresar_datos(self):
        inventario = []
        while True:
            print("¿Que equipo desea guardar en el inventario?")
            print("[1] Computador")
            print("[2] Tablet")
            print("[3] Guardar y Salir")
            while True:
                try:
                    seleccion = int(input())
                    break
                except ValueError:
                    print("Opción no válida, intente nuevamente")
            #manejo de error
            if seleccion == 1:
                computador_obj = Computador.Computador()
                print("Ingrese la referencia del computador")
                computador_obj.set_referencia(input())
                print("Ingrese la marca del computador")
                computador_obj.set_marca(input())
                print("Ingrese el tamaño de la RAM del computador")
                computador_obj.set_tamano_ram(input())
                print("Ingrese el precio por hora del computador")
                computador_obj.set_precio_hora(input())
                    
                inventario.append(computador_obj) #almacena en la pila
                print("Computador guardado en el inventario")
                    
            elif seleccion == 2:
                table_obj = Tablet.Tablet()
                print("Ingrese la referencia de la tablet")
                table_obj.set_referencia(input())
                # for i in inventario:
                #     if i.get_referencia() == table_obj.get_referencia(): #accede al atrubuto del elemento
                #         #while
                #         while True:
                #             print("La referencia ya existe")
                #             print("Ingrese nuevamente la referencia de la tablet")
                #             table_obj.set_referencia(input())
                #             if table_obj.get_referencia() != i.get_referencia():
                #                 break                            
                              
                print("Ingrese la marca de la tablet") # se está saliendo del bucle for
                table_obj.set_marca(input())
                print("Ingrese el precio por hora de la tablet")
                table_obj.set_precio_hora(input())
                table_obj.set_disponible(True)
                inventario.append(table_obj)
                print("Tablet guardada en el inventario")
                    
            elif seleccion == 3:
                if len(inventario) != 0:
                    print("Inventario guardado")
                #     print("¿Desea ver el invetario?")
                #     print("[1] Si\n" \
                #               "[2] No")
                # while True:
                #     try:
                #         mostrar = int(input())
                #         break
                #     except ValueError:
                #             print("Opción no válida, intente nuevamente")
                else:          
                    print("No se registro ningun equipo")
                break #rompe el ciclo para salir del metodo y retorne el inventario
        return inventario
    
    def prestar_equipo(self, inventario):
        cola_prestamos = []
        #ingrese los datos del equipo a presta
        #Nesesito verificar si hay equipos disponibles
        while True:
            if len(inventario) == 0:
                print("NO HAY EQUIPOS DISPONIBLES")
            else:
                print("")
                print("Estos equipos están disponibles")
                for item in inventario:
                    print(item)
                print("")
                print("Seleccione la referencia a prestar")
                referencia_prestamo = input()
                for item in inventario: #accede al __str__ de las clases para imprimir
                    #verifica si el equipo está disponible
                    if referencia_prestamo == item.get_referencia():
                        print("Nombre de la persona al que se la va a prestar el equipo")
                        item.set_nombre_usuario(input())
                        item.set_disponible(False)
                        cola_prestamos.append(item)
                        print("Equipo prestado")
                        print(item)
                if len(inventario) != 0:
                    print("Desea Prestar otro equipo? \n" \
                          "[1] Si\n" \
                          "[2] No")
                    while True: #manejara el error
                        try:
                            opt = int(input())
                            break #rome el ciclo
                        except ValueError:
                            print("Opción no válida, intente nuevamente")
                        
                        if opt == 1:
                            for item in inventario: #accede al __str__ de las clases para imprimir
                                 #verifica si el equipo está disponible
                                if referencia_prestamo == item.get_referencia():
                                    print("Nombre de la persona al que se la va a prestar el equipo")
                                    item.set_nombre_usuario(input())
                                    item.set_disponible(False)
                                    cola_prestamos.append(item)
                                    print("Equipo prestado")
                                    print(item)
                        else:
                            print("No se prestara otro equipo")
                            break
                else:
                    print("No hay equipos disponibles para prestar")
                    break
                
        return inventario, cola_prestamos
    
    def modificar_datos(self, inventario, cola_prestamos):
        while True:
            print("¿Que equipo desea modificar?")
            print("[1] Computador")
            print("[2] Tablet")
            print("[3] Salir")
            while True: #maneja el error de la opción
                try:
                    opt = int(input())
                    break
                except ValueError:
                    print("Opción no válida, intente nuevamente")
            if opt == 1:
                print("Que desea hacer")
                print("[1] Cambiar el nombre del usuario")
                print("[2] Cambiar el precio por hora")
                print("[3] Cambiar la referencia")
                print("[4] Cambiar la marca")
                print("[6] Se devolvió un equipo")
                print("[7] Salir")
                
                opt = int(input())
                #manejo de errores
                while True: #maneja el error de la opción
                    try:
                        opt = int(input())
                        break
                    except ValueError:
                        print("Opción no válida, intente nuevamente")
                if opt == 1:
                    print("Ingrese la referencia del equipo")
                    referencia = input()
                    for item in inventario:
                        if referencia == item.get_referencia():
                            print("Ingrese el nuevo nombre del usuario")
                            item.set_nombre_usuario(input())
                            print("Nombre de usuario cambiado")
                            print(item)
                if opt == 2:
                    print("Ingrese la referencia del equipo")
                    referencia = input()
                    for item in inventario:
                        if referencia == item.get_referencia():
                            print("Ingrese el nuevo precio por hora")
                            item.set_precio_hora(input())
                            print("Precio cambiado")
                            print(item)
                
                elif opt == 3:
                        print("Ingrese la referencia del equipo")
                        referencia = input()
                        for item in inventario:
                            if referencia == item.get_referencia():
                                print("Ingrese la nueva referencia")
                                item.set_referencia(input())
                                print("Referencia cambiada")
                                print(item)
                elif opt == 4:
                        print("Ingrese la referencia del equipo")
                        referencia = input()
                        for item in inventario:
                            if referencia == item.get_referencia():
                                print("Ingrese la nueva marca")
                                item.set_marca(input())
                                print("Marca cambiada")
                                print(item)
                elif opt == 5:
                        print("Ingrese la referencia del equipo")
                        referencia = input()
                        for item in inventario:
                            if referencia == item.get_referencia():
                                print("Ingrese el nuevo tamaño de la RAM")
                                item.set_tamano_ram(input())
                                print("Tamaño de RAM cambiado")
                                print(item)
                elif opt == 6:
                        print("Ingrese la referencia del equipo")
                        referencia = input()
                        for item in inventario:
                            if referencia == item.get_referencia():
                                print("Ingrese el nuevo estado de disponibilidad (True/False)")
                                item.set_disponible(input().lower() == 'true')
                                print("Disponibilidad cambiada")
                                print(item)
                elif opt == 7:
                        print("Ingrese la referencia del equipo")
                        referencia = input()
                        for item in inventario:
                            if referencia == item.get_referencia():
                                print("Ingrese el nuevo nombre del usuario")
                                item.set_nombre_usuario(input())
                                print("Nombre de usuario cambiado")
                                print(item)
                elif opt == 8:
                        print("Ingrese la referencia del equipo")
                        referencia = input()
                        for item in inventario:
                            if referencia == item.get_referencia():
                                print("Ingrese el nuevo precio por hora")
                                item.set_precio_hora(input())
                                print("Precio por hora cambiado")
                                print(item)
                elif opt == 9:
                        print("Saliendo del menú de modificación")
                        break
            elif 2:
                print("Que desea hacer")
                print("[1] Cambiar el nombre del usuario")
                print("[2] Cambiar el precio por hora")
                print("[3] Cambiar la referencia")
                print("[4] Cambiar la marca")
                print("[5] Cambiar el tamaño de la RAM")
                print("[6] Se devolvió un equipo")
                print("[7] Salir")
                
                opt = int(input())
                #manejo de errores
                while True:
                    try:
                        opt = int(input())
                        break
                    except ValueError:
                        print("Opción no válida, intente nuevamente")
                if opt == 1:
                    print("Ingrese la referencia de la tablet")
                    referencia = input()
                    for item in inventario:
                        if referencia == item.get_referencia():
                            print("Ingrese el nuevo nombre del usuario")
                            item.set_nombre_usuario(input())
                            print("Nombre de usuario cambiado")
                            print(item)
                elif opt == 2:
                    print("Ingrese la referencia de la tablet")
                    referencia = input()
                    for item in inventario:
                        if referencia == item.get_referencia():
                            print("Ingrese el nuevo precio por hora")
                            item.set_precio_hora(input())
                            print("Precio cambiado")
                            print(item)
                elif opt == 3:
                    print("Ingrese la referencia de la tablet")
                    referencia = input()
                    for item in inventario:
                        if referencia == item.get_referencia():
                            print("Ingrese la nueva referencia")
                            item.set_referencia(input())
                            print("Referencia cambiada")
                            print(item)
                elif opt == 4:
                    print("Ingrese la referencia de la tablet")
                    referencia = input()
                    for item in inventario:
                        if referencia == item.get_referencia():
                            print("Ingrese la nueva marca")
                            item.set_marca(input())
                            print("Marca cambiada")
                            print(item)
                elif opt == 6:
                    print("Ingrese la referencia de la tablet")
                    referencia = input()
                    cola_auxiliar=[]
                    for item in cola_prestamos:
                        if referencia == item.get_referencia():
                            inventario.append(cola_prestamos.pop(0)) #agrega la tablet a la lista de inventario
                            item.set_disponible(True)
                            item.set_nombre_usuario(None)
                            print("Disponibilidad cambiada")
                        else:
                            cola_auxiliar.append(cola_prestamos.pop(0))
                elif opt == 7:
                    print("Saliendo del menú de modificación")
                    break
            else:
                print("Chao")
                break
            
            return inventario
                
            