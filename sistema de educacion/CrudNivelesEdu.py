from iCrud import ICrud
from utilities import borrarPantalla, gotoxy, dibujar_cuadro
from basejson import JsonFile
import platform, time
import os 

path, _ = os.path.split(os.path.abspath(__file__))

class CrudNivelesEdu(ICrud):
    @staticmethod
    def create():
        borrarPantalla()
        dibujar_cuadro()
        gotoxy(2, 1)
        print("=" * 166)
        gotoxy(70, 1)
        print("REGISTRO DE NIVELES EDUCATIVOS")
        gotoxy(2, 2)
        print("=" * 166)
        gotoxy(2, 4)
        descripcion = input("Ingrese el nombre del nivel educativo (e.g., Primero de Secundaria): ")

        json_file = JsonFile(path + '/archivosbases/niveles_educativos.json')
        niveles = json_file.read()

        for nivel in niveles:
            if nivel['descripcion'] == descripcion:
                gotoxy(2, 6)
                print("El nivel educativo ya existe")
                time.sleep(2)
                return
            
        last_id = max([nivel['id'] for nivel in niveles]) if niveles else 0
        new_id = last_id + 1
        estado = input("Ingrese el estado del nivel educativo (activo/inactivo): ").lower()

        nuevo_nivel = {
            "id": new_id,
            "descripcion": descripcion,
            "estado": estado
        }
        niveles.append(nuevo_nivel)
        json_file.save(niveles)
        gotoxy(2, 6)
        print("Nivel educativo creado correctamente")
        time.sleep(2)

        if platform.system() == 'Windows':
            input("Presione Enter para continuar...")
        else:
            time.sleep(2)


    @staticmethod
    def update():
        borrarPantalla()
        dibujar_cuadro()
        gotoxy(2, 1)
        print("=" * 166)
        gotoxy(70, 1)
        print("ACTUALIZAR NIVEL EDUCATIVO")
        gotoxy(2, 2)
        print("=" * 166)
        gotoxy(2, 4)
        id_nivel = input("Ingrese el ID del nivel educativo a actualizar: ")
        json_file = JsonFile(path + '/archivosbases/niveles_educativos.json')
        niveles = json_file.read()
        nivel = next((nivel for nivel in niveles if nivel['id'] == int(id_nivel)), None)

        if not nivel:
            gotoxy(2, 6)
            print("El nivel educativo no existe")
            time.sleep(2)
            return

        gotoxy(2, 6)
        print(f"Descripcion actual: {nivel['descripcion']}")
        nueva_descripcion = input("Ingrese la nueva descripcion del nivel educativo: ")
        nuevo_estado = input("Ingrese el nuevo estado del nivel educativo (activo/inactivo): ").lower()

        nivel['descripcion'] = nueva_descripcion
        nivel['estado'] = nuevo_estado
        json_file.save(niveles)
        gotoxy(2, 9)
        print("Nivel educativo actualizado correctamente")
        time.sleep(2)

        if platform.system() == 'Windows':
            input("Presione Enter para continuar...")
        else:
            time.sleep(2)
    @staticmethod
    def delete():
        borrarPantalla()
        dibujar_cuadro()
        gotoxy(2, 1)
        print("=" * 166)
        gotoxy(70, 1)
        print("ELIMINAR NIVEL EDUCATIVO")
        gotoxy(2, 2)
        print("=" * 166)
        gotoxy(2, 4)
        id_nivel = input("Ingrese el ID del nivel educativo a eliminar: ")
        json_file = JsonFile(path + '/archivosbases/niveles_educativos.json')
        niveles = json_file.read()
        nivel = next((nivel for nivel in niveles if nivel['id'] == int(id_nivel)), None)

        if not nivel:
            gotoxy(2, 6)
            print("El nivel educativo no existe")
            time.sleep(2)
            return

        niveles.remove(nivel)
        json_file.save(niveles)
        gotoxy(2, 6)
        print("Nivel educativo eliminado correctamente")
        time.sleep(2)

        if platform.system() == 'Windows':
            input("Presione Enter para continuar...")
        else:
            time.sleep(2)

    @staticmethod
    def list():
        borrarPantalla()
        dibujar_cuadro()
        gotoxy(2, 1)
        print("=" * 166)
        gotoxy(70, 1)
        print("LISTADO DE NIVELES EDUCATIVOS")
        gotoxy(2, 2)
        print("=" * 166)
        gotoxy(2, 4)
        json_file = JsonFile(path + '/archivosbases/niveles_educativos.json')
        niveles = json_file.read()
        if not niveles:
            gotoxy(2, 6)
            print("No hay niveles educativos registrados")
            time.sleep(2)
            return

        gotoxy(2, 6)
        print("ID".ljust(5) + "Descripcion".ljust(50) + "Estado".ljust(10))
        gotoxy(2, 7)
        print("=" * 166)

        for nivel in niveles:
            gotoxy(2, 8)
            print(str(nivel['id']).ljust(5) + nivel['descripcion'].ljust(50) + nivel['estado'].ljust(10))
        time.sleep(2)

        if platform.system() == 'Windows':
            input("Presione Enter para continuar...")
        else:
            time.sleep(2)

    def consult():
        borrarPantalla()
        dibujar_cuadro()
        gotoxy(2, 1)
        print("=" * 166)
        gotoxy(70, 1)
        print("CONSULTA DE NIVEL EDUCATIVO")
        gotoxy(2, 2)
        print("=" * 166)
        gotoxy(2, 4)
        id_nivel = input("Ingrese el ID del nivel educativo a consultar: ")
        json_file = JsonFile(path + '/archivosbases/niveles_educativos.json')
        niveles = json_file.read()
        nivel = next((nivel for nivel in niveles if nivel['id'] == int(id_nivel)), None)

        if not nivel:
            gotoxy(2, 6)
            print("El nivel educativo no existe")
            time.sleep(2)
            return

        gotoxy(2, 6)
        print(f"Descripcion: {nivel['descripcion']}")
        gotoxy(2, 7)
        print(f"Estado: {nivel['estado']}")
        time.sleep(2)

        if platform.system() == 'Windows':
            input("Presione Enter para continuar...")
        else:
            time.sleep(2)

    

