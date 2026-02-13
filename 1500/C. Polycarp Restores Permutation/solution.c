#include<stdio.h>
#include<limits.h>

int main(){
    int n,result=1;
    long long total=0;
    scanf("%d",&n);
    int q[n-1], a[n],present[n];
    
    for(int i=0; i<n-1; i++){
        scanf("%d",&q[i]);
        total+= (long long)(n-1-i)*q[i];
        present[i] = 0;
    }
    present[n-1] = 0;
    
    int x = (int)((double)(n+1)/2 - (double)total/n);

    a[0] = x;
    if(a[0]>n || a[0]<1) {result=0; printf("-1"); }
    else{
        present[a[0]-1]++;
        for(int i=0; i<n-1; i++){
            a[i+1]=a[i]+q[i];
            present[a[i+1]-1]++;
            
            if(a[i+1]>n || a[i+1]<1 || present[a[i+1]-1]>1){
                result=0;
                printf("-1");
                break;
            }
        }
    }
        
    if(result){
        for(int i=0; i<n; i++) printf("%d ",a[i]);
    }
    
    return 0;
}
