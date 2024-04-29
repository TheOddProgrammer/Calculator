import customtkinter as ct
import webbrowser as wb
import Components.Solution_X as Sx


def Buttons(frame, app):
    minFrame(frame)
    Principal(frame)
    StepsLU(frame)
    StepsZ(frame)
    Close(frame, app)
    OpenManual(app)


def minFrame(frame):
    boton = ct.CTkButton(
        master=frame,
        fg_color="black",
        width=300,
        height=100,
        font=("monocraft", 30),
        text="Calculadora",
        corner_radius=0,
        hover=False,
    )

    boton.pack(padx=0, pady=0)


def Principal(frame):

    boton = ct.CTkButton(
        master=frame,
        text="Comenzar",
        width=300,
        height=100,
        anchor="center",
        fg_color="black",
        font=("monocraft", 30),
        corner_radius=0,
        border_width=1,
        border_color="white",
        hover_color=("pink", "green"),
    )

    boton.pack(padx=0, pady=0)


def StepsLU(frame):
    boton = ct.CTkButton(
        master=frame,
        text="Pasos LU",
        width=300,
        height=100,
        anchor="center",
        fg_color="black",
        font=("monocraft", 30),
        corner_radius=0,
        border_width=1,
        border_color="white",
        hover_color=("pink", "blue"),
    )

    boton.pack(padx=0, pady=0)


def StepsZ(frame):
    boton = ct.CTkButton(
        master=frame,
        text="Pasos Z",
        width=300,
        height=100,
        anchor="center",
        fg_color="black",
        font=("monocraft", 30),
        corner_radius=0,
        border_width=1,
        border_color="white",
        hover_color=("pink", "blue"),
    )

    boton.pack(padx=0, pady=0)


def Close(frame, app):

    def Cerrar():
        app.destroy()

    boton = ct.CTkButton(
        master=frame,
        text="Cerrar",
        width=300,
        height=100,
        anchor="center",
        fg_color="black",
        font=("monocraft", 30),
        corner_radius=0,
        border_width=1,
        border_color="white",
        hover_color="#F02F2C",
        command=Cerrar,
    )

    boton.pack(padx=0, pady=0)


# Todo lo que Tiene Que Ver Con Manual y Documentación
def OpenManual(app):

    def Open():
        path = "Archives\Potenciometro.pdf"
        wb.open(path)

    def Disable():
        frame.place_forget()
        UnManual.place_forget()

    def Enable():
        UnManual.place(relx=0.94, rely=0.84)
        frame.place(relx=0.78, rely=0.84)

    Manual = ct.CTkButton(
        master=app,
        fg_color="green",
        text="?",
        font=("monocraft", 23),
        height=50,
        width=50,
        corner_radius=200,
        text_color="white",
        bg_color="black",
        command=Enable,
    )

    Manual.place(relx=0.94, rely=0.91)

    UnManual = ct.CTkButton(
        master=app,
        fg_color="green",
        text="X",
        font=("monocraft", 23),
        height=50,
        width=50,
        corner_radius=200,
        text_color="white",
        bg_color="black",
        command=Disable,
    )

    # Opcion de Documentacio o Guía

    frame = ct.CTkFrame(
        master=app,
        fg_color="black",
        bg_color="black",
        corner_radius=10,
    )

    buttonA = ct.CTkButton(
        master=frame,
        text="Documentation",
        command=Open,
        fg_color="blue",
        corner_radius=5,
        hover_color="red",
        bg_color="black",
        height=50,
        width=200,
    )
    buttonA.pack(side=ct.TOP)

    buttonB = ct.CTkButton(
        master=frame,
        hover_color="red",
        text="Guide",
        command=Open,
        fg_color="blue",
        bg_color="black",
        corner_radius=5,
        height=50,
        width=200,
    )

    buttonB.pack(side=ct.TOP)
    buttonB.pack(pady=1)
