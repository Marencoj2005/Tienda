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
                
                while True:
                   objeto_inventario = inventario.pop(0) #desapila el objeto
                   if objeto_inventario.get_referencia() == table_obj.get_referencia():
                       print("Esta referencia ya existe, ingrese una diferente")
                       table_obj.set_referencia(input())
                   else:
                        break
                                     
                              
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
    
    def prestar_equipo(self, inventario, cola_prestamos):
        while True:
            print("\n--- MENÚ DE PRÉSTAMOS ---")
            if not inventario:
                print("¡NO HAY EQUIPOS DISPONIBLES!")
                return inventario, cola_prestamos
            
            # Mostrar equipos disponibles
            print("\nEquipos disponibles:")
            for idx, item in enumerate(inventario, 1):
                if item.get_disponible():
                    print(f"\n[{idx}] {item}")
            
            # Selección de referencia
            referencia = input("\nIngrese la referencia del equipo a prestar (o '0' para salir): ").strip()
            if referencia == '0':
                print("Saliendo del menú de préstamos...")
                return inventario, cola_prestamos
            
            # Buscar equipo
            equipo_encontrado = None
            for item in reversed(inventario):
                if item.get_referencia() == referencia and item.get_disponible():
                    equipo_encontrado = item
                    break
            
            if not equipo_encontrado:
                print("\n¡Error! Referencia no encontrada o equipo no disponible")
                continue
            
            # Proceso de préstamo
            print("\nDATOS DEL PRÉSTAMO")
            nombre = input("Nombre del receptor: ").strip()
            while not nombre:
                print("¡El nombre no puede estar vacío!")
                nombre = input("Nombre del receptor: ").strip()
            
            # Actualizar datos
            equipo_encontrado.set_nombre_usuario(nombre)
            equipo_encontrado.set_disponible(False)
            inventario.remove(equipo_encontrado)
            cola_prestamos.append(equipo_encontrado)
            
            print("\n¡Préstamo exitoso!")
            print(equipo_encontrado)
            
            # Opción para nuevo préstamo
            while True:
                continuar = input("\n¿Desea hacer otro préstamo? (S/N): ").strip().upper()
                if continuar in ['S', 'N']:
                    break
                print("¡Opción inválida! Solo S/N")
            
            if continuar == 'N':
                print("Regresando al menú principal...")
                return inventario, cola_prestamos
    
    def modificar_equipo(self ,inventario, cola_prestamos):
        while True:
            print("\n¿Qué equipo desea modificar?")
            print("[1] Computador")
            print("[2] Tablet")
            print("[3] Salir")
            
            # Manejar entrada del menú principal
            while True:
                try:
                    opt = int(input("Opción: "))
                    break
                except ValueError:
                    print("Opción no válida, intente nuevamente.")
            
            if opt == 1:
                while True:  # Submenú de Computador
                    print("\n¿Qué desea hacer?")
                    print("[1] Cambiar el nombre del usuario")
                    print("[2] Cambiar el precio por hora")
                    print("[3] Cambiar la marca")
                    print("[4] Cambiar la RAM")
                    print("[5] Se devolvió un equipo")
                    print("[6] Volver al menú principal")
                    
                    # Manejar entrada del submenú
                    while True:
                        try:
                            sub_opt = int(input("Opción: "))
                            if 1 <= sub_opt <= 6:
                                break
                            else:
                                print("Opción fuera de rango.")
                        except ValueError:
                            print("Opción no válida.")
                    
                    if sub_opt == 6:
                        break  # Salir del submenú
                    
                    referencia = input("Ingrese la referencia del equipo: ")
                    encontrado = False
                    
                    # Buscar el equipo en inventario
                    for item in reversed(inventario):
                        if item.get_referencia() == referencia:
                            encontrado = True
                            if sub_opt == 1:
                                nuevo_nombre = input("Ingrese el nuevo nombre del usuario: ")
                                item.set_nombre_usuario(nuevo_nombre)
                                print("Nombre actualizado.")
                            elif sub_opt == 2:
                                while True:
                                    try:
                                        nuevo_precio = float(input("Nuevo precio por hora: "))
                                        item.set_precio_hora(nuevo_precio)
                                        break
                                    except ValueError:
                                        print("Debe ingresar un número válido.")
                            elif sub_opt == 3:
                                nueva_marca = input("Ingrese la nueva marca: ")
                                item.set_marca(nueva_marca)
                            elif sub_opt == 4:
                                while True:
                                    try:
                                        nueva_ram = int(input("Nuevo tamaño de RAM (GB): "))
                                        item.set_tamano_ram(nueva_ram)
                                        break
                                    except ValueError:
                                        print("Debe ingresar un número entero.")
                            elif sub_opt == 5:
                                # Buscar en préstamos
                                encontrado_prestamo = False
                                temp = []
                                while cola_prestamos:
                                    equipo = cola_prestamos.pop(0)
                                    if equipo.get_referencia() == referencia:
                                        inventario.append(equipo)
                                        encontrado_prestamo = True
                                        break
                                    else:
                                        temp.append(equipo)
                                cola_prestamos.extend(temp)
                                if encontrado_prestamo:
                                    print("Equipo devuelto al inventario.")
                                else:
                                    print("Equipo no encontrado en préstamos.")
                            
                            print(item)  # Mostrar cambios
                            break  # Salir del for
                    
                    if not encontrado:
                        print("Equipo no encontrado en inventario.")
            
            elif opt == 2:
                while True:  # Submenú de Tablet
                    print("\n¿Qué desea hacer?")
                    print("[1] Cambiar el nombre del usuario")
                    print("[2] Cambiar el precio por hora")
                    print("[3] Cambiar la marca")
                    print("[4] Se devolvió un equipo")
                    print("[5] Volver al menú principal")
                    
                    # Manejar entrada del submenú
                    while True:
                        try:
                            sub_opt = int(input("Opción: "))
                            if 1 <= sub_opt <= 5:
                                break
                            else:
                                print("Opción fuera de rango.")
                        except ValueError:
                            print("Opción no válida.")
                    
                    if sub_opt == 5:
                        break  # Salir del submenú
                    
                    referencia = input("Ingrese la referencia de la tablet: ")
                    encontrado = False
                    
                    # Buscar el equipo en inventario
                    for item in reversed(inventario):
                        if item.get_referencia() == referencia:
                            encontrado = True
                            if sub_opt == 1:
                                nuevo_nombre = input("Ingrese el nuevo nombre del usuario: ")
                                item.set_nombre_usuario(nuevo_nombre)
                            elif sub_opt == 2:
                                while True:
                                    try:
                                        nuevo_precio = float(input("Nuevo precio por hora: "))
                                        item.set_precio_hora(nuevo_precio)
                                        break
                                    except ValueError:
                                        print("Debe ingresar un número válido.")
                            elif sub_opt == 3:
                                nueva_marca = input("Ingrese la nueva marca: ")
                                item.set_marca(nueva_marca)
                            elif sub_opt == 4:
                                # Buscar en préstamos
                                encontrado_prestamo = False
                                temp = []
                                while cola_prestamos:
                                    equipo = cola_prestamos.pop(0)
                                    if equipo.get_referencia() == referencia:
                                        inventario.append(equipo)
                                        encontrado_prestamo = True
                                        break
                                    else:
                                        temp.append(equipo)
                                cola_prestamos.extend(temp)
                                if encontrado_prestamo:
                                    print("Equipo devuelto al inventario.")
                                else:
                                    print("Equipo no encontrado en préstamos.")
                            
                            print(item)  # Mostrar cambios
                            break  # Salir del for
                    
                    if not encontrado:
                        print("Tablet no encontrada en inventario.")
            
            elif opt == 3:
                print("Saliendo del sistema...")
                break
            
            else:
                print("Opción inválida, intente nuevamente.")
        
        return inventario