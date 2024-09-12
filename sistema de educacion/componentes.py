from utilities import gotoxy, borrarPantalla,mensaje
from utilities import reset_color,red_color,green_color,yellow_color,blue_color,purple_color,cyan_color
import time
import re

class Menu:
    def __init__(self,titulo,opciones=[],col=6,fil=1):
        self.titulo = titulo
        self.opciones = opciones
        self.col = col
        self.fil = fil
     
    def menu(self):
        gotoxy(self.col,self.fil);print(f"{self.titulo}")
        self.col -= 3
        for opcion in self.opciones:
            self.fil += 1
            gotoxy(self.col,self.fil);print(f"{opcion}")
        gotoxy(self.col,self.fil+1)
        return (input("Elija una opcion: "))
    
          
class Validar:
    def solo_numeros(self,mensajeError,col,fil):
        while True:
            gotoxy(col,fil);valor = input()
            if valor.isnumeric():
                return valor
            else:
                mensaje(mensajeError,0,col,fil)
                time.sleep(1)

    def solo_letras(self,mensajeError,col,fil):   
        while True:
            gotoxy(col,fil);valor = input(">")
            if valor.isalpha():
                return valor
            else:
                mensaje(mensajeError,0,col,fil)
                time.sleep(1)

    def solo_decimales(self,mensajeError,col,fil):
        while True:
            gotoxy(col,fil);valor = input(">")
            try:
                valor = float(valor)
                return valor
            except:
                mensaje(mensajeError,0,col,fil)
                time.sleep(1)

    def validar_letras(frase, col1, fil1, col2, fil2):
        while True:
            gotoxy(col1, fil1)
            valor = input(frase)
        
        # Expresión regular para permitir letras, números y signos
            if re.match(r'^[a-zA-Z0-9\s\-\+\!\@\#\$\%\^\&\*\(\)\_\=\{\}\[\]\|\:\;\'\"\<\>\,\.\?\/\~\`]+$', valor):
                return valor
            else:
                mensaje("Entrada inválida. Por favor, ingrese letras, números y signos permitidos.", col2, fil2)
                time.sleep(1)

    def validar_numeros(frase, col1, fil1, col2, fil2):
        while True:
            gotoxy(col1,fil1)
            print(blue_color + f"{frase}")
            gotoxy(col2, fil2)
            valor = input(purple_color)
            if valor.isnumeric():
                return valor
            else:
                mensaje("Solo numeros",0,col2,fil2)
                time.sleep(1)
            
  
    def validar_cedula(mensaje, x, y, x2, y2):
        gotoxy(x, y)
        print(mensaje)
        gotoxy(x2, y2)
        dni = input()
        # Aquí puedes agregar la lógica de validación del DNI
        if len(dni) == 10 and dni.isdigit():  
         return dni
    
    def validar_opcion(mensaje, col, fil, col2, fil2, opciones):
        while True:
            gotoxy(col, fil)
            print(mensaje)
            gotoxy(col2, fil2)
            valor = input()
            if valor in opciones:
                return valor
            else:
                mensaje("Opción inválida. Por favor, seleccione una opción válida.", col2, fil2)
                time.sleep(1
    )

    def validar_decimales(mensaje, col, fil, col2, fil2):
        while True:
            gotoxy(col,fil);valor = input(mensaje)
            try:
                valor = float(valor)
                return valor
            except:
                mensaje(mensaje,0,col2,fil2)
                time.sleep(1)

class todas_mienten:
    pass

if __name__ == '__main__':
    opciones_menu = ["1. Entero", "2. Letra", "3. Decimal"]
    menu = Menu(titulo="--Menu--", opciones=opciones_menu, col=10, fil=5)
    opciones_elegida = menu.menu()
    print(f"Opcion elegida: {opciones_elegida}")
    valida = Validar()
    if(opciones_menu==1):
        numero_valido = valida.solo_numeros("Mensaje de error", 10, 10)
        print(f"Numero ingresado: {numero_valido}")
    
    numero_valido = valida.solo_numeros("Mensaje de error", 10, 10)
    print(f"Numero ingresado: {numero_valido}")

    letra_validada = valida.solo_letras("Ingrese una letra:", "Mensaje de error")
    print("Letra validada:", letra_validada)
    
    decimal_validado = valida.solo_decimales("Ingrese un decimal:", "Mensaje de error")
    print("Decimal validado:", decimal_validado)
     

                           