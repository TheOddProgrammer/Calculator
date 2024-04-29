import customtkinter as ct
import Components.Logic as Lg

Lg.Matriz_A = [[3, 2, 5], [10, -23, 3], [45, 12, -14]]
Lg.Matriz_B = [4, 8, 10]


def FrameX(screen):

    # Parte pasos En X
    pasosX = ct.CTkFrame(
        master=screen,
        fg_color="black",
        bg_color="black",
    )

    pasosX.pack(expand=True)
    pasosX.pack(padx=2)
    pasosX.pack(fill=ct.BOTH)

    # Pasos donde Se Ingresan Datos
    frameInsert = ct.CTkFrame(
        master=pasosX,
        fg_color="black",
        height=300,
    )

    frameInsert.pack(expand=True)
    frameInsert.pack(fill=ct.X)
    frameInsert.pack_propagate(False)

    # Pasos donde se Realiza Todo el Proceso
    frameProgress = ct.CTkFrame(
        master=pasosX,
        fg_color="black",
        height=300,
    )

    txt1 = ()

    label1 = ct.CTkLabel(
        master=frameProgress,
        text=txt1,
        font=("monocraft", 25),
        fg_color="pink",
    )
    label1.pack(side=ct.TOP)
    label1.pack(fill=ct.BOTH)
    label1.pack(expand=True)

    # Se Muestra la Compracion de las Ecuaciones con Todo Mostrado
    frameProgress.pack(expand=True)
    frameProgress.pack(fill=ct.X)
    frameProgress.pack_propagate(False)

    frameComparation = ct.CTkFrame(
        master=pasosX,
        fg_color="black",
    )

    frameComparation.pack(expand=True)
    frameComparation.pack(fill=ct.BOTH)
    frameComparation.pack_propagate(False)

    Matriz_B = Lg.Executable("B")

    txt2 = (
        "Ahora reemplazando y Realizando el \nRespectivo Procedimeinto Tenemos:\n"
        + str(Matriz_B[0])
        + " = "
        + str(Matriz_B[0])
        + "\n"
        + str(Matriz_B[1])
        + " = "
        + str(Matriz_B[1])
        + "\n"
        + str(Matriz_B[2])
        + " = "
        + str(Matriz_B[2])
    )

    label2 = ct.CTkLabel(
        master=frameComparation,
        text=txt2,
        font=("monocraft", 25),
        fg_color="black",
    )
    label2.pack(side=ct.TOP)
    label2.pack(fill=ct.Y)
    label2.pack(expand=True)
