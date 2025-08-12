
#include <stdio.h>

int main() {
    int n,m;
    scanf("%d %d",&n,&m);
    getchar();
    char board[n][m];
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            scanf("%c",&board[i][j]);
        }
        getchar();
    }
    
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            if(board[i][j]=='.'){
                if((i+j)%2==0) board[i][j] = 'B';
                else board[i][j] = 'W';
            }
        }
    }
    
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            printf("%c",board[i][j]);
        }
        printf("\n");
    }
    
    return 0;
}
