import customtkinter
import webbrowser as wb
from Components import Design, Manual

customtkinter.set_default_color_theme("green")

ScaleScreen = True

app = customtkinter.CTk(fg_color="white")
if ScaleScreen:
    app.wm_attributes("-fullscreen", True)
else:
    app.geometry("1366x768")


# Declaracion y Llamado Funciones Normales
def FirstGuide():
    path = "Archives\Potenciometro.pdf"
    wb.open(path)


# Llamado Funciones
# FirstGuide()
Design.MenuBotones(app)
Manual.ManualButton(app)


app.mainloop()
