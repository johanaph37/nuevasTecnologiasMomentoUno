from diccionario import estudiantes

def registrar_estudiante():
    id_estudiante = input("Ingrese el la identificación del estudiante: ")
    nombre = input("Ingrese el nombre del estudiante: ")

    estudiantes[id_estudiante] = {
    "nombre": nombre,
    "nota1": 0.0,
    "nota2": 0.0

    }

    print(f"Estudiante {nombre} registrado con éxito")


def registrar_notas():
    id_busqueda = input("Ingrese la identificación de estudiante para registrar las notas: ")

    if id_busqueda in estudiantes:
        nota1 = float(input("Ingrese la nota 1: "))
        nota2 = float(input("Ingrese la nota 2: "))

        estudiantes [id_busqueda]["nota1"] = nota1
        estudiantes [id_busqueda]["nota2"] = nota2

        print("Notas actualizadas correctamente")
    else:
        print("El estudiante no se encuentra registrado")

def ver_promedio():
    id_busqueda = input("Ingrese la identifcación de estudiante para ver e promedio: ")
        
    if id_busqueda in estudiantes:
        estudiante = estudiantes[id_busqueda]
        nota1 = estudiante["nota1"]
        nota2 = estudiante["nota2"]

        promedio = (nota1 + nota2) / 2

        print(f"\nEstudiante: {estudiante['nombre']}")
        print(f"\nEl promedio es: {promedio:.2f}")
    else:
         print("El estudiante no está registrado")

        
