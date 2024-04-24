#Funcion de Formato
def F(numero):
    return (round(numero,4))

#Funcion de Ejecucion Principal
def Executable(X):
    Matriz_B = [9,7,12]
    Matriz_A = [[4,-2,-1],[5,1,-1],[1,2,-1]]
    Matriz_U = LU(Matriz_A,"U")
    Matriz_L = LU(Matriz_A,"L")
    Matriz_Z = UB(Matriz_L,Matriz_B)
    Matriz_X = UZ(Matriz_U,Matriz_Z)
    
    if X == "A":
        return Matriz_A
    elif X == "U":
        return Matriz_U
    elif X == "L":
        return Matriz_L
    elif X == "Z":
        return Matriz_Z
    elif X == "X":
        return Matriz_X
    else:
        return Matriz_B

#Funcion Para Encontrar Valores de L y U
def LU(Matriz_A,N):
    U11 = F(Matriz_A[0][0])
    U12 = F(Matriz_A[0][1])
    U13 = F(Matriz_A[0][2])
    
    L21 = F(Matriz_A[1][0]/U11)
    U22 = F(Matriz_A[1][1]-(L21*U12))
    U23 = F(Matriz_A[1][2]-(L21*U13))
    
    L31 = F(Matriz_A[2][0]/U11)
    L32 = F((Matriz_A[2][1]-(L31*U12))/U22)
    U33 = F((Matriz_A[2][2]-(L31*U13) - (L32*U23)))
    
    Matriz_L = [[1,0,0],[L21,1,0],[L31,L32,1]]
    Matriz_U = [[U11,U12,U13],[0,U22,U23],[0,0,U33]]
    
    if N == "L":
        return Matriz_L
    else:
        return Matriz_U

#Funcion para Encontrar Valores de Z
def UB(Matriz_L,Matriz_B):
    Z1 = F(Matriz_B[0])
    Z2 = F(Matriz_B[1] - (Matriz_L[1][0]*Z1))
    Z3 = F(Matriz_B[2] - (Matriz_L[2][0]*Z1) - (Matriz_L[2][1]*Z2))
    
    Matriz_Z = [Z1, Z2, Z3]
    
    return Matriz_Z

#Funcion para Encontrar Valores de X
def UZ(Matriz_U,Matriz_Z):
    X3 = F(Matriz_Z[2]/Matriz_U[2][2])
    X2 = F((Matriz_Z[1]-(Matriz_U[1][2]*X3))/Matriz_U[1][1])
    X1 = F((Matriz_Z[0]-(Matriz_U[0][2]*X3)-(Matriz_U[0][1]*X2))/Matriz_U[0][0])
    
    Matriz_X = [X1, X2, X3]
    
    return Matriz_X