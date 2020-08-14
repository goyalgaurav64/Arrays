#include<stdio.h>
int main()
{
    int a,b,i,j;
    printf("Enter First no.:");
    scanf("%d",&a);
    printf("Enter Second no.:");
    scanf("%d",&b);
    for(i=a+1;i<b;i++)
    {
        for(j=2;j<i;j++)
        {
            if(i%j==0)
                break;
        }
    if(i==j)
    {
        printf("%d ",i);
    }
    }
}