from componentes import Menu, Validar
from utilities import borrarPantalla, gotoxy, dibujar_cuadro
from utilities import reset_color, red_color, green_color, yellow_color, blue_color, purple_color, cyan_color
from basejson import JsonFile
from Unemi import University
from iCrud import ICrud
from CrudAsignaturas import CrudAsignaturas
from CrudEstudiante import CrudEstudiante
from CrudPeriodos import CrudPeriodos
from CrudNivelesEdu import CrudNivelesEdu
from CrudNotas import CrudNotas
from CrudProfesores import CrudProfesores
from CrudCursos import CrudCurso
from CrudMatriculas import CrudMatricula
import datetime
import time, os
from functools import reduce
import platform


path, _ = os.path.split(os.path.abspath(__file__))

# Función para mostrar el menú principal con diseño
def mostrar_menu_principal():
    borrarPantalla()
    dibujar_cuadro()
    gotoxy(2, 1)
    print(green_color + "╔═════════════════════════════════════════════════════╗")
    print("║" + yellow_color + "                   Menu Gestión Académica                     " + reset_color + "║")
    print("╠══════════════════════════════════════════════════════════╣")
    print("║ " + cyan_color + "1) " + reset_color + "Periodos Académicos" + " " * 35 + "║")
    print("║ " + cyan_color + "2) " + reset_color + "Niveles Educativos" + " " * 36 + "║")
    print("║ " + cyan_color + "3) " + reset_color + "Agregar Curso" + " " * 40 + "║")
    print("║ " + cyan_color + "4) " + reset_color + "Asignaturas" + " " * 43 + "║")
    print("║ " + cyan_color + "5) " + reset_color + "Profesores" + " " * 44 + "║")
    print("║ " + cyan_color + "6) " + reset_color + "Estudiantes" + " " * 43 + "║")
    print("║ " + cyan_color + "7) " + reset_color + "Matriculas" + " " * 43 + "║")
    print("║ " + cyan_color + "8) " + reset_color + "Notas" + " " * 49 + "║")
    print("║ " + cyan_color + "9) " + reset_color + "Salir" + " " * 49 + "║")
    print("╚══════════════════════════════════════════════════════════╝")
    opc = input(green_color + "Seleccione una opción: " + reset_color)
    return opc

# Función para mostrar un submenú con diseño
def mostrar_submenu(titulo, opciones):
    borrarPantalla()
    dibujar_cuadro()
    gotoxy(2, 1)
    print(green_color + "╔═════════════════════════════════════════════════════════╗")
    print(f"║{yellow_color}{titulo.center(55)}{reset_color}║")
    print("╠═════════════════════════════════════════════════════════╣")
    for idx, opcion in enumerate(opciones, start=1):
        print(f"║ {cyan_color}{idx}){reset_color} {opcion.ljust(50)}║")
    print("╚═════════════════════════════════════════════════════════╝")
    opc = input(green_color + "Seleccione una opción: " + reset_color)
    return opc

