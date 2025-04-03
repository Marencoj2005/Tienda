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
                for i in inventario:
                    if i.get_referencia() == table_obj.get_referencia(): #accede al atrubuto del elemento
                        #emular un do-while
                        print("La referencia ya existe")
                        print("Ingrese nuevamente la referencia de la tablet")
                        table_obj.set_referencia(input())
                            
                        if table_obj.get_referencia() != i.get_referencia():
                            break                            
                    print("Ingrese la marca de la tablet")
                    table_obj.set_marca(input())
                    print("Ingrese el precio por hora de la tablet")
                    table_obj.set_precio(input())
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
            return inventario
    
    def prestar_equipo(self):
        return print("En Mantenimiento")
    
    def modificar_datos(self):
        return print("En Mantenimiento")
    