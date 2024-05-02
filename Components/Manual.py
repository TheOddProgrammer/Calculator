import customtkinter as ct
import webbrowser as wb


def ManualButton(app):

    # Funcion de los Botones Usados

    def ButtonPosition(Texto):
        Texto.pack(side=ct.TOP)
        Texto.pack(expand=True)
        Texto.pack(padx=2, pady=2)
        Texto.pack(fill=ct.BOTH)
        Texto.pack_propagate(False)

    def OpenDoc():
        wb.open("Archives\Documentacion.pdf")

    def OpenGuide():
        wb.open("Archives\Manual.pdf")

    def OpenOptions():
        OpenButton.place_forget()
        FrameOptions.place(relx=0.88, rely=0.82)
        FrameOptions.pack_propagate(False)
        CloseButton.place(relx=0.94, rely=0.92)
        CloseButton.pack_propagate(False)

    def CloseOptions():
        CloseButton.place_forget()
        FrameOptions.place_forget()
        OpenButton.place(relx=0.94, rely=0.92)
        OpenButton.pack_propagate(False)

    # Boton para Abrir las Opciones de Seguimmeinto Como Manual
    OpenButton = ct.CTkButton(
        master=app,
        fg_color="#0B2133",
        bg_color="#293C4B",
        corner_radius=400,
        width=50,
        height=50,
        command=OpenOptions,
        text="?",
        font=("Times New Roman", 25),
    )

    OpenButton.place(relx=0.94, rely=0.92)
    OpenButton.pack_propagate(False)

    # Boton para Cerrar las Opciones de Seguimiento
    CloseButton = ct.CTkButton(
        master=app,
        fg_color="#33060E",
        bg_color="#293C4B",
        corner_radius=400,
        width=50,
        height=50,
        text="X",
        command=CloseOptions,
        hover_color="#2D000B",
        font=("Times New Roman", 16),
    )

    # Frame donde se Muestran las Opciones a Elegir

    FrameOptions = ct.CTkFrame(
        master=app,
        bg_color="#293C4B",
        fg_color="white",
        width=1000,
        height=500,
        corner_radius=10,
    )

    ButtonGuide = ct.CTkButton(
        master=FrameOptions,
        text="Guide",
        bg_color="white",
        fg_color="#0B2133",
        command=OpenGuide,
        font=("arial", 17),
    )

    ButtonPosition(ButtonGuide)

    ButtonDocument = ct.CTkButton(
        master=FrameOptions,
        text="Document",
        bg_color="white",
        fg_color="#0B2133",
        command=OpenDoc,
        font=("arial", 17),
    )

    ButtonPosition(ButtonDocument)
