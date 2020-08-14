#include<stdio.h>
int main()
{
    int r,c,m,n,a[10][10],t[10][10];
    printf("Enter no. of rows and cols:");
    scanf("%d%d",&m,&n);
    printf("Enter elements in matrix:\n");
    for(r=0;r<m;r++)
    {
        for(c=0;c<n;c++)
        {
            scanf("%d",&a[r][c]);
        }
    }
    printf("Matrix is:\n");
    for(r=0;r<m;r++)
    {
        for(c=0;c<n;c++)
        {
            printf("%d ",a[r][c]);
        }
        printf("\n");
    }
    printf("Transpose is:\n");
    for(r=0;r<m;r++)
    {
        for(c=0;c<n;c++)
        {
            t[c][r]=a[r][c];
        }
    }
    for(r=0;r<m;r++)
    {
        for(c=0;c<n;c++)
        {
            printf("%d ",t[r][c]);
        }
        printf("\n");
    }
}