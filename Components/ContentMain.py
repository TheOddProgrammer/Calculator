import customtkinter as ct
import Components.Logic as Lg
from CTkMessagebox import CTkMessagebox

# Definicion Variables Globales y Sobreescritura de las Ya Declaradas en Documento Logic
MatrizA = [[50, 4, 25], [20, 10, 10], [20, 20, 40]]
MatrizB = [20, 20, 9]
Lg.Matriz_A = MatrizA
Lg.Matriz_B = MatrizB


# Funcion Principal
def ScreenData(frame, FrameMainLu, FrameMainZ):

    # Limpia la Entrada de Texto
    def DeleteData():
        Entry00.delete(0, "end")
        Entry01.delete(0, "end")
        Entry02.delete(0, "end")
        Entry10.delete(0, "end")
        Entry11.delete(0, "end")
        Entry12.delete(0, "end")
        Entry20.delete(0, "end")
        Entry21.delete(0, "end")
        Entry22.delete(0, "end")
        EntryB1.delete(0, "end")
        EntryB2.delete(0, "end")
        EntryB3.delete(0, "end")

    # Crea los Frames de la Data
    def createFrames():

        # Declarando Matrices Usadas
        Matriz_L = Lg.Executable("L")
        Matriz_U = Lg.Executable("U")
        Matriz_B = Lg.Executable("B")
        Matriz_Z = Lg.Executable("Z")
        Matriz_X = Lg.Executable("X")
        Matriz_A = Lg.Executable("A")

        # Frame principal de Datos LU
        FrameShowLU = ct.CTkFrame(
            master=frame,
            fg_color="#293C4B",
            corner_radius=0,
        )

        # Frame para Acomodar
        FrameInputInvisibleSmall = ct.CTkFrame(
            master=FrameShowLU,
            fg_color="#293C4B",
            width=80,
            corner_radius=0,
        )

        LabelParOp = ct.CTkLabel(
            master=FrameShowLU,
            corner_radius=0,
            fg_color="#293C4B",
            text="L(",
            text_color="white",
            font=("Times New Roman", 70),
            anchor="center",
        )

        LabelParCl = ct.CTkLabel(
            master=FrameShowLU,
            corner_radius=0,
            fg_color="#293C4B",
            text=")",
            text_color="white",
            font=("Times New Roman", 70),
            anchor="center",
        )

        LabelX = ct.CTkLabel(
            master=FrameShowLU,
            corner_radius=0,
            fg_color="#293C4B",
            text="*",
            text_color="white",
            font=("Arial", 70),
            anchor="center",
        )

        LabelParOp1 = ct.CTkLabel(
            master=FrameShowLU,
            corner_radius=0,
            fg_color="#293C4B",
            text="U(",
            text_color="white",
            font=("Times New Roman", 70),
            anchor="center",
        )

        LabelParCl1 = ct.CTkLabel(
            master=FrameShowLU,
            corner_radius=0,
            fg_color="#293C4B",
            text=")",
            text_color="white",
            font=("Times New Roman", 70),
            anchor="center",
        )

        LabelParOp2 = ct.CTkLabel(
            master=FrameShowLU,
            corner_radius=0,
            fg_color="#293C4B",
            text="B(",
            text_color="white",
            font=("Times New Roman", 70),
            anchor="center",
        )

        LabelParCl2 = ct.CTkLabel(
            master=FrameShowLU,
            corner_radius=0,
            fg_color="#293C4B",
            text=")",
            text_color="white",
            font=("Times New Roman", 70),
            anchor="center",
        )

        LabelSame = ct.CTkLabel(
            master=FrameShowLU,
            corner_radius=0,
            fg_color="#293C4B",
            text="=",
            text_color="white",
            font=("Arial", 70),
            anchor="center",
        )

        txtL = (
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

        LabelDataL = ct.CTkLabel(
            master=FrameShowLU,
            text=txtL,
            font=("arial", 19),
            text_color="white",
        )

        txtU = (
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

        LabelDataU = ct.CTkLabel(
            master=FrameShowLU,
            text=txtU,
            font=("arial", 19),
            text_color="white",
        )

        txtB = (
            Format(Matriz_B[0])
            + "\n"
            + Format(Matriz_B[1])
            + "\n"
            + Format(Matriz_B[2])
        )

        LabelDataB = ct.CTkLabel(
            master=FrameShowLU,
            text=txtB,
            font=("arial", 19),
            text_color="white",
        )

        OrdenContentMain(FrameShowLU)
        FrameShowLU.pack(pady=1)
        FrameInputInvisibleSmall.pack(side=ct.LEFT)
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

        # __________________________________Show Data Z_________________________________

        FrameShowZ = ct.CTkFrame(
            master=frame,
            fg_color="#293C4B",
            corner_radius=0,
        )

        txtZ = (
            "Z₁ = "
            + Format(Matriz_Z[0])
            + "\nZ₂ = "
            + Format(Matriz_Z[1])
            + "\nZ₃ = "
            + Format(Matriz_Z[2])
        )

        LabelValuesZ = ct.CTkLabel(
            master=FrameShowZ,
            text=txtZ,
            font=("arial", 19),
            anchor="w",
            text_color="white",
        )

        OrdenContentMain(FrameShowZ)
        LabelValuesZ.pack(side=ct.TOP)
        LabelValuesZ.pack(pady=20)

        # __________________________________Show Data X_________________________________

        FrameShowX = ct.CTkFrame(
            master=frame,
            fg_color="#293C4B",
            corner_radius=0,
        )

        txtX = (
            "X₁ = "
            + Format(Matriz_X[0])
            + "\nX₂ = "
            + Format(Matriz_X[1])
            + "\nX₃ = "
            + Format(Matriz_X[2])
        )

        LabelValuesX = ct.CTkLabel(
            master=FrameShowX,
            text=txtX,
            font=("arial", 19),
            anchor="w",
            text_color="white",
        )

        OrdenContentMain(FrameShowX)
        LabelValuesX.pack(side=ct.TOP)
        LabelValuesX.pack(pady=20)

        # __________________________________Show Data Comparation________________________

        FrameShowComparation = ct.CTkFrame(
            master=frame,
            fg_color="#293C4B",
            corner_radius=0,
        )

        txtComparation = (
            "① ("
            + Format(Matriz_A[0][0])
            + "*"
            + Format(Matriz_X[0])
            + ") + ("
            + Format(Matriz_A[0][1])
            + "*"
            + Format(Matriz_X[1])
            + ") + ("
            + Format(Matriz_A[0][2])
            + "*"
            + Format(Matriz_X[2])
            + ") = "
            + Format(Matriz_B[0])
            + " ; "
            + Format(Matriz_B[0])
            + " = "
            + Format(Matriz_B[0])
            + "\n"
            + "② ("
            + Format(Matriz_A[1][0])
            + "*"
            + Format(Matriz_X[0])
            + ") + ("
            + Format(Matriz_A[1][1])
            + "*"
            + Format(Matriz_X[1])
            + ") + ("
            + Format(Matriz_A[1][2])
            + "*"
            + Format(Matriz_X[2])
            + ") = "
            + Format(Matriz_B[1])
            + " ; "
            + Format(Matriz_B[1])
            + " = "
            + Format(Matriz_B[1])
            + "\n"
            + "③ ("
            + Format(Matriz_A[2][0])
            + "*"
            + Format(Matriz_X[0])
            + ") + ("
            + Format(Matriz_A[2][1])
            + "*"
            + Format(Matriz_X[1])
            + ") + ("
            + Format(Matriz_A[2][2])
            + "*"
            + Format(Matriz_X[2])
            + ") = "
            + Format(Matriz_B[2])
            + " ; "
            + Format(Matriz_B[2])
            + " = "
            + Format(Matriz_B[2])
        )

        LabelValuesComparation = ct.CTkLabel(
            master=FrameShowComparation,
            text=txtComparation,
            font=("arial", 19),
            anchor="w",
            text_color="white",
        )

        OrdenContentMain(FrameShowComparation)
        LabelValuesComparation.pack(side=ct.TOP)
        LabelValuesComparation.pack(pady=20)

    def DefinirDatos():
        try:
            MatrizA[0][0] = float(A01.get())
            MatrizA[0][1] = float(A02.get())
            MatrizA[0][2] = float(A03.get())
            MatrizA[1][0] = float(A11.get())
            MatrizA[1][1] = float(A12.get())
            MatrizA[1][2] = float(A13.get())
            MatrizA[2][0] = float(A21.get())
            MatrizA[2][1] = float(A22.get())
            MatrizA[2][2] = float(A23.get())
            MatrizB[0] = float(B01.get())
            MatrizB[1] = float(B02.get())
            MatrizB[2] = float(B03.get())
        except ValueError:
            CTkMessagebox(
                title="Error",
                message="- Caracter No Permitido\n- Celda(s) Vacia\nVer Manual Recomendado",
                icon="cancel",
            )
        else:
            createFrames()
            Content(FrameMainLu)
            ContentZ(FrameMainZ)

    def Content(FrameMainLU):

        Matriz_L = Lg.Executable("L")
        Matriz_U = Lg.Executable("U")
        Matriz_A = Lg.Executable("A")

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
        FrameLu.pack(pady=1)
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

    def ContentZ(FrameMainZ):

        Matriz_L = Lg.Executable("L")
        Matriz_Z = Lg.Executable("Z")
        Matriz_B = Lg.Executable("B")

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
        FrameZ.pack(pady=1)
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
            Format(Matriz_Z[0])
            + "\n"
            + Format(Matriz_Z[1])
            + "\n"
            + Format(Matriz_Z[2])
        )

        LabelDataUReemplazo = ct.CTkLabel(
            master=FrameReemplazo,
            text=txtZReemplazo,
            font=("arial", 19),
            text_color="white",
        )

        txtBReemplazo = (
            Format(Matriz_B[0])
            + "\n"
            + Format(Matriz_B[1])
            + "\n"
            + Format(Matriz_B[2])
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

    def Format(X):
        return "{:,.4f}".format(X)

    # Function in Archive
    def OrdenContentMain(Cuadro):
        Cuadro.pack(expand=True)
        Cuadro.pack(side=ct.TOP)
        Cuadro.pack(fill=ct.BOTH)

    # ____________________________Primer Frame de Ingreso de Datos_____________________________

    FrameInputData = ct.CTkFrame(
        master=frame,
        fg_color="#293C4B",
        corner_radius=0,
    )

    LabelKey = ct.CTkLabel(
        master=FrameInputData,
        corner_radius=0,
        fg_color="#293C4B",
        text="{",
        text_color="white",
        font=("Times New Roman", 150),
        anchor="center",
    )

    FrameInputInvisibleBig = ct.CTkFrame(
        master=FrameInputData,
        fg_color="#293C4B",
        height=200,
        width=250,
        corner_radius=0,
    )

    FrameInputContainer = ct.CTkFrame(
        master=FrameInputData,
        fg_color="#293C4B",
        height=190,
        width=400,
    )

    A01 = ct.StringVar()
    A02 = ct.StringVar()
    A03 = ct.StringVar()
    A11 = ct.StringVar()
    A12 = ct.StringVar()
    A13 = ct.StringVar()
    A21 = ct.StringVar()
    A22 = ct.StringVar()
    A23 = ct.StringVar()
    B01 = ct.StringVar()
    B02 = ct.StringVar()
    B03 = ct.StringVar()

    # Objetos Para Leer los
    Entry00 = ct.CTkEntry(
        master=FrameInputContainer, width=50, bg_color="#293C4B", textvariable=A01
    )
    Entry01 = ct.CTkEntry(
        master=FrameInputContainer, width=50, bg_color="#293C4B", textvariable=A02
    )
    Entry02 = ct.CTkEntry(
        master=FrameInputContainer, width=50, bg_color="#293C4B", textvariable=A03
    )
    Entry10 = ct.CTkEntry(
        master=FrameInputContainer, width=50, bg_color="#293C4B", textvariable=A11
    )
    Entry11 = ct.CTkEntry(
        master=FrameInputContainer, width=50, bg_color="#293C4B", textvariable=A12
    )
    Entry12 = ct.CTkEntry(
        master=FrameInputContainer, width=50, bg_color="#293C4B", textvariable=A13
    )
    Entry20 = ct.CTkEntry(
        master=FrameInputContainer, width=50, bg_color="#293C4B", textvariable=A21
    )
    Entry21 = ct.CTkEntry(
        master=FrameInputContainer, width=50, bg_color="#293C4B", textvariable=A22
    )
    Entry22 = ct.CTkEntry(
        master=FrameInputContainer, width=50, bg_color="#293C4B", textvariable=A23
    )
    EntryB1 = ct.CTkEntry(
        master=FrameInputContainer, width=50, bg_color="#293C4B", textvariable=B01
    )
    EntryB2 = ct.CTkEntry(
        master=FrameInputContainer, width=50, bg_color="#293C4B", textvariable=B02
    )
    EntryB3 = ct.CTkEntry(
        master=FrameInputContainer, width=50, bg_color="#293C4B", textvariable=B03
    )

    LabelX10 = ct.CTkLabel(
        master=FrameInputContainer,
        width=30,
        text="x₁ +",
        text_color="white",
        font=("arial", 20),
        fg_color="#293C4B",
    )
    LabelX20 = ct.CTkLabel(
        master=FrameInputContainer,
        width=30,
        text="x₂ +",
        text_color="white",
        font=("arial", 20),
        fg_color="#293C4B",
    )
    LabelX30 = ct.CTkLabel(
        master=FrameInputContainer,
        width=30,
        text="x₃ =",
        text_color="white",
        font=("arial", 20),
        fg_color="#293C4B",
    )

    LabelX11 = ct.CTkLabel(
        master=FrameInputContainer,
        width=30,
        text="x₁ +",
        text_color="white",
        font=("arial", 20),
        fg_color="#293C4B",
    )
    LabelX21 = ct.CTkLabel(
        master=FrameInputContainer,
        width=30,
        text="x₂ +",
        text_color="white",
        font=("arial", 20),
        fg_color="#293C4B",
    )
    LabelX31 = ct.CTkLabel(
        master=FrameInputContainer,
        width=30,
        text="x₃ =",
        text_color="white",
        font=("arial", 20),
        fg_color="#293C4B",
    )

    LabelX12 = ct.CTkLabel(
        master=FrameInputContainer,
        width=30,
        text="x₁ +",
        text_color="white",
        font=("arial", 20),
        fg_color="#293C4B",
    )
    LabelX22 = ct.CTkLabel(
        master=FrameInputContainer,
        width=30,
        text="x₂ +",
        text_color="white",
        font=("arial", 20),
        fg_color="#293C4B",
    )
    LabelX32 = ct.CTkLabel(
        master=FrameInputContainer,
        width=30,
        text="x₃ =",
        text_color="white",
        font=("arial", 20),
        fg_color="#293C4B",
    )

    Entry00.grid(row=0, column=0)
    LabelX10.grid(row=0, column=1)
    Entry01.grid(row=0, column=2)
    LabelX20.grid(row=0, column=3)
    Entry02.grid(row=0, column=4)
    LabelX30.grid(row=0, column=5)
    EntryB1.grid(row=0, column=6)

    Entry10.grid(row=1, column=0)
    LabelX11.grid(row=1, column=1)
    Entry11.grid(row=1, column=2)
    LabelX21.grid(row=1, column=3)
    Entry12.grid(row=1, column=4)
    LabelX31.grid(row=1, column=5)
    EntryB2.grid(row=1, column=6)

    Entry20.grid(row=2, column=0)
    LabelX12.grid(row=2, column=1)
    Entry21.grid(row=2, column=2)
    LabelX22.grid(row=2, column=3)
    Entry22.grid(row=2, column=4)
    LabelX32.grid(row=2, column=5)
    EntryB3.grid(row=2, column=6)

    # Finalizacion Objetos Lectura

    OrdenContentMain(FrameInputData)
    FrameInputInvisibleBig.pack(side=ct.LEFT)
    LabelKey.pack(side=ct.LEFT)
    LabelKey.pack(fill=ct.Y)
    FrameInputContainer.pack(side=ct.LEFT)

    ButtonExecute = ct.CTkButton(
        master=FrameInputData, text="Ejecutar", command=DefinirDatos
    ).pack(side=ct.LEFT, padx=20)

    ButtonClear = ct.CTkButton(
        master=FrameInputData, text="Limpiar", command=DeleteData
    ).pack(side=ct.LEFT, padx=20)
    # __________________________________Show Data LU________________________________
