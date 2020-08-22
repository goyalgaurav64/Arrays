def printDia(m):
    r=len(m)
    c=len(m[0])
    for col in range(c-1):
        j=col
        i=0
        while j >= 0:
            print(m[i][j],end=" ")
            j-=1
            i+=1
        print()
    
    for row in range(r):
        i=row
        j=c-1
        while i<=r-1:
            print(m[i][j],end=" ")
            i+=1
            j-=1
        print()




if __name__ == "__main__":
    m=[[1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20]]
    printDia(m)