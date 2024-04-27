import customtkinter as ct
import Components.Menu as Menu
import Components.Screen as Screen


def Ejecution(app):
    frame = ct.CTkFrame(
        master=app,
        width=2000,
        height=2000,
        fg_color="pink",
    )
    frame.pack(padx=0, pady=0)
    frame.place(
        relx=0,
        rely=0,
    )

    Menu.MainFrame(frame)
    Screen.ShowData(frame)
