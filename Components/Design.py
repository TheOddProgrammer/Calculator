import customtkinter as ct
import Components.ContentMain as Content
from CTkMessagebox import CTkMessagebox


def MenuBotones(app):

    # Definicion de Funciones que Llamaran los Botones

    # Cierra la Aplicacion
    def Close():
        msg = CTkMessagebox(
            title="Exit?",
            message="¿Desea Cerrar el Programa?",
            icon="question",
            option_1="Cancel",
            option_2="No",
            option_3="Yes",
        )
        response = msg.get()

        if response == "Yes":
            app.destroy()
        else:
            print("Enjoy")

    # Organiza los Botones en el Frame
    def OrganizateButtons(Bonton):
        Bonton.pack(side=ct.TOP)
        Bonton.pack(fill=ct.X)
        Bonton.pack(pady=1)

    # Define la Posicion en Pantalla de los Frames
    def ScreensPositions(Screen):
        Screen.pack(expand=True)
        Screen.pack(fill=ct.BOTH)
        Screen.pack(padx=2)

    # Abre el Frame Principal
    def OpenMainScreen():
        ScreensPositions(ScreenMainFrame)
        ScreenLuFrame.pack_forget()
        ScreenZFrame.pack_forget()

    # Abre el Frame de LU
    def OpenLuScreen():
        ScreensPositions(ScreenLuFrame)
        ScreenMainFrame.pack_forget()
        ScreenZFrame.pack_forget()

    # Abre el Frame de Pasos en Z
    def OpenZScreen():
        ScreensPositions(ScreenZFrame)
        ScreenLuFrame.pack_forget()
        ScreenMainFrame.pack_forget()

    # Frame donde se Ubican los Botonoes Correspondientes del Menu

    MenuFrame = ct.CTkFrame(
        master=app,
        fg_color="#FFFFFF",
        width=300,
        corner_radius=0,
    )

    MenuFrame.pack(side=ct.LEFT)
    MenuFrame.pack(fill=ct.Y)
    MenuFrame.pack_propagate(False)

    # Titulo del Menu como Boton

    TituloButton = ct.CTkButton(
        master=MenuFrame,
        text="CALCULADORA",
        height=80,
        fg_color="#0B2133",
        corner_radius=0,
        hover=False,
        font=("Times New Roman", 33),
    )

    TituloButton.pack(side=ct.TOP)
    TituloButton.pack(fill=ct.X)

    # Boton que Llevara al Frame Principal donde Se Ingresan los Datos

    ComenzarButton = ct.CTkButton(
        master=MenuFrame,
        text="Ingreso Datos",
        height=80,
        fg_color="#0B2133",
        corner_radius=0,
        hover=True,
        command=OpenMainScreen,
        font=("arial", 25),
    )

    OrganizateButtons(ComenzarButton)

    # Boton para Mostrar los Pasos de LU Correspondientes

    LUButton = ct.CTkButton(
        master=MenuFrame,
        text="Proceso 'LU'",
        height=80,
        fg_color="#0B2133",
        corner_radius=0,
        command=OpenLuScreen,
        hover=True,
        font=("arial", 25),
    )

    OrganizateButtons(LUButton)

    # Boton para Mostrar los Pasos de Z Correspondientes

    ZButton = ct.CTkButton(
        master=MenuFrame,
        text="Proceso 'Z'",
        height=80,
        fg_color="#0B2133",
        command=OpenZScreen,
        corner_radius=0,
        hover=True,
        font=("arial", 25),
    )

    OrganizateButtons(ZButton)

    # Boton para Mostrar Cerrar la Aplicacion

    CerrarButton = ct.CTkButton(
        master=MenuFrame,
        text="Cerrar",
        height=80,
        fg_color="#0B2133",
        corner_radius=0,
        hover=True,
        command=Close,
        hover_color="#33060E",
        font=("arial", 25),
    )

    OrganizateButtons(CerrarButton)

    FrameOcultar = ct.CTkFrame(master=MenuFrame, fg_color="#0B2133", corner_radius=0)

    FrameOcultar.pack(side=ct.TOP)
    FrameOcultar.pack(expand=True)
    FrameOcultar.pack(fill=ct.BOTH)

    # ________________________________Frame Principal Ingreso Datos__________________________________

    ScreenMainFrame = ct.CTkScrollableFrame(
        master=app,
        fg_color="white",
        corner_radius=0,
    )
    ScreensPositions(ScreenMainFrame)

    # ________________________________Frame Pasos de LU______________________________________________

    ScreenLuFrame = ct.CTkScrollableFrame(
        master=app,
        fg_color="white",
        corner_radius=0,
    )

    # ________________________________Frame Pasos de Z_______________________________________________

    ScreenZFrame = ct.CTkScrollableFrame(
        master=app,
        fg_color="white",
        corner_radius=0,
    )

    # Funcion que Genera los Frames al momento de Insercion de Datos

    Content.ScreenData(ScreenMainFrame, ScreenLuFrame, ScreenZFrame)
