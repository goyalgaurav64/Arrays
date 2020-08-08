def modifyMatrix(mat):
    row_flag=False
    col_flag=False
    m=len(mat)
    n=len(mat[0])
    for i in range(m):
        for j in range(n):
            if(i==0 and mat[i][j]==1):
                row_flag=True
            if(j==0 and mat[i][j]==1):
                col_flag=True
            if (mat[i][j] == 1) : 
                mat[0][j] = 1
                mat[i][0] = 1
    for i in range(1,len(mat)):
        for j in range(1,len(mat)+1):
            if(mat[i][0]==1 or mat[0][j]==1):
                mat[i][j]=1
    if row_flag==True:
        for i in range(len(mat)):
            mat[0][i]=1
    if col_flag==True:
        for i in range(len(mat)):
            mat[i][0]=1
    
    for i in range(m):
        for j in range(n):
            print(mat[i][j],end=' ')
        print()





if __name__ == "__main__":
    mat=[[1,0,0,1],
    [0,0,1,0],
    [0,0,0,0]]
    modifyMatrix(mat)