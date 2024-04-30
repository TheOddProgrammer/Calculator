import customtkinter as ct
import Components.Logic as Lg

Matriz_L = Lg.Executable("L")
Matriz_Z = Lg.Executable("Z")
Matriz_B = Lg.Executable("B")


def Content(FrameMainZ):

    def OrdenContentMain(Cuadro):
        Cuadro.pack(expand=True)
        Cuadro.pack(side=ct.TOP)
        Cuadro.pack(fill=ct.BOTH)

    def Format(X):
        return "{:,.4f}".format(X)

    # ______________________________Formula Para Hallar Z_____________________________

    FrameZ = ct.CTkFrame(
        master=FrameMainZ,
        corner_radius=0,
        fg_color="#293C4B",
    )

    FrameInputInvisibleBig = ct.CTkFrame(
        master=FrameZ,
        fg_color="#293C4B",
        width=250,
        corner_radius=0,
    )

    LabelParOp = ct.CTkLabel(
        master=FrameZ,
        corner_radius=0,
        fg_color="#293C4B",
        text="L(",
        text_color="white",
        font=("Times New Roman", 70),
        anchor="center",
    )

    LabelParCl = ct.CTkLabel(
        master=FrameZ,
        corner_radius=0,
        fg_color="#293C4B",
        text=")",
        text_color="white",
        font=("Times New Roman", 70),
        anchor="center",
    )

    LabelX = ct.CTkLabel(
        master=FrameZ,
        corner_radius=0,
        fg_color="#293C4B",
        text="*",
        text_color="white",
        font=("Arial", 70),
        anchor="center",
    )

    LabelParOp1 = ct.CTkLabel(
        master=FrameZ,
        corner_radius=0,
        fg_color="#293C4B",
        text="Z(",
        text_color="white",
        font=("Times New Roman", 70),
        anchor="center",
    )

    LabelParCl1 = ct.CTkLabel(
        master=FrameZ,
        corner_radius=0,
        fg_color="#293C4B",
        text=")",
        text_color="white",
        font=("Times New Roman", 70),
        anchor="center",
    )

    LabelParOp2 = ct.CTkLabel(
        master=FrameZ,
        corner_radius=0,
        fg_color="#293C4B",
        text="B(",
        text_color="white",
        font=("Times New Roman", 70),
        anchor="center",
    )

    LabelParCl2 = ct.CTkLabel(
        master=FrameZ,
        corner_radius=0,
        fg_color="#293C4B",
        text=")",
        text_color="white",
        font=("Times New Roman", 70),
        anchor="center",
    )

    LabelSame = ct.CTkLabel(
        master=FrameZ,
        corner_radius=0,
        fg_color="#293C4B",
        text="=",
        text_color="white",
        font=("Arial", 70),
        anchor="center",
    )

    txtL = "1   +   0   +   0\nL₂₁  +   1   +   0\nL₃₁  +   L₃₂ +   1"

    LabelDataL = ct.CTkLabel(
        master=FrameZ,
        text=txtL,
        font=("arial", 19),
        text_color="white",
    )

    txtU = "Z₁\nZ₂\nZ₃"

    LabelDataU = ct.CTkLabel(
        master=FrameZ,
        text=txtU,
        font=("arial", 19),
        text_color="white",
    )

    txtB = "B₁\nB₂\nB₃"

    LabelDataB = ct.CTkLabel(
        master=FrameZ,
        text=txtB,
        font=("arial", 19),
        text_color="white",
    )

    OrdenContentMain(FrameZ)
    FrameInputInvisibleBig.pack(side=ct.LEFT)
    LabelParOp.pack(side=ct.LEFT)
    LabelParOp.pack(padx=2)
    LabelDataL.pack(side=ct.LEFT)
    LabelParCl.pack(side=ct.LEFT)
    LabelParCl.pack(padx=2)
    LabelX.pack(side=ct.LEFT)
    LabelX.pack(padx=2)
    LabelParOp1.pack(side=ct.LEFT)
    LabelParOp1.pack(padx=2)
    LabelDataU.pack(side=ct.LEFT)
    LabelParCl1.pack(side=ct.LEFT)
    LabelParCl1.pack(padx=2)
    LabelSame.pack(side=ct.LEFT)
    LabelSame.pack(padx=2)
    LabelParOp2.pack(side=ct.LEFT)
    LabelParOp2.pack(padx=2)
    LabelDataB.pack(side=ct.LEFT)
    LabelParCl2.pack(side=ct.LEFT)
    LabelParCl2.pack(padx=2)

    # ______________________________Despeje Z__________________________________________
    FrameFormula = ct.CTkFrame(
        master=FrameMainZ,
        fg_color="#293C4B",
        corner_radius=0,
    )

    txtFormula = (
        "Despues de la Respectiva Formula Despejamos, Obteniendo: \n\nZ₁ = B₁/L₁₁ ; Z₁ = "
        + Format(Matriz_B[0])
        + "\nZ₂ = B₂ - (L₂₁*Z₁) ; Z₂ = "
        + Format(Matriz_B[1])
        + " - ("
        + Format(Matriz_L[1][0])
        + "*"
        + Format(Matriz_Z[0])
        + ") = "
        + Format(Matriz_Z[1])
        + "\nZ₃ = B₃ - (L₃₁*Z₁) - (L₃₂*Z₂) ; Z₃ = "
        + Format(Matriz_B[2])
        + " - ("
        + Format(Matriz_L[2][0])
        + "*"
        + Format(Matriz_Z[0])
        + ") - ("
        + Format(Matriz_L[2][1])
        + "*"
        + Format(Matriz_Z[1])
        + ") = "
        + Format(Matriz_Z[2])
        + "\n\nComenzamos a Realizar el templazo y Encontramos las Matrices:"
    )

    LabelFormula = ct.CTkLabel(
        master=FrameFormula,
        font=("arial", 19),
        text=txtFormula,
        anchor="ne",
        text_color="white",
    )

    OrdenContentMain(FrameFormula)
    LabelFormula.pack(side=ct.TOP)
    # ______________________________Reemplazo Formula de Z_____________________________

    FrameReemplazo = ct.CTkFrame(
        master=FrameMainZ,
        fg_color="#293C4B",
        corner_radius=0,
    )

    FrameInputInvisibleBigReemplazo = ct.CTkFrame(
        master=FrameReemplazo,
        fg_color="#293C4B",
        width=170,
        corner_radius=0,
    )
    LabelParOpReemplazo = ct.CTkLabel(
        master=FrameReemplazo,
        corner_radius=0,
        fg_color="#293C4B",
        text="L(",
        text_color="white",
        font=("Times New Roman", 70),
        anchor="center",
    )

    LabelParClReemplazo = ct.CTkLabel(
        master=FrameReemplazo,
        corner_radius=0,
        fg_color="#293C4B",
        text=")",
        text_color="white",
        font=("Times New Roman", 70),
        anchor="center",
    )

    LabelXReemplazo = ct.CTkLabel(
        master=FrameReemplazo,
        corner_radius=0,
        fg_color="#293C4B",
        text="*",
        text_color="white",
        font=("Arial", 70),
        anchor="center",
    )

    LabelParOp1Reemplazo = ct.CTkLabel(
        master=FrameReemplazo,
        corner_radius=0,
        fg_color="#293C4B",
        text="Z(",
        text_color="white",
        font=("Times New Roman", 70),
        anchor="center",
    )

    LabelParCl1Reemplazo = ct.CTkLabel(
        master=FrameReemplazo,
        corner_radius=0,
        fg_color="#293C4B",
        text=")",
        text_color="white",
        font=("Times New Roman", 70),
        anchor="center",
    )

    LabelParOp2Reemplazo = ct.CTkLabel(
        master=FrameReemplazo,
        corner_radius=0,
        fg_color="#293C4B",
        text="B(",
        text_color="white",
        font=("Times New Roman", 70),
        anchor="center",
    )

    LabelParCl2Reemplazo = ct.CTkLabel(
        master=FrameReemplazo,
        corner_radius=0,
        fg_color="#293C4B",
        text=")",
        text_color="white",
        font=("Times New Roman", 70),
        anchor="center",
    )

    LabelSameReemplazo = ct.CTkLabel(
        master=FrameReemplazo,
        corner_radius=0,
        fg_color="#293C4B",
        text="=",
        text_color="white",
        font=("Arial", 70),
        anchor="center",
    )

    txtZReemplazo = (
        Format(Matriz_L[0][0])
        + " + "
        + Format(Matriz_L[0][1])
        + " + "
        + Format(Matriz_L[0][2])
        + "\n"
        + Format(Matriz_L[1][0])
        + " + "
        + Format(Matriz_L[1][1])
        + " + "
        + Format(Matriz_L[1][2])
        + "\n"
        + Format(Matriz_L[2][0])
        + " + "
        + Format(Matriz_L[2][1])
        + " + "
        + Format(Matriz_L[2][2])
    )

    LabelDataLReemplazo = ct.CTkLabel(
        master=FrameReemplazo,
        text=txtZReemplazo,
        font=("arial", 19),
        text_color="white",
    )

    txtZReemplazo = (
        Format(Matriz_Z[0]) + "\n" + Format(Matriz_Z[1]) + "\n" + Format(Matriz_Z[2])
    )

    LabelDataUReemplazo = ct.CTkLabel(
        master=FrameReemplazo,
        text=txtZReemplazo,
        font=("arial", 19),
        text_color="white",
    )

    txtBReemplazo = (
        Format(Matriz_B[0]) + "\n" + Format(Matriz_B[1]) + "\n" + Format(Matriz_B[2])
    )

    LabelDataBReemplazo = ct.CTkLabel(
        master=FrameReemplazo,
        text=txtBReemplazo,
        font=("arial", 19),
        text_color="white",
    )

    OrdenContentMain(FrameReemplazo)
    FrameInputInvisibleBigReemplazo.pack(side=ct.LEFT)
    LabelParOpReemplazo.pack(side=ct.LEFT)
    LabelParOpReemplazo.pack(padx=2)
    LabelDataLReemplazo.pack(side=ct.LEFT)
    LabelParClReemplazo.pack(side=ct.LEFT)
    LabelParClReemplazo.pack(padx=2)
    LabelXReemplazo.pack(side=ct.LEFT)
    LabelXReemplazo.pack(padx=2)
    LabelParOp1Reemplazo.pack(side=ct.LEFT)
    LabelParOp1Reemplazo.pack(padx=2)
    LabelDataUReemplazo.pack(side=ct.LEFT)
    LabelParCl1Reemplazo.pack(side=ct.LEFT)
    LabelParCl1Reemplazo.pack(padx=2)
    LabelSameReemplazo.pack(side=ct.LEFT)
    LabelSameReemplazo.pack(padx=2)
    LabelParOp2Reemplazo.pack(side=ct.LEFT)
    LabelParOp2Reemplazo.pack(padx=2)
    LabelDataBReemplazo.pack(side=ct.LEFT)
    LabelParCl2Reemplazo.pack(side=ct.LEFT)
    LabelParCl2Reemplazo.pack(padx=2)
