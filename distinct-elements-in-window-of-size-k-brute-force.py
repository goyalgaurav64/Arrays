def distinctEle(a,n,k):
    cnt=0
    for i in range(k):
        j=0
        while j<i:
            if a[i]==a[j]:
                break
            else:
                j+=1
        if i==j:
            cnt+=1
    return cnt
        



if __name__ == "__main__":
    a=[1, 2, 1, 3, 4, 2, 3]
    k=4
    for i in range(len(a)-k+1):
        print(distinctEle(a[i:k+i],len(a),k),end=" ")