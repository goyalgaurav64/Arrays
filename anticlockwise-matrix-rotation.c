#include<stdio.h>
int main()
{
    int a[10][10],n,i,j;
    printf("Enter Size of matrix:");
    scanf("%d",&n);
    printf("\nEnter Elements in Matrix:\n");
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {
            scanf("%d",&a[i][j]);
        }
    }
    printf("\nOriginal Matrix:\n");
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {
            printf("%d ",a[i][j]);
        }
        printf("\n");
    }
    printf("Counter-Clockwise by 90 deg:\n");
    for(i=n-1;i>=0;i--)
    {
        for(j=0;j<n;j++)
        {
            printf("%d ",a[j][i]);
        }
        printf("\n");
    }
}