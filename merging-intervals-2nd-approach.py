def merge(li,n):
    m=[]
    i=1
    li.sort(key=lambda x:x[0])
    while i<len(li):
        if li[i-1][1] >= li[i][0]:
            li[i-1][0]=min(li[i-1][0],li[i][0])
            li[i-1][1]=max(li[i-1][1],li[i][1])
            li.pop(i)
        else:
            i+=1
    return li





if __name__ == "__main__":
    # a=[[6, 8], [1, 9], [2, 4], [4, 7]]
    a=[[1,3],[2,4],[8,10],[15,18]] 
    n=len(a)
    li=merge(a,n)
    for i in range(len(li)):
        print(li[i],end=" ")









# b=li[i+1]
#         if (a[1] > b[0] and a[1] < b[1]):
#             a[1]=b[1]
#             m.append([a[0],a[1]])
#         elif(a[1]>b[0] and a[1] > b[1]):
#             m.append([a[0],a[1]])
#     m.append(b)
#     return m