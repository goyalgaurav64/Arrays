def modifyMatrix(mat):
    r=len(mat)
    c=len(mat[0])
    row=[0]*r
    col=[0]*c
    for i in range(r):
        for j in range(c):
            if(mat[i][j]==1):
                row[i]=1
                col[j]=1
    for i in range(r):
        for j in range(c):
            if(row[i]==1 or col[j]==1):
                mat[i][j]=1
    
    for i in range(r):
        for j in range(c):
            print(mat[i][j],end=' ')
        print()

    # Time Complexity=O(r*c)
    # Space Complexity=O(r+c)



if __name__ == "__main__":
    mat=[[0,0,0],
    [0,0,1]]
    modifyMatrix(mat)