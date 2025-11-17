#include <stdio.h>

long long gcd(long long a, long long  b) {
    while (b != 0) {
        long long temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int main() {
    int t;
    scanf("%d", &t);
    while (t--) {
        int n,result=1;
        scanf("%d",&n);
        long long p[n], s[n], lcm[n];
        
        scanf("%lld",&p[0]);
        for(int i=1; i<n; i++){
            scanf("%lld",&p[i]);
            if(p[i]>p[i-1] || p[i-1]%p[i]!=0) result=0;
        }
        scanf("%lld",&s[0]);
        for(int i=1; i<n; i++){
            scanf("%lld",&s[i]);
            if(s[i]<s[i-1] || s[i]%s[i-1]!=0) result=0;
        }
        
        if(result)
            for (int i = 0; i < n; i++) lcm[i] = p[i] * s[i] / gcd(p[i], s[i]);
        
        if(result){
            long long x = 0;
            for (int i = 0; i < n; i++){
                x = gcd(x, lcm[i]);
                if (x != p[i]) { result = 0; break;}
            }
        }
        
        if(result){
            long long x = 0;
            for (int i = n - 1; i >= 0; i--) {
                x = gcd(x, lcm[i]);
                if (x != s[i]) {result = 0; break;}
            }
        }

        printf("%s\n", result ? "YES" : "NO");
    }
    return 0;
}
