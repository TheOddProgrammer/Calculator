import customtkinter as ct
import Components.Boton as Boton


def MainFrame(container):
    frame = ct.CTkFrame(
        master=container,
        fg_color="gray",
        height=1000,
        width=300,
    )

    frame.grid(row=0, column=0)

    Boton.Buttons(frame)
