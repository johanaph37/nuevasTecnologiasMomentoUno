import funciones

def menu():
    while True:
        print("\n MENÚ")
        print("1. Registrar Estudiante")
        print("2. Registrar Notas")
        print("3. Ver promedio")
        print("4. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            funciones.registrar_estudiante()
        elif opcion == "2":
            funciones.registrar_notas()
        elif opcion == "3":
            funciones.ver_promedio()
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción incorrecta")



if __name__ == "__main__":
    menu()