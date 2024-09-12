from iCrud import ICrud
from utilities import borrarPantalla, gotoxy, dibujar_cuadro
from basejson import JsonFile
import platform, time
import os

path, _ = os.path.split(os.path.abspath(__file__))

class CrudProfesores(ICrud):
    @staticmethod
    def create():
        borrarPantalla()
        dibujar_cuadro()
        gotoxy(2, 1)
        print("Registro de Profesor")
        gotoxy(2, 3)
        nombre = input("Ingrese el nombre del profesor: ")
        gotoxy(2, 4)
        apellido = input("Ingrese el apellido del profesor: ")
        gotoxy(2, 5)
        dni = input("Ingrese el DNI del profesor: ")
        gotoxy(2, 6)
        fecha_nacimiento = input("Ingrese la fecha de nacimiento del profesor (yyyy-mm-dd): ")
        gotoxy(2, 7)
        telefono = input("Ingrese el teléfono del profesor: ")
        gotoxy(2, 8)
        email = input("Ingrese el email del profesor: ")
        gotoxy(2, 9)
        direccion = input("Ingrese la dirección del profesor: ")
        gotoxy(2, 10)
        asignaturas = input("Ingrese la asignatura del profesor: ")
        gotoxy(2, 11)
        estado = input("Ingrese el estado del profesor (activo/inactivo): ").lower()
        
        json_file = JsonFile(path + '/archivosbases/profesores.json')
        profesores = json_file.read()

        for profesor in profesores:
            if profesor['dni'] == dni:
                print("Ya existe un profesor registrado con el mismo DNI.")
                if platform.system() == 'Windows':
                    input("Presione Enter para continuar...")
                else:
                    time.sleep(2)
                return
        
        last_id = max([profesor['id'] for profesor in profesores]) if profesores else 0
        new_id = last_id + 1
        
        nuevo_profesor = {
            "id": new_id,
            "nombre": nombre,
            "apellido": apellido,
            "dni": dni,
            "fecha_nacimiento": fecha_nacimiento,
            "telefono": telefono,
            "email": email,
            "direccion": direccion,
            "asignaturas": [{"id": 1, "Asignatura": asignaturas}],
            "estado": estado

        }
        
        profesores.append(nuevo_profesor)
        json_file.save(profesores)
        print("Profesor registrado exitosamente.")
        
        if platform.system() == 'Windows':
            input("Presione Enter para continuar...")
        else:
            time.sleep(2)
    
    @staticmethod
    def update():
        borrarPantalla()
        dibujar_cuadro()
        gotoxy(2, 1)
        print("Actualización de Profesor")
        gotoxy(2, 3)
        
        json_file_profesores = JsonFile(path + '/archivosbases/profesores.json')
        profesores = json_file_profesores.read()
        
        id_profesor = int(input("Ingrese el ID del profesor que desea actualizar: "))
        profesor = next((p for p in profesores if p['id'] == id_profesor), None)
        
        if profesor:
            print(f"Profesor actual: {profesor['nombre']}, Estado: {profesor['estado']}")
            nuevo_nombre = input("Ingrese el nuevo nombre del profesor (dejar vacío para no cambiar): ")
            nuevo_estado = input("Ingrese el nuevo estado (activo/inactivo) (dejar vacío para no cambiar): ")
            
            if nuevo_nombre:
                profesor['nombre'] = nuevo_nombre
            if nuevo_estado:
                profesor['estado'] = nuevo_estado.lower()
            
            # Mostrar asignaturas actuales y seleccionar nuevas si se desea
            print("Asignaturas actuales:")
            for asignatura in profesor['asignaturas']:
                print(f"ID: {asignatura['id']} - {asignatura['descripcion']}")
            
            modificar_asignaturas = input("¿Desea modificar las asignaturas asignadas al profesor? (s/n): ").lower()
            if modificar_asignaturas == 's':
                json_file_asignaturas = JsonFile(path + '/archivosbases/asignaturas.json')
                asignaturas = json_file_asignaturas.read()
                
                print("Asignaturas disponibles:")
                for asignatura in asignaturas:
                    print(f"ID: {asignatura['id']} - {asignatura['descripcion']}")
                id_asignaturas = input("Ingrese los IDs de las asignaturas a las que estará asignado el profesor, separadas por comas: ").split(',')
                id_asignaturas = [int(id_asig.strip()) for id_asig in id_asignaturas]
                
                asignaturas_seleccionadas = [asignatura for asignatura in asignaturas if asignatura['id'] in id_asignaturas]
                profesor['asignaturas'] = [{"id": a['id'], "descripcion": a['descripcion']} for a in asignaturas_seleccionadas]
            
            json_file_profesores.save(profesores)
            print("Profesor actualizado exitosamente.")
        else:
            print("Profesor no encontrado.")
        
        if platform.system() == 'Windows':
            input("Presione Enter para continuar...")
        else:
            time.sleep(2)
    
    @staticmethod
    def delete():
        borrarPantalla()
        dibujar_cuadro()
        gotoxy(2, 1)
        print("Eliminación de Profesor")
        gotoxy(2, 3)
        
        json_file_profesores = JsonFile(path + '/archivosbases/profesores.json')
        profesores = json_file_profesores.read()
        
        id_profesor = int(input("Ingrese el ID del profesor que desea eliminar: "))
        profesor = next((p for p in profesores if p['id'] == id_profesor), None)
        
        if profesor:
            print(f"Profesor encontrado: {profesor['nombre']}")
            confirmacion = input("¿Está seguro de que desea eliminar este profesor? (s/n): ").lower()
            if confirmacion == 's':
                profesores = [p for p in profesores if p['id'] != id_profesor]
                json_file_profesores.save(profesores)
                print("Profesor eliminado exitosamente.")
        else:
            print("Profesor no encontrado.")
        
        if platform.system() == 'Windows':
            input("Presione Enter para continuar...")
        else:
            time.sleep(2)

    @staticmethod
    def consult():
        borrarPantalla()
        dibujar_cuadro()
        gotoxy(2, 1)
        print("Consulta de Profesor")
        gotoxy(2, 3)
        
        json_file_profesores = JsonFile(path + '/archivosbases/profesores.json')
        profesores = json_file_profesores.read()
        
        id_profesor = int(input("Ingrese el ID del profesor que desea consultar: "))
        profesor = next((p for p in profesores if p['id'] == id_profesor), None)
        
        if profesor:
            print(f"Nombre: {profesor['nombre']} {profesor['apellido']}")
            print(f"DNI: {profesor['dni']}")
            print(f"Fecha de nacimiento: {profesor['fecha_nacimiento']}")
            print(f"Teléfono: {profesor['telefono']}")
            print(f"Email: {profesor['email']}")
            print(f"Dirección: {profesor['direccion']}")
            print(f"Estado: {profesor['estado']}")
            print("Asignaturas asignadas:")
            for asignatura in profesor['asignaturas']:
                print(f"ID: {asignatura['id']} - {asignatura['Asignatura']}")
        else:
            print("Profesor no encontrado.")
        
        if platform.system() == 'Windows':
            input("Presione Enter para continuar...")
        else:
            time.sleep(2)

            






