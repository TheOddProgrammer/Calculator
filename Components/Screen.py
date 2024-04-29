import customtkinter as ct
import Components.Solution_X as SX


def PrincipalShowData(container):
    frame = ct.CTkFrame(
        master=container,
        fg_color="blue",
    )

    frame.pack(side=ct.LEFT)
    frame.pack(expand=True)
    frame.pack(fill=ct.BOTH)

    SX.FrameX(frame)
