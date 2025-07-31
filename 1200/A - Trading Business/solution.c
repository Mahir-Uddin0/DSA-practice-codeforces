#include<stdio.h>
 
int main(){
    int n,m,k, total_elem, total_profit, max_ind, temp, max_profit=0;
    scanf("%d %d %d",&n, &m, &k);
    int a[n][m], b[n][m], c[n][m], profit_mat[n][n], profit[m];
    char planet[n][30];
    
    for(int i=0; i<n; i++){
        scanf("%s",&planet[i]);
        for(int j=0; j<m; j++) scanf("%d %d %d",&a[i][j], &b[i][j], &c[i][j]);
    }  
    printf("\n\n");
    for(int i=0; i<n; i++){
        profit_mat[i][i] = 0;
        for(int l=0; l<n; l++){
            if(i==l) continue;
            for(int j=0; j<m; j++) profit[j] = b[l][j] - a[i][j];
            total_elem = 0;
            total_profit = 0;
            for(int j=0; j<m; j++){
                max_ind = j;
                for(int a=0; a<m;a++) if(profit[a]>profit[max_ind]) max_ind=a;
                
                if(profit[max_ind] <=0) break;
                if(c[i][max_ind]>=k-total_elem){
                    total_profit+=(k-total_elem)*profit[max_ind];
                    break;
                }
                else{
                    total_profit+=c[i][max_ind]*profit[max_ind];
                    total_elem+=c[i][max_ind];
                    profit[max_ind] = 0;
                }
            }
            profit_mat[i][l] = total_profit;
        }
    }
    
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            if(max_profit<profit_mat[i][j]) max_profit = profit_mat[i][j];
        }
    }
    printf("%d",max_profit);
    return 0;
}
