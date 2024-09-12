from iCrud import ICrud
from utilities import borrarPantalla, gotoxy, dibujar_cuadro
from basejson import JsonFile
import platform, time
import os

path, _ = os.path.split(os.path.abspath(__file__))


class CrudEstudiante(ICrud):
    @staticmethod
    def create():
        borrarPantalla()
        dibujar_cuadro()
        gotoxy(2, 1)
        print("Registro de Estudiante")
        gotoxy(2, 3)
        nombre = input("Ingrese el nombre del estudiante: ")
        gotoxy(2, 4)
        apellido = input("Ingrese el apellido del estudiante: ")
        gotoxy(2, 5)
        dni = input("Ingrese el DNI del estudiante: ")
        gotoxy(2, 6)
        fecha_nacimiento = input("Ingrese la fecha de nacimiento del estudiante (yyyy-mm-dd): ")
        gotoxy(2, 7)
        telefono = input("Ingrese el teléfono del estudiante: ")
        gotoxy(2, 8)
        email = input("Ingrese el email del estudiante: ")
        gotoxy(2, 9)
        direccion = input("Ingrese la dirección del estudiante: ")
        gotoxy(2, 10)
        estado = input("Ingrese el estado del estudiante (activo/inactivo): ").lower()
        
        json_file = JsonFile(path + '/archivosbases/estudiantes.json')
        estudiantes = json_file.read()
        
        for estudiante in estudiantes:
            if estudiante['dni'] == dni:
                print("Ya existe un estudiante registrado con el mismo DNI.")
                if platform.system() == 'Windows':
                    input("Presione Enter para continuar...")
                else:
                    time.sleep(2)
                return
            

        last_id = max([estudiante['id'] for estudiante in estudiantes]) if estudiantes else 0
        new_id = last_id + 1
        
        nuevo_estudiante = {
        "id": new_id,
        "nombre": nombre,
        "apellido": apellido,
        "dni": dni,
        "fecha_nacimiento": fecha_nacimiento,
        "telefono": telefono,
        "email": email,
        "direccion": direccion,
        "estado": estado,
        "asignaturas": []
    }
        
        estudiantes.append(nuevo_estudiante)
        json_file.save(estudiantes)
        print("Estudiante registrado exitosamente.")
        
        if platform.system() == 'Windows':
            input("Presione Enter para continuar...")
        else:
            time.sleep(2)
    @staticmethod
    def agregar_asignatura():
        while True:
            borrarPantalla()
            dibujar_cuadro()
            gotoxy(2, 1)
            print("Agregar Asignatura a Estudiante")
            
            # Leer la lista de asignaturas
            json_file_asignaturas = JsonFile(path + '/archivosbases/asignaturas.json')
            asignaturas = json_file_asignaturas.read()
            
            gotoxy(2, 3)
            id_estudiante = int(input("Ingrese el ID del estudiante al que desea agregar una asignatura: "))
            
            json_file_estudiantes = JsonFile(path + '/archivosbases/estudiantes.json')
            estudiantes = json_file_estudiantes.read()
            
            estudiante = next((e for e in estudiantes if e['id'] == id_estudiante), None)
            if not estudiante:
                print("Estudiante no encontrado.")
                input("Presione Enter para continuar...")
                return
            
            while True:
                # Limpiar la parte de la pantalla donde se muestran las asignaturas y las opciones
                borrarPantalla()
                dibujar_cuadro()
                gotoxy(2, 1)
                print("Agregar Asignatura a Estudiante")
                
                gotoxy(2, 3)
                id_estudiante = int(input("Ingrese el ID del estudiante al que desea agregar una asignatura: "))
                
                # Mostrar asignaturas disponibles
                gotoxy(2, 5)
                print("Asignaturas disponibles:")
                
                for i, asignatura in enumerate(asignaturas, start=6):
                    gotoxy(2, i)
                    print(f"ID: {asignatura['id']}, Nombre: {asignatura['Asignatura']}")
                
                gotoxy(2, len(asignaturas) + 7)
                id_asignatura = int(input("Ingrese el ID de la asignatura que desea agregar: "))
                
                # Buscar el nombre de la asignatura
                asignatura_seleccionada = next((a for a in asignaturas if a['id'] == id_asignatura), None)
                if not asignatura_seleccionada:
                    print("Asignatura no encontrada.")
                    continue
                
                nombre_asignatura = asignatura_seleccionada['Asignatura']
                
                # Verificar si la asignatura ya está registrada
                if 'asignaturas' in estudiante and nombre_asignatura in estudiante['asignaturas']:
                    print(f"Ya está matriculado en la asignatura '{nombre_asignatura}'.")
                else:
                    # Asegúrate de que el campo 'asignaturas' existe
                    if 'asignaturas' not in estudiante:
                        estudiante['asignaturas'] = []
                    
                    # Agregar la asignatura por nombre
                    estudiante['asignaturas'].append(nombre_asignatura)
                    print(f"Asignatura '{nombre_asignatura}' agregada exitosamente al estudiante.")
                    time.sleep(2)
                    borrarPantalla()
                    
                # Preguntar si desea agregar más asignaturas
                while True:
                    respuesta = input("¿Desea agregar más asignaturas? (s/n): ")
                    if respuesta.lower() not in ['s', 'n']:
                        print("Respuesta inválida. Por favor, ingrese 's' o 'n'.")
                        continue
                    break
                if respuesta.lower() == 'n':
                    # Guardar los cambios y regresar al menú principal de estudiantes
                    json_file_estudiantes.save(estudiantes)
                    return  # Salir de la función y volver al menú principal
        
        





    @staticmethod
    def update():
        borrarPantalla()
        dibujar_cuadro()
        gotoxy(2, 1)
        print("Actualizar Estudiante")
        gotoxy(2, 3)
        id_estudiante = int(input("Ingrese el ID del estudiante a actualizar: "))
        
        json_file = JsonFile(path + '/archivosbases/estudiantes.json')
        estudiantes = json_file.read()
        
        estudiante = next((e for e in estudiantes if e['id'] == id_estudiante), None)
        if not estudiante:
            print("Estudiante no encontrado.")
            return
        
        gotoxy(2, 5)
        nuevo_nombre = input(f"Ingrese el nuevo nombre del estudiante (actual: {estudiante['nombre']}): ")
        nuevo_apellido = input(f"Ingrese el nuevo apellido del estudiante (actual: {estudiante['apellido']}): ")
        nuevo_dni = input(f"Ingrese el nuevo DNI del estudiante (actual: {estudiante['dni']}): ")
        nueva_fecha_nacimiento = input(f"Ingrese la nueva fecha de nacimiento del estudiante (actual: {estudiante['fecha_nacimiento']}): ")
        nuevo_telefono = input(f"Ingrese el nuevo teléfono del estudiante (actual: {estudiante['telefono']}): ")
        nuevo_email = input(f"Ingrese el nuevo email del estudiante (actual: {estudiante['email']}): ")
        nueva_direccion = input(f"Ingrese la nueva dirección del estudiante (actual: {estudiante['direccion']}): ")
        nuevo_estado = input(f"Ingrese el nuevo estado del estudiante (activo/inactivo, actual: {estudiante['estado']}): ").lower()
        
        estudiante['nombre'] = nuevo_nombre if nuevo_nombre else estudiante['nombre']
        estudiante['apellido'] = nuevo_apellido if nuevo_apellido else estudiante['apellido']
        estudiante['dni'] = nuevo_dni if nuevo_dni else estudiante['dni']
        estudiante['fecha_nacimiento'] = nueva_fecha_nacimiento if nueva_fecha_nacimiento else estudiante['fecha_nacimiento']
        estudiante['telefono'] = nuevo_telefono if nuevo_telefono else estudiante['telefono']
        estudiante['email'] = nuevo_email if nuevo_email else estudiante['email']
        estudiante['direccion'] = nueva_direccion if nueva_direccion else estudiante['direccion']
        estudiante['estado'] = nuevo_estado
        if nuevo_estado == "inactivo":
            estudiante['estado'] = nuevo_estado
        else:
            estudiante['estado'] = "activo"
    
        json_file.save(estudiantes)
        print("Estudiante actualizado correctamente.")
        
        input("Presione Enter para continuar...")
        time.sleep(2)

    @staticmethod   
    def delete():
        borrarPantalla()
        dibujar_cuadro()
        gotoxy(2, 1)
        print("Eliminar Estudiante")
        gotoxy(2, 3)
        id_estudiante = int(input("Ingrese el ID del estudiante a eliminar: "))
        
        json_file = JsonFile(path + '/archivosbases/estudiantes.json')
        estudiantes = json_file.read()
        
        estudiante = next((e for e in estudiantes if e['id'] == id_estudiante), None)
        if not estudiante:
            print("Estudiante no encontrado.")
            return
        
        gotoxy(2, 5)
        confirmacion = input(f"¿Está seguro de que desea eliminar al estudiante {estudiante['nombre']} {estudiante['apellido']}? (s/n): ").lower()
        if confirmacion == 's':
            estudiantes = [e for e in estudiantes if e['id'] != id_estudiante]
            json_file.save(estudiantes)
            print("Estudiante eliminado exitosamente.")
        
        input("Presione Enter para continuar...")
        time.sleep(2)

    @staticmethod
    def consult_all():
        borrarPantalla()
        dibujar_cuadro()
        gotoxy(2, 1)
        print("Consulta de Estudiantes")
        gotoxy(2, 3)
        
        json_file = JsonFile(path + '/archivosbases/estudiantes.json')
        estudiantes = json_file.read()
        
        # Definir posiciones para cada columna
        pos_id = 2
        pos_nombre = pos_id + 6
        pos_apellido = pos_nombre + 20
        pos_dni = pos_apellido + 20
        pos_fecha_nacimiento = pos_dni + 15
        pos_telefono = pos_fecha_nacimiento + 15
        pos_email = pos_telefono + 12
        pos_direccion = pos_email + 30
        pos_estado = pos_direccion + 30

        # Imprimir encabezados
        gotoxy(pos_id, 5)
        print("ID", end="")
        gotoxy(pos_nombre, 5)
        print("Nombre", end="")
        gotoxy(pos_apellido, 5)
        print("Apellido", end="")
        gotoxy(pos_dni, 5)
        print("DNI", end="")
        gotoxy(pos_fecha_nacimiento, 5)
        print("Fecha Nac.", end="")
        gotoxy(pos_telefono, 5)
        print("Teléfono", end="")
        gotoxy(pos_email, 5)
        print("Email", end="")
        gotoxy(pos_direccion, 5)
        print("Dirección", end="")
        gotoxy(pos_estado, 5)
        print("Estado")

        # Imprimir línea separadora
        gotoxy(2, 6)
        print("=" * (pos_estado + 20 - 2))  # Ajusta el ancho total según sea necesario

        # Imprimir datos de los estudiantes
        for i, estudiante in enumerate(estudiantes):
            gotoxy(pos_id, 7 + i)
            print(str(estudiante['id']).ljust(6), end="")
            gotoxy(pos_nombre, 7 + i)
            print(estudiante['nombre'].ljust(20), end="")
            gotoxy(pos_apellido, 7 + i)
            print(estudiante['apellido'].ljust(20), end="")
            gotoxy(pos_dni, 7 + i)
            print(estudiante['dni'].ljust(20), end="")
            gotoxy(pos_fecha_nacimiento, 7 + i)
            print(estudiante['fecha_nacimiento'].ljust(15), end="")
            gotoxy(pos_telefono, 7 + i)
            print(estudiante['telefono'].ljust(15), end="")
            gotoxy(pos_email, 7 + i)
            print(estudiante['email'].ljust(30), end="")
            gotoxy(pos_direccion, 7 + i)
            print(estudiante['direccion'].ljust(30), end="")
            gotoxy(pos_estado, 7 + i)
            print(estudiante['estado'].ljust(20))

        input("Presione Enter para continuar...")
        time.sleep(2)