# Menú Proceso Principal
opc = ""
while opc != "7":
    opc = mostrar_menu_principal()
    if opc == "1":
        opc1 = ""
        while opc1 != "5":
            opciones = [red_color + "Ingresar", red_color +"Actualizar", red_color +"Eliminar", red_color +"Consultar", red_color +"Salir"]
            opc1 = mostrar_submenu("Menu Periodos Académicos", opciones)
            if opc1 == "1":
                CrudPeriodos.create()
            elif opc1 == "2":
                CrudPeriodos.update()
            elif opc1 == "3":
                CrudPeriodos.delete()
            elif opc1 == "4":
                CrudPeriodos.consult()
            elif opc1 == "5":
                borrarPantalla()
                print("Regresando al Menu Principal")
                time.sleep(2)
    elif opc == "2":
        opc1 = ""
        while opc1 != "5":
            opciones = [red_color +"Ingresar", red_color +"Actualizar",red_color + "Eliminar", red_color +"Consultar", red_color +"Salir"]
            opc1 = mostrar_submenu("Menu Niveles Educativos", opciones)
            if opc1 == "1":
                CrudNivelesEdu.create()
            elif opc1 == "2":
                CrudNivelesEdu.update()
            elif opc1 == "3":
                CrudNivelesEdu.delete()
            elif opc1 == "4":
                CrudNivelesEdu.consult()
            elif opc1 == "5":
                borrarPantalla()
                print("Regresando al Menu Principal")
                time.sleep(2)
    elif opc == "3":
        opc1 = ""
        while opc1 != "5":
            opciones = [red_color +"Ingresar", red_color +"Actualizar",red_color + "Eliminar", red_color +"Consultar", red_color +"Salir"]
            opc1 = mostrar_submenu("Menu Cursos", opciones)
            if opc1 == "1":
                CrudCurso.create()
            elif opc1 == "2":
                CrudCurso.update()
            elif opc1 == "3":
                CrudCurso.delete()
            elif opc1 == "4":
                CrudCurso.consult()
            elif opc1 == "5":
                borrarPantalla()
                print("Regresando al Menu Principal")
                time.sleep(2)
        
    elif opc == "4":
        opc1 = ""
        while opc1 != "5":
            opciones = [red_color +"Ingresar", red_color +"Actualizar",red_color + "Eliminar", red_color +"Consultar",red_color + "Salir"]
            opc1 = mostrar_submenu("Menu Asignaturas", opciones)
            if opc1 == "1":
                CrudAsignaturas.create()
            elif opc1 == "2":
                CrudAsignaturas.update()
            elif opc1 == "3":
                CrudAsignaturas.delete()
            elif opc1 == "4":
                CrudAsignaturas.consult()
            elif opc1 == "5":
                borrarPantalla()
                print("Regresando al Menu Principal")
                time.sleep(2)
    elif opc == "5":
        opc1 = ""
        while opc1 != "5":
            opciones = [red_color +"Ingresar",red_color + "Actualizar",red_color + "Eliminar", red_color +"Consultar",red_color + "Salir"]
            opc1 = mostrar_submenu("Menu Profesores", opciones)
            if opc1 == "1":
                CrudProfesores.create()
            elif opc1 == "2":
                CrudProfesores.update()
            elif opc1 == "3":
                CrudProfesores.delete()
            elif opc1 == "4":
                CrudProfesores.consult()
            elif opc1 == "5":
                borrarPantalla()
                print("Regresando al Menu Principal")
                time.sleep(2)
    elif opc == "6":
        opc1 = ""
        while opc1 != "7":
            opciones = [red_color +"Ingresar",red_color + "Agregar Asignatura",red_color + "Actualizar", red_color +"Eliminar",red_color + "Consultar", red_color +"Consultar all.",red_color + "Salir"]
            opc1 = mostrar_submenu("Menu Estudiantes", opciones)
            if opc1 == "1":
                CrudEstudiante.create()
            elif opc1 == "2":
                CrudEstudiante.agregar_asignatura()
            elif opc1 == "3":
                CrudEstudiante.update()
            elif opc1 == "4":
                CrudEstudiante.delete()
            elif opc1 == "5":
                CrudEstudiante.consult()
            elif opc1 == "6":
                CrudEstudiante.consult_all()
            elif opc1 == "7":
                borrarPantalla()
                print("Regresando al Menu Principal")
                time.sleep(2)
    elif opc == "7":
        opc1 = ""
        while opc1 != "5":
            opciones = [red_color +"Ingresar", red_color +"Actualizar", red_color +"Eliminar", red_color +"Consultar", red_color +"Salir"]
            opc1 = mostrar_submenu("Menu Matriculas", opciones)
            if opc1 == "1":
                CrudMatricula.create()
            elif opc1 == "2":
                CrudMatricula.update()
            elif opc1 == "3":
                CrudMatricula.delete()
            elif opc1 == "4":
                CrudMatricula.consult()
            elif opc1 == "5":
                borrarPantalla()
                print("Regresando al Menu Principal")
                time.sleep(2)
        

    elif opc == "8":
        opc1 = ""
        while opc1 != "5":
            opciones = [red_color +"Ingresar", red_color +"Actualizar", red_color +"Eliminar",red_color + "Consultar",red_color + "Salir"]
            opc1 = mostrar_submenu("Menu Notas", opciones)
            if opc1 == "1":
                CrudNotas.create()
            elif opc1 == "2":
                CrudNotas.update()
            elif opc1 == "3":
                CrudNotas.delete()
            elif opc1 == "4":
                CrudNotas.consult()
            elif opc1 == "5":
                borrarPantalla()
                print("Regresando al Menu Principal")
                time.sleep(2)
    elif opc == "9":
        borrarPantalla()
        print("Gracias por su visita....")
        time.sleep(2)
