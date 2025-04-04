import MetodosGenerales
class Menu():
    def main():
        metodos_obj  = MetodosGenerales.MetodosGenerales()
        #menu 
        menu ="[1] Ingresar datos\n" \
              "[2] Prestar equipo\n" \
              "[3] Modificar datos\n" \
              "[4] Salir\n" \
                  
        while True: #es un ciclo
            print("Bienvenido al sistema de inventario")
            print("¿Que desea hacer?")
            print(menu)
            #manejo de errores
            while True:
                try:
                    opt = int(input()) #si es correcto sale del bucle sino pasa al except
                    break
                except ValueError:
                    print("Ingrese el dato correcto")
            
            
            if opt == 1:
                inventario_main = []
                inventario_main = metodos_obj.ingresar_datos()
            elif opt == 2:
                metodos_obj.prestar_equipo(inventario_main)
            elif opt == 3:
                metodos_obj.modificar_datos()
            elif opt == 4:
                print("Saliendo del sistema... Chao")
                break
            else:
                print("Opción no válida, intente nuevamente")
            

if __name__ == "__main__":
    Menu.main()