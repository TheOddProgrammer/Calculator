# Importacion de Librerias o Datos de Otro Archivo

import customtkinter
import webbrowser as wb
from Components import Design, Manual


# Colores Base de la Aplicacion
customtkinter.set_default_color_theme("green")

ScaleScreen = True
app = customtkinter.CTk(fg_color="white")

# Definir el Tamaño de la Aplicacion en un Principio
if ScaleScreen:
    app.wm_attributes("-fullscreen", True)
else:
    app.geometry("1366x768")


# Declaracion y Llamado Funciones Normales
def FirstGuide():
    path = "Archives\Manual.pdf"
    wb.open(path)


# Llamado Funciones
FirstGuide()
Design.MenuBotones(app)
Manual.ManualButton(app)

# Permite a la Aplicacion Generar Cambios
app.mainloop()
