# CrudNotas.py
from iCrud import ICrud
from utilities import borrarPantalla, gotoxy, dibujar_cuadro
from basejson import JsonFile
import platform, time, os
from CalculoNota import CalculoNotas

path, _ = os.path.split(os.path.abspath(__file__))

class CrudNotas(ICrud):
    @staticmethod
    def create():
        borrarPantalla()
        dibujar_cuadro()
        gotoxy(2, 1)
        print("Registro de Notas")
        
        gotoxy(2, 3)
        nota1 = float(input("Ingrese la nota del Parcial 1: "))
        gotoxy(2, 4)
        nota2 = float(input("Ingrese la nota del Parcial 2: "))
        gotoxy(2, 5)
        examen = float(input("Ingrese la nota del Examen: "))

        # Cargar estudiantes, asignaturas y profesores para validar IDs
        json_file_estudiantes = JsonFile(path + '/archivosbases/estudiantes.json')
        estudiantes = json_file_estudiantes.read()
        json_file_asignaturas = JsonFile(path + '/archivosbases/asignaturas.json')
        asignaturas = json_file_asignaturas.read()
        json_file_profesores = JsonFile(path + '/archivosbases/profesores.json')
        profesores = json_file_profesores.read()
        
        # Validación de ID de estudiante
        gotoxy(2, 6)
        while True:
            id_estudiante = input("Ingrese el ID del estudiante: ")
            if any(int(e['id']) == int(id_estudiante) for e in estudiantes):  # Convertimos ambos a entero
                break
            else:
                print("ID de estudiante no válido. Inténtelo nuevamente.")

        # Validación de ID de asignatura
        gotoxy(2, 7)
        while True:
            id_asignatura = input("Ingrese el ID de la asignatura: ")
            if any(int(a['id']) == int(id_asignatura) for a in asignaturas):  # Convertimos ambos a entero
                break
            else:
                print("ID de asignatura no válido. Inténtelo nuevamente.")

        # Validación de ID de profesor
        gotoxy(2, 8)
        while True:
            id_profesor = input("Ingrese el ID del profesor: ")
            if any(int(p['id']) == int(id_profesor) for p in profesores):  # Convertimos ambos a entero
                break
            else:
                print("ID de profesor no válido. Inténtelo nuevamente.")
        
        json_file = JsonFile(path + '/archivosbases/notas.json')
        notas = json_file.read()
        
        last_id = max([nota['id'] for nota in notas]) if notas else 0
        new_id = last_id + 1
        
        promedio, estado = CalculoNotas.calcular_promedio(nota1, nota2, examen)
        
        nueva_nota = {
            "id": new_id,
            "parcial1": nota1,
            "parcial2": nota2,
            "examen": examen,
            "id_estudiante": id_estudiante,
            "id_asignatura": id_asignatura,
            "id_profesor": id_profesor,
            "estado": estado,
            "promedio": promedio
        }
        
        notas.append(nueva_nota)
        json_file.save(notas)
        print("Nota registrada exitosamente.")
        
        if platform.system() == 'Windows':
            input("Presione Enter para continuar...")
        else:
            time.sleep(2)



    @staticmethod
    def update():
        borrarPantalla()
        dibujar_cuadro()
        gotoxy(2, 1)
        print("Actualizar Nota")
        gotoxy(2, 3)
        id_nota = int(input("Ingrese el ID de la nota a actualizar: "))
        
        json_file = JsonFile(path + '/archivosbases/notas.json')
        notas = json_file.read()
        
        nota = next((n for n in notas if n['id'] == id_nota), None)
        if not nota:
            print("Nota no encontrada.")
            return
        
        gotoxy(2, 5)
        nuevo_parcial1 = input(f"Ingrese la nueva nota del Parcial 1 (actual: {nota['parcial1']}): ")
        nuevo_parcial2 = input(f"Ingrese la nueva nota del Parcial 2 (actual: {nota['parcial2']}): ")
        nuevo_examen = input(f"Ingrese la nueva nota del Examen (actual: {nota['examen']}): ")
        nuevo_estado = input(f"Ingrese el nuevo estado de la nota (actual: {nota['estado']}): ").lower()
        
        # Si no se introduce una nueva nota, mantenemos la existente
        parcial1 = float(nuevo_parcial1) if nuevo_parcial1 else nota['parcial1']
        parcial2 = float(nuevo_parcial2) if nuevo_parcial2 else nota['parcial2']
        examen = float(nuevo_examen) if nuevo_examen else nota['examen']
        
        # Actualizamos las notas y el estado
        promedio, estado = CalculoNotas.calcular_promedio(parcial1, parcial2, examen)
        nota['parcial1'] = parcial1
        nota['parcial2'] = parcial2
        nota['examen'] = examen
        nota['estado'] = estado
        nota['promedio'] = promedio
        
        json_file.save(notas)
        print("Nota actualizada correctamente.")
        
        if platform.system() == 'Windows':
            input("Presione Enter para continuar...")
        else:
            time.sleep(2)
            
    @staticmethod
    def delete():
        borrarPantalla()
        dibujar_cuadro()
        gotoxy(2, 1)
        print("Eliminar Nota")
        gotoxy(2, 3)
        id_nota = int(input("Ingrese el ID de la nota a eliminar: "))
        
        json_file = JsonFile(path + '/archivosbases/notas.json')
        notas = json_file.read()
        
        nota = next((n for n in notas if n['id'] == id_nota), None)
        if not nota:
            print("Nota no encontrada.")
            return
        
        notas.remove(nota)
        json_file.save(notas)
        print("Nota eliminada correctamente.")
        
        # Llama al método de CalculoNotas para actualizar el promedio
        CalculoNotas.calcular_promedio(nota['id_estudiante'])  # Cambia esto por el método adecuado
        
        if platform.system() == 'Windows':
            input("Presione Enter para continuar...")
        else:
            time.sleep(2)
    
    @staticmethod
    def consult():
        borrarPantalla()
        dibujar_cuadro()
        gotoxy(2, 1)
        print("Consulta de Notas")
        gotoxy(2, 3)
        id_estudiante = input("Ingrese el ID del estudiante para consultar: ")
        
        json_file_notas = JsonFile(path + '/archivosbases/notas.json')
        notas = json_file_notas.read()
        
        json_file_estudiantes = JsonFile(path + '/archivosbases/estudiantes.json')
        estudiantes = json_file_estudiantes.read()
        
        if not notas:
            print("No hay notas registradas.")
            return

        # Filtrar las notas del estudiante ingresado
        notas_estudiante = [nota for nota in notas if nota['id_estudiante'] == id_estudiante]
        
        if not notas_estudiante:
            print("No se encontraron notas para el estudiante con ID:", id_estudiante)
            return
        
        estudiantes_dict = {e['id']: f"{e['nombre']} {e['apellido']}" for e in estudiantes}
        
        for nota in notas_estudiante:
            nombre_estudiante = estudiantes_dict.get(nota['id_estudiante'], "Desconocido")
            print(f"ID: {nota['id']} | Parcial 1: {nota['parcial1']} | Parcial 2: {nota['parcial2']} | Examen: {nota['examen']} | Promedio: {nota['promedio']} | Estado: {nota['estado']} | Estudiante: {id_estudiante} | ID Asignatura: {nota['id_asignatura']} | ID Profesor: {nota['id_profesor']}")
        
        if platform.system() == 'Windows':
            input("Presione Enter para continuar...")
        else:
            time.sleep(2)
