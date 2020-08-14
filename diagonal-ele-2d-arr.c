#include<stdio.h>
int main()
{
    int i,j,m,n,a[20][30];
    printf("Enter No. of ros and cols:");
    scanf("%d%d",&m,&n);
    printf("Enter elements in matrix:\n");
    for(i=0;i<m;i++)
    {
        for(j=0;j<n;j++)
        {
            scanf("%d",&a[i][j]);
        }
    }
    printf("Matrix Is:\n");
    for(i=0;i<m;i++)
    {
        for(j=0;j<n;j++)
        {
            printf("%d ",a[i][j]);
        }
        printf("\n");
    }
    printf("Left Diagonal elements are:\n");
    for(i=0;i<m;i++)
    {
        for(j=0;j<n;j++)
        {
            if(i==j)
            printf("%d ",a[i][j]);
        }
    }
    printf("\nRight Diagonal elements are:\n");
    for(i=0;i<m;i++)
    {
        for(j=0;j<n;j++)
        {
            if(i+j==m-1)
            printf("%d ",a[i][j]);
        }
    }
}