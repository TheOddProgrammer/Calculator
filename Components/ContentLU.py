import customtkinter as ct
import Components.Logic as Lg


Matriz_L = Lg.Executable("L")
Matriz_U = Lg.Executable("U")
Matriz_B = Lg.Executable("B")
Matriz_A = Lg.Executable("A")


def Content(FrameMainLU):

    def OrdenContentMain(Cuadro):
        Cuadro.pack(expand=True)
        Cuadro.pack(side=ct.TOP)
        Cuadro.pack(fill=ct.BOTH)

    def Format(X):
        return "{:,.4f}".format(X)

    # _________________________________Formula LU__________________________________

    FrameLu = ct.CTkFrame(
        master=FrameMainLU,
        corner_radius=0,
        fg_color="#293C4B",
    )

    FrameInputInvisibleBig = ct.CTkFrame(
        master=FrameLu,
        fg_color="#293C4B",
        width=100,
        corner_radius=0,
    )

    LabelParOp = ct.CTkLabel(
        master=FrameLu,
        corner_radius=0,
        fg_color="#293C4B",
        text="L(",
        text_color="white",
        font=("Times New Roman", 70),
        anchor="center",
    )

    LabelParCl = ct.CTkLabel(
        master=FrameLu,
        corner_radius=0,
        fg_color="#293C4B",
        text=")",
        text_color="white",
        font=("Times New Roman", 70),
        anchor="center",
    )

    LabelX = ct.CTkLabel(
        master=FrameLu,
        corner_radius=0,
        fg_color="#293C4B",
        text="*",
        text_color="white",
        font=("Arial", 70),
        anchor="center",
    )

    LabelParOp1 = ct.CTkLabel(
        master=FrameLu,
        corner_radius=0,
        fg_color="#293C4B",
        text="U(",
        text_color="white",
        font=("Times New Roman", 70),
        anchor="center",
    )

    LabelParCl1 = ct.CTkLabel(
        master=FrameLu,
        corner_radius=0,
        fg_color="#293C4B",
        text=")",
        text_color="white",
        font=("Times New Roman", 70),
        anchor="center",
    )

    LabelParOp2 = ct.CTkLabel(
        master=FrameLu,
        corner_radius=0,
        fg_color="#293C4B",
        text="A(",
        text_color="white",
        font=("Times New Roman", 70),
        anchor="center",
    )

    LabelParCl2 = ct.CTkLabel(
        master=FrameLu,
        corner_radius=0,
        fg_color="#293C4B",
        text=")",
        text_color="white",
        font=("Times New Roman", 70),
        anchor="center",
    )

    LabelSame = ct.CTkLabel(
        master=FrameLu,
        corner_radius=0,
        fg_color="#293C4B",
        text="=",
        text_color="white",
        font=("Arial", 70),
        anchor="center",
    )

    txtL = "1   +   0   +   0\nL₂₁  +   1   +   0\nL₃₁  +   L₃₂ +   1"

    LabelDataL = ct.CTkLabel(
        master=FrameLu,
        text=txtL,
        font=("arial", 19),
        text_color="white",
    )

    txtU = "U₁₁  +   U₁₂ + U₁₃\n0    +   U₂₂ + U₂₃\n0    +    0    +  U₃₃"

    LabelDataU = ct.CTkLabel(
        master=FrameLu,
        text=txtU,
        font=("arial", 19),
        text_color="white",
    )

    txtB = "A₁₁  +   A₁₂ + A₁₃\nA₂₁    +   A₂₂ + A₂₃\nA₃₁    +   A₃₂   +  A₃₃"

    LabelDataB = ct.CTkLabel(
        master=FrameLu,
        text=txtB,
        font=("arial", 19),
        text_color="white",
    )

    OrdenContentMain(FrameLu)
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

    # _________________________________Hallando Valores de L & U__________________________________

    FrameFormula = ct.CTkFrame(
        master=FrameMainLU,
        fg_color="#293C4B",
        corner_radius=0,
    )

    txtFormula = (
        "En la Parte Superior Observamos la Formual que Realizando el Despeje Queda:"
        + "\n\nU₁₁ = A₁₁ ; U₁₁ = "
        + Format(Matriz_A[0][0])
        + "\nU₁₂ = A₁₂ ; U₁₂ = "
        + Format(Matriz_A[0][1])
        + "\nU₁₃ = A₁₃ ; U₁₃ = "
        + Format(Matriz_A[0][2])
        + "\nL₂₁ = (A₂₁/U₁₁) ; L₂₁ = "
        + Format(Matriz_A[1][0])
        + " / "
        + Format(Matriz_U[0][0])
        + " = "
        + Format(Matriz_L[1][0])
        + "\nL₃₁ = (A₃₁/U₁₁) ; L₂₁ = "
        + Format(Matriz_A[2][0])
        + " / "
        + Format(Matriz_U[0][0])
        + " = "
        + Format(Matriz_L[2][0])
        + "\nU₂₂ = (A₂₂ - L₂₁) * U₁₂ ; U₂₂ = ("
        + Format(Matriz_A[1][1])
        + " - "
        + Format(Matriz_L[1][0])
        + ") * "
        + Format(Matriz_U[0][1])
        + " = "
        + Format(Matriz_U[1][1])
        + "\nU₂₃ = (A₂₃ - L₂₁) * U₁₃ ; U₂₃ = ("
        + Format(Matriz_A[1][2])
        + " - "
        + Format(Matriz_L[1][0])
        + ") * "
        + Format(Matriz_U[0][2])
        + " = "
        + Format(Matriz_U[1][2])
        + "\nL₃₂ = {[(A₂₃ - L₃₁)*U₁₂]/U₂₂} ; L₃₂ = {[("
        + Format(Matriz_A[1][2])
        + " - "
        + Format(Matriz_L[2][0])
        + ")*"
        + Format(Matriz_U[0][1])
        + "]/"
        + Format(Matriz_U[1][1])
        + "} = "
        + Format(Matriz_L[2][1])
        + "\nU₃₃ = [(A₃₃ - L₃₁)*U₁₃] - (L₃₂*U₂₃) ; U₃₃ = [("
        + Format(Matriz_A[2][2])
        + " - "
        + Format(Matriz_L[2][0])
        + ")*"
        + Format(Matriz_U[0][2])
        + "] - ("
        + Format(Matriz_L[2][1])
        + "*"
        + Format(Matriz_U[1][2])
        + ") = "
        + Format(Matriz_U[2][2])
        + "\n\nAhora Realizaremos el Respectivo Reemplazo en la Matrices y Quedaría:"
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
    LabelFormula.pack(pady=20)

    # ___________________________________Reemplazo LU__________________________________

    FrameReemplazo = ct.CTkFrame(
        master=FrameMainLU,
        fg_color="#293C4B",
        corner_radius=0,
    )

    FrameInputInvisibleBigReemplazo = ct.CTkFrame(
        master=FrameReemplazo,
        fg_color="#293C4B",
        width=130,
        corner_radius=0,
    )
    LabelParOpReemplazo = ct.CTkLabel(
        master=FrameReemplazo,
        corner_radius=0,
        fg_color="#293C4B",
        text="L(",
        text_color="white",
        font=("Times New Roman", 60),
        anchor="center",
    )

    LabelParClReemplazo = ct.CTkLabel(
        master=FrameReemplazo,
        corner_radius=0,
        fg_color="#293C4B",
        text=")",
        text_color="white",
        font=("Times New Roman", 60),
        anchor="center",
    )

    LabelXReemplazo = ct.CTkLabel(
        master=FrameReemplazo,
        corner_radius=0,
        fg_color="#293C4B",
        text="*",
        text_color="white",
        font=("Arial", 60),
        anchor="center",
    )

    LabelParOp1Reemplazo = ct.CTkLabel(
        master=FrameReemplazo,
        corner_radius=0,
        fg_color="#293C4B",
        text="U(",
        text_color="white",
        font=("Times New Roman", 60),
        anchor="center",
    )

    LabelParCl1Reemplazo = ct.CTkLabel(
        master=FrameReemplazo,
        corner_radius=0,
        fg_color="#293C4B",
        text=")",
        text_color="white",
        font=("Times New Roman", 60),
        anchor="center",
    )

    LabelParOp2Reemplazo = ct.CTkLabel(
        master=FrameReemplazo,
        corner_radius=0,
        fg_color="#293C4B",
        text="A(",
        text_color="white",
        font=("Times New Roman", 60),
        anchor="center",
    )

    LabelParCl2Reemplazo = ct.CTkLabel(
        master=FrameReemplazo,
        corner_radius=0,
        fg_color="#293C4B",
        text=")",
        text_color="white",
        font=("Times New Roman", 60),
        anchor="center",
    )

    LabelSameReemplazo = ct.CTkLabel(
        master=FrameReemplazo,
        corner_radius=0,
        fg_color="#293C4B",
        text="=",
        text_color="white",
        font=("Arial", 60),
        anchor="center",
    )

    txtLReemplazo = (
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
        text=txtLReemplazo,
        font=("arial", 15),
        text_color="white",
    )

    txtUReemplazo = (
        Format(Matriz_U[0][0])
        + " + "
        + Format(Matriz_U[0][1])
        + " + "
        + Format(Matriz_U[0][2])
        + "\n"
        + Format(Matriz_U[1][0])
        + " + "
        + Format(Matriz_U[1][1])
        + " + "
        + Format(Matriz_U[1][2])
        + "\n"
        + Format(Matriz_U[2][0])
        + " + "
        + Format(Matriz_U[2][1])
        + " + "
        + Format(Matriz_U[2][2])
    )

    LabelDataUReemplazo = ct.CTkLabel(
        master=FrameReemplazo,
        text=txtUReemplazo,
        font=("arial", 15),
        text_color="white",
    )

    txtBReemplazo = (
        Format(Matriz_A[0][0])
        + " + "
        + Format(Matriz_A[0][1])
        + " + "
        + Format(Matriz_A[0][2])
        + "\n"
        + Format(Matriz_A[1][0])
        + " + "
        + Format(Matriz_A[1][1])
        + " + "
        + Format(Matriz_A[1][2])
        + "\n"
        + Format(Matriz_A[2][0])
        + " + "
        + Format(Matriz_A[2][1])
        + " + "
        + Format(Matriz_A[2][2])
    )

    LabelDataBReemplazo = ct.CTkLabel(
        master=FrameReemplazo,
        text=txtBReemplazo,
        font=("arial", 15),
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
