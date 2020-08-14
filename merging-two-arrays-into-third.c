#include<stdio.h>
int main()
{
    int a[10]={1,2,3,4},b[10]={6,7,8,9},c[10],i,j=0,k=0,n,h=0;
    printf("First Array:\n");
    for(i=0;i<4;i++)
    {
        printf("%d ",a[i]);
    }
    printf("\nSecond Array:\n");
    for(i=0;i<4;i++)
    {
        printf("%d ",b[i]);
    }
    while(j<8)
    {
        if(j<4)
        c[j]=a[k++];
        else
        c[j]=b[h++];
        j++;
    }
    printf("\nMerged array is:\n");
    for(i=0;i<8;i++)
    {
        printf("%d ",c[i]);
    }

}