import customtkinter as ct
import Components.Menu as Menu
import Components.Screen as Screen


def Ejecution(app):
    frame = ct.CTkFrame(
        master=app,
        fg_color="pink",
    )

    frame.pack(expand=True, fill=ct.BOTH)

    Menu.MainFrame(frame, app)
    Screen.PrincipalShowData(frame)
