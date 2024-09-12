from iCrud import ICrud
from utilities import borrarPantalla, gotoxy, dibujar_cuadro
from basejson import JsonFile
import platform, time
import os
path, _ = os.path.split(os.path.abspath(__file__))

class CrudAsignaturas(ICrud):
    @staticmethod
    def create():
        borrarPantalla()
        dibujar_cuadro()
        gotoxy(2, 1)
        print("Registro de Asignatura")
        gotoxy(2, 3)
        descripcion = input("Ingrese el nombre de la asignatura (e.g., Matemáticas): ")
        
        # Obtener la lista de niveles educativos disponibles
        json_file_niveles = JsonFile(path + '/archivosbases/niveles_educativos.json')
        niveles = json_file_niveles.read()
        
        if not niveles:
            print("No hay niveles registrados. Debe registrar un nivel antes de agregar asignaturas.")
            return
        
        # Mostrar niveles disponibles y seleccionar uno
        print("Niveles educativos disponibles:")
        for nivel in niveles:
            print(f"ID: {nivel['id']} - {nivel['descripcion']}")
        id_nivel = int(input("Ingrese el ID del nivel al que pertenece la asignatura: "))
        
        
        nivel_seleccionado = next((n for n in niveles if n['id'] == id_nivel), None)
        if not nivel_seleccionado:
            print("Nivel no encontrado.")
            return
        
        estado = input("Ingrese el estado de la asignatura (activo/inactivo): ").lower()
        
        json_file_asignaturas = JsonFile(path + '/archivosbases/asignaturas.json')
        asignaturas = json_file_asignaturas.read()

        for asignatura in asignaturas:
            if asignatura['Asignatura'] == descripcion and asignatura['Nivel'] == nivel_seleccionado['descripcion']:
                print("La asignatura ya existe.")
                return
        
        last_id = max([asignatura['id'] for asignatura in asignaturas]) if asignaturas else 0
        new_id = last_id + 1
        
        nueva_asignatura = {
            "id": new_id,
            "Asignatura": descripcion,
            "Nivel": nivel_seleccionado['descripcion'],
            "Estado": estado
        }
        
        asignaturas.append(nueva_asignatura)
        json_file_asignaturas.save(asignaturas)
        print("Asignatura registrada exitosamente.")
        
        if platform.system() == 'Windows':
            input("Presione Enter para continuar...")
        else:
            time.sleep(2)
    
    @staticmethod
    def update():
        borrarPantalla()
        dibujar_cuadro()
        gotoxy(2, 1)
        print("Actualizar Asignatura")
        gotoxy(2, 3)
        id_asignatura = int(input("Ingrese el ID de la asignatura a actualizar: "))
        
        json_file_asignaturas = JsonFile(path + '/archivosbases/asignaturas.json')
        asignaturas = json_file_asignaturas.read()
        
        asignatura = next((a for a in asignaturas if a['id'] == id_asignatura), None)
        if not asignatura:
            print("Asignatura no encontrada.")
            return
        
        gotoxy(2, 5)
        nueva_descripcion = input(f"Ingrese la nueva descripción de la asignatura (actual: {asignatura['Asignatura']}): ")
        nuevo_estado = input(f"Ingrese el nuevo estado de la asignatura (activo/inactivo, actual: {asignatura['Estado']}): ").lower()
        
        # Actualizar valores solo si se ingresan nuevos, de lo contrario mantener los actuales
        asignatura['Asignatura'] = nueva_descripcion if nueva_descripcion else asignatura['Asignatura']
        asignatura['Estado'] = nuevo_estado if nuevo_estado else asignatura['Estado']
        
        json_file_asignaturas.save(asignaturas)
        print("Asignatura actualizada correctamente.")
        
        if platform.system() == 'Windows':
            input("Presione Enter para continuar...")
        else:
            time.sleep(2)

    @staticmethod
    def delete():
        borrarPantalla()
        dibujar_cuadro()
        gotoxy(2, 1)
        print("Eliminar Asignatura")
        gotoxy(2, 3)
        id_asignatura = int(input("Ingrese el ID de la asignatura a eliminar: "))
        
        json_file_asignaturas = JsonFile(path + '/archivosbases/asignaturas.json')
        asignaturas = json_file_asignaturas.read()
        
        asignatura = next((a for a in asignaturas if a['id'] == id_asignatura), None)
        if not asignatura:
            print("Asignatura no encontrada.")
            return
        
        asignaturas.remove(asignatura)
        json_file_asignaturas.save(asignaturas)
        print("Asignatura eliminada correctamente.")
        
        if platform.system() == 'Windows':
            input("Presione Enter para continuar...")
        else:
            time.sleep(2)

    @staticmethod
    def consult():
        borrarPantalla()
        dibujar_cuadro()
        gotoxy(2, 1)
        print("Consultar Asignaturas")
        
        json_file_asignaturas = JsonFile(path + '/archivosbases/asignaturas.json')
        asignaturas = json_file_asignaturas.read()
        
        if not asignaturas:
            print("No hay asignaturas registradas.")
            return
        
        for asignatura in asignaturas:
            print(f"ID: {asignatura['id']}, Descripción: {asignatura['Asignatura']}, Nivel: {asignatura['Nivel']}, Estado: {asignatura['Estado']}")
        
        if platform.system() == 'Windows':
            input("Presione Enter para continuar...")
        else:
            time.sleep(2)
            
      
    








        