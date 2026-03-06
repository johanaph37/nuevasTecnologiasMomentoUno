def ver_aprobacion():
    id_busqueda = input("Ingrese la identificación del estudiante para verificar aprobación: ")

    if id_busqueda in estudiantes:
        estudiante = estudiantes[id_busqueda]
        nota1 = estudiante["nota1"]
        nota2 = estudiante["nota2"]

        promedio = (nota1 + nota2) / 2

        if promedio >= 3.0:
            print(f"\nEstudiante: {estudiante['nombre']}")
            print(f"Promedio: {promedio:.2f}")
            print("Estado: APRUEBA")
        else:
            print(f"\nEstudiante: {estudiante['nombre']}")
            print(f"Promedio: {promedio:.2f}")
            print("Estado: NO APRUEBA")
    else:
        print("El estudiante no está registrado")