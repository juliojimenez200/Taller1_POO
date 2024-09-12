from iCrud import ICrud
from utilities import borrarPantalla, gotoxy, dibujar_cuadro
from basejson import JsonFile
import platform, time
import os
from datetime import datetime
path, _ = os.path.split(os.path.abspath(__file__))

class CrudMatricula(ICrud):
    @staticmethod
    def create():
        borrarPantalla()
        dibujar_cuadro()
        gotoxy(2, 1)
        print("Registro de Matrícula")
        
        # Cargar datos necesarios
        json_file_estudiantes = JsonFile(path + '/archivosbases/estudiantes.json')
        estudiantes = json_file_estudiantes.read()
        json_file_cursos = JsonFile(path + '/archivosbases/cursos.json')
        cursos = json_file_cursos.read()
        json_file_periodos = JsonFile(path + '/archivosbases/periodos.json')
        periodos = json_file_periodos.read()
        json_file_profesores = JsonFile(path + '/archivosbases/profesores.json')
        profesores = json_file_profesores.read()
        json_file_asignaturas = JsonFile(path + '/archivosbases/asignaturas.json')
        asignaturas = json_file_asignaturas.read()
        
        # Validación de ID de estudiante
        gotoxy(2, 3)
        while True:
            id_estudiante = input("Ingrese el ID del estudiante: ")
            estudiante = next((e for e in estudiantes if int(e['id']) == int(id_estudiante)), None)
            if estudiante:
                nombre_estudiante = f"{estudiante['nombre']} {estudiante['apellido']}"
                break
            else:
                print("ID de estudiante no válido. Inténtelo nuevamente.")

        # Validación de ID de curso
        gotoxy(2, 4)
        while True:
            id_curso = input("Ingrese el ID del curso: ")
            curso = next((c for c in cursos if int(c['id']) == int(id_curso)), None)
            if curso:
                nombre_curso = curso['Curso']
                break
            else:
                print("ID de curso no válido. Inténtelo nuevamente.")
        
        # Validación de ID de periodo
        gotoxy(2, 5)
        while True:
            id_periodo = input("Ingrese el ID del periodo: ")
            periodo = next((p for p in periodos if int(p['id']) == int(id_periodo)), None)
            if periodo:
                nombre_periodo = periodo['Periodo']
                break
            else:
                print("ID de periodo no válido. Inténtelo nuevamente.")
        
        # Validación de ID de profesor
        gotoxy(2, 6)
        while True:
            id_profesor = input("Ingrese el ID del profesor: ")
            profesor = next((p for p in profesores if int(p['id']) == int(id_profesor)), None)
            if profesor:
                nombre_profesor = f"{profesor['nombre']} {profesor['apellido']}"
                break
            else:
                print("ID de profesor no válido. Inténtelo nuevamente.")
        
        # Validación de ID de asignatura
        gotoxy(2, 7)
        while True:
            id_asignatura = input("Ingrese el ID de la asignatura: ")
            asignatura = next((a for a in asignaturas if int(a['id']) == int(id_asignatura)), None)
            if asignatura:
                nombre_asignatura = asignatura['Asignatura']
                break
            else:
                print("ID de asignatura no válido. Inténtelo nuevamente.")
        
        json_file = JsonFile(path + '/archivosbases/matriculas.json')
        matriculas = json_file.read()
        
        # Validar si ya existe una matrícula para el estudiante y curso seleccionados
        if any(m['id_estudiante'] == id_estudiante and m['id_curso'] == id_curso for m in matriculas):
            print("El estudiante ya está matriculado en el curso seleccionado.")
            return
        
        last_id = max([m['id'] for m in matriculas]) if matriculas else 0
        new_id = last_id + 1
        
        # Obtener la fecha actual
        fecha_creacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        nueva_matricula = {
            "id": new_id,
            "id_estudiante": id_estudiante,
            "nombre_estudiante": nombre_estudiante,
            "id_curso": id_curso,
            "nombre_curso": nombre_curso,
            "id_periodo": id_periodo,
            "nombre_periodo": nombre_periodo,
            "id_profesor": id_profesor,
            "nombre_profesor": nombre_profesor,
            "id_asignatura": id_asignatura,
            "nombre_asignatura": nombre_asignatura,
            "fecha_creacion": fecha_creacion
        }
        
        matriculas.append(nueva_matricula)
        json_file.save(matriculas)
        print("Matrícula registrada exitosamente.")
        
        input("Presione Enter para continuar...")
        time.sleep(2)
    
    @staticmethod
    def update():
        borrarPantalla()
        dibujar_cuadro()
        gotoxy(2, 1)
        print("Actualizar Matrícula")
        gotoxy(2, 3)
        id_matricula = int(input("Ingrese el ID de la matrícula a actualizar: "))
        
        json_file = JsonFile(path + '/archivosbases/matriculas.json')
        matriculas = json_file.read()
        
        matricula = next((m for m in matriculas if m['id'] == id_matricula), None)
        if not matricula:
            print("Matrícula no encontrada.")
            return
        
        # Cargar datos necesarios
        json_file_estudiantes = JsonFile(path + '/archivosbases/estudiantes.json')
        estudiantes = json_file_estudiantes.read()
        json_file_cursos = JsonFile(path + '/archivosbases/cursos.json')
        cursos = json_file_cursos.read()
        json_file_periodos = JsonFile(path + '/archivosbases/periodos.json')
        periodos = json_file_periodos.read()
        json_file_profesores = JsonFile(path + '/archivosbases/profesores.json')
        profesores = json_file_profesores.read()
        json_file_asignaturas = JsonFile(path + '/archivosbases/asignaturas.json')
        asignaturas = json_file_asignaturas.read()
        
        # Validación de ID de estudiante
        gotoxy(2, 5)
        while True:
            id_estudiante = input("Ingrese el ID del estudiante: ")
            estudiante = next((e for e in estudiantes if int(e['id']) == int(id_estudiante)), None)
            if estudiante:
                nombre_estudiante = f"{estudiante['nombre']} {estudiante['apellido']}"
                break
            else:
                print("ID de estudiante no válido. Inténtelo nuevamente.")

        # Validación de ID de curso
        gotoxy(2, 6)
        while True:
            id_curso = input("Ingrese el ID del curso: ")
            curso = next((c for c in cursos if int(c['id']) == int(id_curso)), None)
            if curso:
                nombre_curso = curso['Curso']
                break
            else:
                print("ID de curso no válido. Inténtelo nuevamente.")
                time.sleep(2)    
  
        # Validación de ID de periodo
        gotoxy(2, 7)
        while True:
            id_periodo = input("Ingrese el ID del periodo: ")
            periodo = next((p for p in periodos if int(p['id']) == int(id_periodo)), None)
            if periodo:
                nombre_periodo = periodo['Periodo']
                break
            else:
                print("ID de periodo no válido. Inténtelo nuevamente.")
                time.sleep(2) 
        # Validación de ID de profesor
        gotoxy(2, 8)
        while True:
            id_profesor = input("Ingrese el ID del profesor: ")
            profesor = next((p for p in profesores if int(p['id']) == int(id_profesor)), None)
            if profesor:
                nombre_profesor = f"{profesor['nombre']} {profesor['apellido']}"
                break
            else:
                print("ID de profesor no válido. Inténtelo nuevamente.")
                time.sleep(2)
        # Validación de ID de asignatura
        gotoxy(2, 9)
        while True:
            id_asignatura = input("Ingrese el ID de la asignatura: ")
            asignatura = next((a for a in asignaturas if int(a['id']) == int(id_asignatura)), None)
            if asignatura:
                nombre_asignatura = asignatura['Asignatura']
                break
            else:
                print("ID de asignatura no válido. Inténtelo nuevamente.")
                time.sleep(2)
        # Obtener la fecha actual
        fecha_creacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Crear un nuevo registro en la base de datos
        matricula['id_estudiante'] = id_estudiante
        matricula['nombre_estudiante'] = nombre_estudiante
        matricula['id_curso'] = id_curso
        matricula['nombre_curso'] = nombre_curso
        matricula['id_periodo'] = id_periodo
        matricula['nombre_periodo'] = nombre_periodo
        matricula['id_profesor'] = id_profesor
        matricula['nombre_profesor'] = nombre_profesor
        matricula['id_asignatura'] = id_asignatura
        matricula['nombre_asignatura'] = nombre_asignatura
        matricula['fecha_creacion'] = fecha_creacion
        json_file.save(matriculas)
        print("Matrícula actualizada exitosamente.")
        
        input("Presione Enter para continuar...")
        time.sleep(2)
    @staticmethod
    def delete():
        borrarPantalla()
        dibujar_cuadro()
        gotoxy(2, 1)
        print("Eliminar Matrícula")
        gotoxy(2, 3)
        id_matricula = int(input("Ingrese el ID de la matrícula a eliminar: "))
        
        json_file = JsonFile(path + '/archivosbases/matriculas.json')
        matriculas = json_file.read()
        
        matricula = next((m for m in matriculas if m['id'] == id_matricula), None)
        if not matricula:
            print("Matrícula no encontrada.")
            return
        
        matriculas.remove(matricula)
        json_file.save(matriculas)
        print("Matrícula eliminada exitosamente.")
        
        input("Presione Enter para continuar...")
        time.sleep(2)

    @staticmethod
    def consult():
        borrarPantalla()
        dibujar_cuadro()
        gotoxy(2, 1)
        print("Consulta de Matrículas")
        
        # Cargar los archivos JSON
        json_file_matriculas = JsonFile(path + '/archivosbases/matriculas.json')
        matriculas = json_file_matriculas.read()
        
        json_file_estudiantes = JsonFile(path + '/archivosbases/estudiantes.json')
        estudiantes = json_file_estudiantes.read()
        
        json_file_cursos = JsonFile(path + '/archivosbases/cursos.json')
        cursos = json_file_cursos.read()
        
        json_file_periodos = JsonFile(path + '/archivosbases/periodos.json')
        periodos = json_file_periodos.read()
        
        json_file_profesores = JsonFile(path + '/archivosbases/profesores.json')
        profesores = json_file_profesores.read()
        
        json_file_asignaturas = JsonFile(path + '/archivosbases/asignaturas.json')
        asignaturas = json_file_asignaturas.read()
        
        if not matriculas:
            print("No hay matrículas registradas.")
            input("Presione Enter para continuar...")
            time.sleep(2)
            return

        # Crear diccionarios para buscar rápidamente los nombres a partir de los IDs
        estudiantes_dict = {str(e['id']): f"{e['nombre']} {e['apellido']}" for e in estudiantes}
        cursos_dict = {str(c['id']): c['Curso'] for c in cursos}
        periodos_dict = {str(p['id']): p['Periodo'] for p in periodos}
        profesores_dict = {str(p['id']): f"{p['nombre']} {p['apellido']}" for p in profesores}
        asignaturas_dict = {str(a['id']): a['Asignatura'] for a in asignaturas}

        # Mostrar las matrículas con toda la información
        for matricula in matriculas:
            nombre_estudiante = estudiantes_dict.get(str(matricula['id_estudiante']), "Desconocido")
            nombre_curso = cursos_dict.get(str(matricula['id_curso']), "Desconocido")
            nombre_periodo = periodos_dict.get(str(matricula['id_periodo']), "Desconocido")
            nombre_profesor = profesores_dict.get(str(matricula['id_profesor']), "Desconocido")
            nombre_asignatura = asignaturas_dict.get(str(matricula['id_asignatura']), "Desconocido")
            fecha_creacion = matricula.get('fecha_creacion', "No disponible")
            print(f"ID Matrícula: {matricula['id']}")
            print(f"Estudiante: {nombre_estudiante} (ID: {matricula['id_estudiante']})")
            print(f"Curso: {nombre_curso} (ID: {matricula['id_curso']})")
            print(f"Periodo: {nombre_periodo} (ID: {matricula['id_periodo']})")
            print(f"Profesor: {nombre_profesor} (ID: {matricula['id_profesor']})")
            print(f"Asignatura: {nombre_asignatura} (ID: {matricula['id_asignatura']})")
            print(f"Fecha de Creación: {fecha_creacion}")
            print("-" * 50)
        
        input("Presione Enter para continuar...")
        time.sleep(2)

