#include<stdio.h>
#include<stdlib.h>
struct stack
{
    int stack[100];
    int top;
};
int n;
int pop(struct stack *s);
void push(struct stack *s,int ele);
void findnextGreater(int a[],int n);
void fillarr();
int isEmpty(struct stack *s);
void createStack(int top);
int main()
{
    fillarr();
}
void fillarr()
{
    int i,a[10];
    printf("Enter size:");
    scanf("%d",&n);
    printf("Enter elements:");
    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
    printf("\nArray is:");
    for(i=0;i<n;i++)
    {
        printf("%d ",a[i]);
    }
    findnextGreater(a,n);
}
void findnextGreater(int a[],int n)
{
    struct stack s;
    s.top=-1;
    int i=0;
    push(&s,a[0]);
    for(i=1;i<n;i++)
    {
        if(!isEmpty(&s))
        {
            int ele=pop(&s);
            while(a[i]>ele)
            {
                printf("\n%d--->%d",ele,a[i]);
                    if(isEmpty(&s)==1)
                    break;
                ele=pop(&s);
            }
            if (ele > a[i]) 
                push(&s, ele); 
        }
        push(&s,a[i]);
    }
    while(isEmpty(&s)==0)
    {
        int ele=pop(&s);
        printf("\n%d--->-1",ele);
    }
}
void push(struct stack *s,int ele)
{
    if(s->top==n-1)
    {
        printf("Stack is Full");
        exit(0);
    }
    else
    {
        s->top+=1;
        int top=s->top;
        s->stack[top]=ele;
    }
    
}

int pop(struct stack *s)
{
    if(s->top==-1)
        printf("Stack is Empty");
    else
    {
        int top=s->top;
        int val=s->stack[top];
        s->top-=1;
        return val;
    }
    
}
int isEmpty(struct stack *s)
{
    if(s->top==-1)
        return 1;
    else
    {
        return 0;
    }
    
}