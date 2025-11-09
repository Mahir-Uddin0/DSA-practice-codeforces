#include <stdio.h>

int main(){
    int t;
    scanf("%d ",&t);
    
    while(t--){
        int n,same=1;
        scanf("%d",&n);
        int a[n],b[n];
        
        for(int i=0; i<n; i++) scanf("%d",&a[i]);
        for(int i=0; i<n; i++) scanf("%d",&b[i]);
        
        if(a[n-1]!=b[n-1]){ printf("NO\n"); continue;}
        
        for(int i=0; i<n-1; i++){
            if(a[i]==b[i]) continue;
            else if((a[i]^a[i+1])==b[i]) continue;
            else if((a[i]^b[i+1])==b[i]) continue;
            else{
                printf("NO\n");
                same = 0;
                break;
            }
        }
        
        if(same) printf("YES\n");
        
    }
    
    return 0;
}
