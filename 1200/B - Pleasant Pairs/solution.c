#include<stdio.h>

int main(){
    int t,n;
    scanf("%d",&t);
    
    for(int k=0; k<t; k++){
        scanf("%d",&n);
        int a[n];
        for(int i=0; i<n; i++) scanf("%d",&a[i]);
        int count = 0;
        
        for(int i=0; i<n; i++){
            for(int j=(a[i]+i-(2*(i+1))%a[i]), l=(i+j+2)/a[i]; j<n; j+=a[i],l++)
                if(a[j]==l) count++;
        }
        printf("%d\n",count);
    }
    
    
    return 0;
}
