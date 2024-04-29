import customtkinter as ct
import Components.Boton as Boton


def MainFrame(container, app):
    frame = ct.CTkFrame(
        master=container,
        fg_color="black",
        bg_color="black",
    )

    frame.pack(side=ct.LEFT)
    frame.pack(fill=ct.Y)

    Boton.Buttons(frame, app)
