import customtkinter as ct
import Components.Boton as Boton


def ShowData(container):
    frame = ct.CTkFrame(
        master=container,
        fg_color="white",
        width=2000,
        height=700,
    )

    frame.grid(row=0, column=1)
