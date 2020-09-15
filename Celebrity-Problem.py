                                    # TIME COMPLEXITY : O(N)
                                    #SPACE COMPLEXITY : O(N)
from collections import deque
def knows(a):
    s=deque()
    for i in range(len(a)):
        s.append(i)
    while len(s) >= 2:
        i=s.pop()
        j=s.pop()

        if a[i][j] == 1:
            # if i knows j -> i can't be celebrity
            s.append(j)
        else:
            # if i does not know j -> i may be a celebrity
            s.append(i)
        pot=s.pop()
        for i in range(len(a)):
            if i!=pot:
                if a[i][pot]==0 or a[pot][i]==1:
                    return -1
        return pot




if __name__ == "__main__":
    a= [[0, 0, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 0],
        [0, 0, 1, 0]]
    ans=knows(a)
    if ans==-1:
        print("No celebrity")
    else:
        print(ans)