def printDiag(m):
    r=len(m)
    c=len(m[0])
    print("Diagonal Matrix is:")
    for k in range(r):
        i=k
        j=0
        while i>=0:
            print(m[i][j],end=' ')
            i-=1
            j+=1
        print()
    for k in range(1,c):
        i=r-1
        j=k
        while j<=c-1:
            print(m[i][j],end=' ')
            i-=1
            j+=1
        print()






if __name__ == "__main__":
    m=[['a','b','c','d','e'],
    ['f','g','h','i','j'],
    ['k','l','m','n','o'],
    ['p','q','r','s','t']]
    printDiag(m)
