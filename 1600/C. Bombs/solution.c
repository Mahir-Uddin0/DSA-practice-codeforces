#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct {
    long long x, y;
} Bomb;

typedef struct {
    double dist;
    int index;
} DistIndex;

int compare(const void* a, const void* b) {
    DistIndex* da = (DistIndex*)a;
    DistIndex* db = (DistIndex*)b;
    if (da->dist < db->dist) return -1;
    if (da->dist > db->dist) return 1;
    return 0;
}

int main() {
    int n;
    scanf("%d", &n);
    
    Bomb* bombs = (Bomb*)malloc(n * sizeof(Bomb));
    DistIndex* dist = (DistIndex*)malloc(n * sizeof(DistIndex));

    for (int i = 0; i < n; ++i) {
        scanf("%lld %lld", &bombs[i].x, &bombs[i].y);
        dist[i].dist = (double)(bombs[i].x * bombs[i].x + bombs[i].y * bombs[i].y);
        dist[i].index = i;
    }

    qsort(dist, n, sizeof(DistIndex), compare);

    int total_steps = 0;
    for (int i = 0; i < n; ++i) {
        int idx = dist[i].index;
        Bomb b = bombs[idx];
        if (b.y != 0) total_steps += 2; 
        if (b.x != 0) total_steps += 2;
        total_steps += 2; 
    }

    printf("%d\n", total_steps);

    for (int i = 0; i < n; ++i) {
        int idx = dist[i].index;
        Bomb b = bombs[idx];

        if (b.y != 0) {
            if (b.y > 0) printf("1 %lld U\n", b.y);
            else printf("1 %lld D\n", -b.y);
        }

        if (b.x != 0) {
            if (b.x > 0) printf("1 %lld R\n", b.x);
            else printf("1 %lld L\n", -b.x);
        }

        printf("2\n");

        if (b.y != 0) {
            if (b.y > 0) printf("1 %lld D\n", b.y);
            else printf("1 %lld U\n", -b.y);
        }
        if (b.x != 0) {
            if (b.x > 0) printf("1 %lld L\n", b.x);
            else printf("1 %lld R\n", -b.x);
        }

        printf("3\n");
    }

    return 0;
}

