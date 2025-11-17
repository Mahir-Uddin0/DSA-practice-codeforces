#include <stdio.h>
#include <stdlib.h>

void merge(int arr[][3], int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;
    
    int L[n1][3];
    int R[n2][3];

    for (int i = 0; i < n1; i++){
        L[i][0] = arr[left + i][0];
        L[i][1] = arr[left + i][1];
        L[i][2] = arr[left + i][2];
    }
    for (int i = 0; i < n2; i++){
        R[i][0] = arr[mid + 1 + i][0];
        R[i][1] = arr[mid + 1 + i][1];
        R[i][2] = arr[mid + 1 + i][2];
    }

    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2) {
        if (L[i][2] <= R[j][2]) {
            arr[k][0] = L[i][0];
            arr[k][1] = L[i][1];
            arr[k][2] = L[i][2];
            i++;
        } else {
            arr[k][0] = R[j][0];
            arr[k][1] = R[j][1];
            arr[k][2] = R[j][2];
            j++;
        }
        k++;
    }

    while (i < n1) {
        arr[k][0] = L[i][0];
        arr[k][1] = L[i][1];
        arr[k][2] = L[i][2];
        i++;
        k++;
    }

    while (j < n2) {
        arr[k][0] = R[j][0];
        arr[k][1] = R[j][1];
        arr[k][2] = R[j][2];
        j++;
        k++;
    }

    free(L);
    free(R);
}

void mergeSort(int arr[][3], int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;

        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }
}

int main(){
    int t;
    scanf("%d", &t);

    while(t--){
        int n,k;
        scanf("%d %d",&n,&k);
        int mat[n][3];
        
        for(int i=0; i<n; i++) scanf("%d %d %d",&mat[i][0],&mat[i][1],&mat[i][2]);
                 
        mergeSort(mat,0,n-1);
        
        int coin = k;
        for(int i=0; i<n; i++){
            if(coin>=mat[i][0] && coin<=mat[i][1] && coin<mat[i][2]){
                coin = mat[i][2];
            }
        }
        
        printf("%d\n",coin);

    }

    return 0;
}
