from iCrud import ICrud
from utilities import borrarPantalla, gotoxy, dibujar_cuadro
from basejson import JsonFile
import platform, time
import os
path, _ = os.path.split(os.path.abspath(__file__))

class CrudCurso(ICrud):
    @staticmethod
    def create():
        borrarPantalla()
        dibujar_cuadro()
        gotoxy(2, 1)
        print("Registro de Curso")
        gotoxy(2, 3)
        descripcion = input("Ingrese el nombre del curso (e.g., Programación): ")
        
        # Obtener la lista de niveles educativos disponibles
        json_file_niveles = JsonFile(path + '/archivosbases/niveles_educativos.json')
        niveles = json_file_niveles.read()
        
        if not niveles:
            print("No hay niveles registrados. Debe registrar un nivel antes de agregar cursos.")
            return
        
        # Mostrar niveles disponibles y seleccionar uno
        print("Niveles educativos disponibles:")
        for nivel in niveles:
            print(f"ID: {nivel['id']} - {nivel['descripcion']}")
        id_nivel = int(input("Ingrese el ID del nivel al que pertenece el curso: "))
        
        
        nivel_seleccionado = next((n for n in niveles if n['id'] == id_nivel), None)
        if not nivel_seleccionado:
            print("Nivel no encontrado.")
            return
        
        estado = input("Ingrese el estado del curso (activo/inactivo): ").lower()
        
        json_file_cursos = JsonFile(path + '/archivosbases/cursos.json')
        cursos = json_file_cursos.read()

        for curso in cursos:
            if curso['Curso'] == descripcion and curso['Nivel'] == nivel_seleccionado['descripcion']:
                print("El curso ya existe.")
                return
        
        last_id = max([curso['id'] for curso in cursos]) if cursos else 0
        new_id = last_id + 1
        
        nuevo_curso = {
            "id": new_id,
            "Curso": descripcion,
            "Nivel": nivel_seleccionado['descripcion'],
            "Estado": estado
        }
        
        cursos.append(nuevo_curso)
        json_file_cursos.save(cursos)
        print("Curso registrado exitosamente.")

    @staticmethod
    def update():
        borrarPantalla()
        dibujar_cuadro()
        gotoxy(2, 1)
        print("Actualizar Curso")
        gotoxy(2, 3)
        id_curso = int(input("Ingrese el ID del curso a actualizar: "))
        
        json_file = JsonFile(path + '/archivosbases/cursos.json')
        cursos = json_file.read()
        
        curso = next((n for n in cursos if n['id'] == id_curso), None)
        if not curso:
            print("Curso no encontrado.")
            return
        
        gotoxy(2, 5)
        nueva_descripcion = input(f"Ingrese el nuevo nombre del curso (actual: {curso['Curso']}): ")
        nuevo_estado = input(f"Ingrese el nuevo estado del curso (actual: {curso['Estado']}): ").lower()
        
        # Si no se introduce una nueva descripción, mantenemos la existente
        descripcion = nueva_descripcion if nueva_descripcion else curso['Curso']
        
        # Actualizamos las notas y el estado
        curso['Curso'] = descripcion
        curso['Estado'] = nuevo_estado
        
        json_file.save(cursos)
        print("Curso actualizado exitosamente.")
        
        if platform.system() == 'Windows':
            input("Presione Enter para continuar...")
        else:
            time.sleep(2)
    
    @staticmethod
    def delete():
        borrarPantalla()
        dibujar_cuadro()
        gotoxy(2, 1)
        print("Eliminar Curso")
        gotoxy(2, 3)
        id_curso = int(input("Ingrese el ID del curso a eliminar: "))
        
        json_file = JsonFile(path + '/archivosbases/cursos.json')
        cursos = json_file.read()
        
        curso = next((n for n in cursos if n['id'] == id_curso), None)
        if not curso:
            print("Curso no encontrado.")
            return
        
        cursos.remove(curso)
        json_file.save(cursos)
        print("Curso eliminado exitosamente.")
        
        if platform.system() == 'Windows':
            input("Presione Enter para continuar...")
        else:
            time.sleep(2)
    
    @staticmethod
    def consult():
        borrarPantalla()
        dibujar_cuadro()
        gotoxy(2, 1)
        print("Consultar Cursos")
        json_file = JsonFile(path + '/archivosbases/cursos.json')
        cursos = json_file.read()
    
        if not cursos:
            print("No hay cursos registrados.")
            return
        
        for curso in cursos:
            print(f"ID: {curso['id']}, Curso: {curso['Curso']}, Nivel: {curso['Nivel']}, Estado: {curso['Estado']}")
    
        if platform.system() == 'Windows':
            input("Presione Enter para continuar...")
        else:
            time.sleep(2)
            










        

    
 


