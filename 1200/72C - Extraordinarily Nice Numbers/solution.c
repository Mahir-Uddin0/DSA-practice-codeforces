#include <stdio.h>

int main() {
    int x;
    scanf("%d", &x);

    int odd = 0, even = 0;

    for (int i = 1; i <= x / 2; i++) {
        if (x % i == 0) {
            if (i % 2 == 0)
                even++;
            else
                odd++;
        }
    }

    if (x % 2 == 0)
        even++;
    else
        odd++;

    if (odd == even)
        printf("YES\n");
    else
        printf("NO\n");

    return 0;
}

