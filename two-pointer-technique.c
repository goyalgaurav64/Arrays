#include<stdio.h>
int main()
{
    int a[]={10,20,35,50,75,80},t;
    int flag=0;
    int n=sizeof(a)/sizeof(a[0]);
    printf("Enter Target Sum:");
    scanf("%d",&t);
    int i=0,j=n-1;
    while(i<j)
    {
        if(a[i]+a[j]<t)
            i++;
        else if(a[i]+a[j]==t)
        {
            flag=1;
            break;
        }
        else
            j--;
        
    }
    if(flag==1)
    printf("%d + %d=%d",a[i],a[j],t);
    else
    {
        printf("No such Pair Exists");
    }
}