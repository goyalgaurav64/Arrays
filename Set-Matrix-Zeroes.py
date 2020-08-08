def setMatZero(mat):
    m=len(mat)
    n=len(mat[0])
    row=False
    col=False
    for i in range(m):
        for j in range(n):
            if i==0 and mat[i][j]==0:
                row=True
            if j==0 and mat[i][j]==0:
                col=True
            if mat[i][j]==0:
                mat[i][0]=0
                mat[0][j]=0
    for i in range(1,m):
        for j in range(1,n):
            if mat[0][j]==0 or mat[i][0]==0:
                mat[i][j]=0
    if row==True:
        for i in range(m):
            mat[0][i]=0
    if col==True:
        for i in range(n):
            mat[i][0]=0
    
    for i  in range(m):
        for j in range(n):
            print(mat[i][j],end=" ")
        print()

    





if __name__ == "__main__":
    mat=[[2,0,1],
    [3,5,2],
    [7,4,6]]
    setMatZero(mat)