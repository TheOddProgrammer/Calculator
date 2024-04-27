import customtkinter as ct
import tkinter as tk


def Buttons(frame):
    minFrame(frame)
    Principal(frame)
    StepsLU(frame)
    StepsZ(frame)
    Close(frame)


def minFrame(frame):
    boton = ct.CTkButton(
        master=frame,
        fg_color="black",
        width=300,
        height=100,
        font=("monocraft", 30),
        text="Calculadora LU",
        corner_radius=0,
        hover=False,
    )

    boton.pack(padx=0, pady=0)


def Principal(frame):

    def hide():
        boton.pack_forget()

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
        command=hide,
    )

    boton.pack(padx=0, pady=0)


def StepsLU(frame):
    boton = ct.CTkButton(
        master=frame,
        text="Pasos L",
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


def Close(frame):
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
        hover_color="red",
    )

    boton.pack(padx=0, pady=0)
