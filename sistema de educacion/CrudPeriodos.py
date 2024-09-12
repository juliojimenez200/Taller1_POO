import os
from iCrud import ICrud
import time
from datetime import datetime
from utilities import borrarPantalla, gotoxy, dibujar_cuadro
from componentes import Validar
from basejson import JsonFile
import platform
path, _ = os.path.split(os.path.abspath(__file__))
class CrudPeriodos(ICrud):
    @staticmethod
    def create():
        borrarPantalla()
        dibujar_cuadro()
        gotoxy(2, 2)
        print("=" * 166)
        gotoxy(70, 2)
        print("REGISTRO DE PERIODO ACADEMICO")
        gotoxy(2, 3)
        print("=" * 166)

        #solicitamos datos del periodo academico
        gotoxy(2,5)
        nombre = Validar.validar_letras("Ingrese el nombre del periodo (ej: 'Semestre 1 - 2024'): ", 2, 5, 50, 5)
        estado = Validar.validar_opcion("Ingrese el estado del periodo (1: Activo, 0: Inactivo): ", 2, 6, 57, 6, ["1", "0"])
        fecha_creacion = datetime.now().strftime('%Y-%m-%d')

        #cargar periodos exixtentes
        json_file = JsonFile(path + '/archivosbases/periodos.json')
        periodos = json_file.read()

        #obtener el ultimo id y calcular el nuevo
        last_id = max([periodo["id"]for periodo in periodos])if periodos else 0 
        new_id = last_id + 1

        #verificar si el periodo ya existe
        existing_periodo = next((periodo for periodo in periodos if periodo["Periodo"] == nombre), None)
        if existing_periodo:
            gotoxy(2, 8)
            print("El periodo academico ya existe")
            time.sleep(2)
            return
        
        # # Crear nuevo periodo
        periodo = {
            "id": new_id,
            "Periodo": nombre,
            "fecha_creacion": fecha_creacion,'estado': 'Activo' if estado == '1' else 'Inactivo'
        }
        periodos.append(periodo)
        json_file.save(periodos)
        gotoxy(2, 8)
        print("Periodo academico creado correctamente")

    input("Precione ENTER para continuar...")
    time.sleep(2)
        
    @staticmethod
    def update():
        borrarPantalla()
        dibujar_cuadro()
        gotoxy(2, 2)
        print("=" * 166)
        gotoxy(70, 2)
        print("ACTUALIZACION DE PERIODO ACADEMICO")
        gotoxy(2, 3)
        print("=" * 166)

        # Solicitar ID del periodo a actualizar
        id_periodo = int(Validar.validar_numeros("Ingrese el ID del periodo que desea actualizar: ", 2, 6, 50, 6))
        json_file = JsonFile(path + '/archivosbases/periodos.json')
        periodos = json_file.read()

         # Buscar el periodo
        found_periodo = None
        for periodo in periodos:
            if periodo['id'] == id_periodo:
                found_periodo = periodo
                break
            if not found_periodo:
                gotoxy(2, 8)
                print("No se encontro el periodo academico")
                time.sleep(2)
                return

        if found_periodo:
            gotoxy(2, 8)
            print("Detalles del periodo a actualizar:")
            gotoxy(2, 9)
            print(f"ID: {found_periodo['id']}, Nombre: {found_periodo['Periodo']}, Estado: {found_periodo['estado']}")
        
        # Actualizar los datos

            nuevo_nombre = Validar.validar_letras(f"Ingrese el nuevo nombre del periodo (actual: {found_periodo['Periodo']}): ", 2, 10, 62, 10)
            nuevo_estado = Validar.validar_opcion(f"Ingrese el nuevo estado del periodo (1: Activo, 0: Inactivo, actual: {found_periodo['estado']}): ", 2, 11, 79, 11, ["1", "0"])

            found_periodo['nombre'] = nuevo_nombre if nuevo_nombre else found_periodo['nombre']
            found_periodo['estado'] = 'Activo' if nuevo_estado == '1' else 'Inactivo'

            #guardar cambios 
            json_file.save(periodos)
            gotoxy(2, 13)
            print("Periodo academico actualizado correctamente")
        else:
            gotoxy(2, 13)
            print("No se encontro el periodo academico")

        input("Presiona Enter para continuar...")
        time.sleep(2)

    @staticmethod
    def delete():
        borrarPantalla()
        dibujar_cuadro()
        gotoxy(2, 2)
        print("=" * 166)
        gotoxy(70, 2)
        print("ELIMINACION DE PERIODO ACADEMICO")
        gotoxy(2, 3)
        print("=" * 166)

        # Solicitar ID del periodo a eliminar
        id_periodo = int(Validar.validar_numeros("Ingrese el ID del periodo que desea eliminar: ", 2, 6, 50, 6))
        json_file = JsonFile(path + '/archivosbases/periodos.json')
        periodos = json_file.read()

        #Buscar el periodo
        found_periodo = next((periodo for periodo in periodos if periodo['id'] == id_periodo), None)
        
        if found_periodo:
            gotoxy(2, 8)
            print(f"Periodo encontrado: {found_periodo['nombre']}")
            confirmacion = Validar.validar_letras("¿Está seguro de que desea eliminar este periodo? (s/n): ", 2, 9, 58, 9).lower()
            if confirmacion == 's':
                periodos = [p for p in periodos if p['id'] != id_periodo]
                json_file.save(periodos)
                gotoxy(2, 11)
                print("Periodo eliminado exitosamente.")
            else:
                gotoxy(2, 11)
                print("Eliminación cancelada.")

        else:
            gotoxy(2, 11)
            print("No se encontró el periodo académico.")

        input("Presiona Enter para continuar...")
        time.sleep(2) 


    @staticmethod
    def consult():
        borrarPantalla()
        dibujar_cuadro()
        gotoxy(2, 2)
        print("=" * 166)
        gotoxy(70, 2)
        print("CONSULTA DE PERIODO ACADEMICO")
        gotoxy(2, 3)
        print("=" * 166)

        # Cargar periodos
        json_file = JsonFile(path + '/archivosbases/periodos.json')
        periodos = json_file.read()

        # Imprimir encabezado
        gotoxy(2, 5)
        print("ID".ljust(5) + "Periodo".ljust(50) + "Estado".ljust(20) + "Fecha de Creación".ljust(20))
        print("=" * 166)

        # Imprimir periodos
        linea = 7  # Línea inicial para mostrar los periodos
        for periodo in periodos:
            gotoxy(2, linea)
            print(str(periodo['id']).ljust(5) + str(periodo['Periodo']).ljust(50) + str(periodo['estado']).ljust(20) + str(periodo['fecha_creacion']).ljust(20))
            linea += 1  # Incrementar la línea para el próximo periodo
            
        input("Presiona Enter para continuar...")
        time.sleep(2)

    

            
            


   










    