#include<stdio.h>

int main(){
    int n,max=0;
    long long sum=0;
    scanf("%d",&n);
    int a[n];
    
    for(int i=0; i<n; i++){
        scanf("%d",&a[i]);
        sum+= a[i];
        if(a[i]>max) max = a[i];
    }
    
    int result = sum/(n-1);
    if(sum%(n-1)!=0) result++;
    
    if(max>result) printf("%d",max);
    else printf("%d",result);
    
    return 0;
}
