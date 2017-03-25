#definition for adding two matrices
def addMatrix(X,Y):
     #Checking the dimensions
    if(len(X)==len(Y) and len(X[0])==len(Y[0])):   
        #Result Matrix
        summ=[]        
        # iterate through rows
        for i in range(len(X)):
            summ.append([])
            # iterate through columns
            for j in range(len(X[0])):
                summ[i] .append( X[i][j] + Y[i][j])
        return summ
    else:
        print("The iven Matrces cant be added")
            
###########################################################
    
#definition for subtracting two matrices
def subMatrix(X,Y):
    #Checking the dimensions
    if(len(X)==len(Y) and len(X[0])==len(Y[0])):
        #Result Matrix
        subm=[]        
        # iterate through rows
        for i in range(len(X)):
            subm.append([])
            # iterate through columns
            for j in range(len(X[0])):
                subm[i] .append( X[i][j]-Y[i][j])
        return subm
    else:
        print("The iven Matrces cant be added")
            
###########################################################
    
def multiplyMatrix(X,Y):
    rowX=len(X)
    colX=len(X[0])
    rowY=len(Y)
    colY=len(Y[0])
    if colX!=rowY:
      print("Matrix Multiplication is not possible")
      return

    # Create the result matrix
    # Dimensions would be rowX x colY
    Z=[[0 for row in range(colY)] for col in range(rowX)]
    for i in range(rowX):
        for j in range(colY):
            for k in range(colX):
                Z[i][j]+=X[i][k]*Y[k][j]
    return Z
        
###########################################################
    
#Function to find Determinrnt of a matrix
def det(l):
    try:
        #Checking if the matrix is squarre or not
        if len(l)==len(l[0]):
            #For 1x1 Mtrix
            if len(l)==1:
                return l[0][0]
            #for 2x2 Matrix
            elif len(l)==2:
                detm=(l[0][0]*l[1][1])-(l[0][1]*l[1][0])
                return detm
                
            #for All other Matrices
            else:
                #Creating  a list for the first row
                k=[]
                for ih in range(0,len(l)):
                    k.append(l[0][ih])
                detm=0
                #Sperating the minors in the form of list
                for i1 in range(0,len(l)):
                    mm=[]
                    for i in range(0,len(l)):
                        for j in range(0,len(l)):
                            if i!=0 and j!=i1:
                                mm.append(l[i][j])
                    #Converting the list in to matrix
                    kk=[]
                    count=0
                    for ik in range(0,int(len(mm)**0.5)):
                        kk.append([])
                        for jk in range(0,int(len(mm)**0.5)):
                            kk[ik].append(mm[count])
                            count+=1
                    #Using Recurssion 
                    p=det(kk)
                    #Summing up all of them
                    if(i1%2==0):
                        detm+=k[i1]*p
                    else:
                        detm+=(-k[i1])*p
                    
                return detm
        #if the given matrix is not a squre matrix
        else:
            print("Give a square Matrix")
    except:
        print("Something gone wrong")
    
###########################################################
    
 #Function for Trsanspose of a Matrix       
def trans(l):
    k=[]
    for i in range(0,len(l)):
        k.append([])
        for j in range(0,len(l[0])):
            k[i].append(l[j][i])
    return k
        
###########################################################
    
#Fuction for Inverse of a matrix
def inv(l):
    #Checking if the matrix is squarre or not
    if len(l)==len(l[0]):
        k=[]
        inv=[]
        cofac=[]
        #Creating  a list for the elements in the matrix
        for ih in range(0,len(l)):
            for jh in range(0,len(l)):
                k.append(l[ih][jh])
        #Iterating over the rows and columns
        for i1 in range(0,len(l)):
            for j1 in range(0,len(l)):
                mm=[]
                #Seperating Minors of the matrix and appending it in to list
                for i in range(0,len(l)):
                    for j in range(0,len(l)):
                        if i!=i1 and j!=j1:
                           mm.append(l[i][j])
                #Converting the list in to a matrix 
                kk=[]
                count=0
                for ik in range(0,int(len(mm)**0.5)):
                    kk.append([])
                    for jk in range(0,int(len(mm)**0.5)):
                        kk[ik].append(mm[count])
                        count+=1
                #Filling the cofactor Matrix
                cofac.append((-1)**(i1+j1)*(det(kk)/det(l)))
        count=0
        #Filling the Adjoint Matrixx
        for ik in range(0,int(len(cofac)**0.5)):
            inv.append([])
            for jk in range(0,int(len(cofac)**0.5)):
                inv[ik].append(cofac[count])
                count+=1
        #Inverse is transpose of the adjoint Matrix
        inv=trans(inv)
        return inv
    #Else if the Matrix is not square
    else:
        print("Give a square Matrix")
            
###########################################################
    
#Solve the equation Ax=b
def solve(A,b):
    if(det(A)!=0):
        #x=(A**-1)*(b)
        x=multiplyMatrix(inv(A),b)
        return x
    else:
        print("The given Matrix doesnt have a unoque solution")
                 
###########################################################
       
    
