#include <stdio.h>

int min(int a, int b){
    if (a <= b) return a;
    else return b;
}

int main() {
    int t;
    scanf("%d",&t);
    
    while(t--){
        int n;
        scanf("%d",&n);
        int arr[n], dp[n+1];
        
        for(int i=0; i<=n; i++) dp[i] = n+1;
        
        for(int i=0; i<n; i++){
            scanf("%d",&arr[i]);
            dp[arr[i]] = 1;
        }
        
        for(int num=4; num<=n; num++){
            for(int k=2; k*k<=n; k++){
                if (num % k != 0) continue;
                if (dp[num / k] == n+1 || dp[k] == n+1) continue;
                dp[num] = min(dp[num], dp[num/k] + dp[k]);
            }
        }
        
        for(int i=1; i<=n; i++){
            if (dp[i] == n+1) printf("-1 ");
            else printf("%d ",dp[i]);
        }
        printf("\n");
    }
    

    return 0;
}

 
