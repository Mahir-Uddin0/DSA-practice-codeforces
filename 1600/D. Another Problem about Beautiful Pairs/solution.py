#include <stdio.h>

int main() {
    int t;
    scanf("%d", &t);

    while (t--) {
        int n;
        scanf("%d", &n);

        long long count = 0, similar_count = 0;
        long long a[n + 1];
        a[0] = 0;
        scanf("%lld", &a[1]);
        for (int i = 2; i <= n; i++) {
            scanf("%lld", &a[i]);
        }


        for (int i = 1; i <= n; i++) {
            
            long long k = 1;
            while (k <= a[i]) {
                long long jp = i + a[i] * k;
                long long jn = i - a[i] * k;

                if (jp > n && jn < 1) break;

                if (jp <= n && a[jp] == k){
                    if (a[i] == k) similar_count++;   
                    count++;
                }
                if (jn > 0 && a[jn] == k){
                    if (a[i] == k) similar_count++;   
                    count++;
                }

                k++;
            }
        }

        printf("%lld\n", count - similar_count/2);
    }

    return 0;
}
