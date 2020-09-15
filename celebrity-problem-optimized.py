                                # TIME COMPLEXITY : O(N)
                                # SPACE COMPLEXITY: O(1) 

def celebrity(a):
    m=0
    n=len(a)-1
    while m < n:
        if knows(a,m,n):
            m+=1
        else:
            n-=1
    for i in range(len(a)-1):
        if i!=m and (knows(a,m,i) or (not knows(a,i,m))):
            return -1
    return m

def knows(a,m,n):
    if a[m][n]==1:
        return True
    return False




if __name__ == "__main__":
    a= [[0, 0, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 0],
        [0, 0, 1, 0]]
    ans=celebrity(a)
    if ans==-1:
        print("No celebrity")
    else:
        print(ans)