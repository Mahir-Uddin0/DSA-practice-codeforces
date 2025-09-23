#include<stdio.h>

int main(){
    int x1, y1, x2, y2, x3, y3, x4, y4;
    scanf("%d %d %d %d",&x1,&y1,&x2,&y2);
    
    if(x1!=x2 && y1!=y2){
        if((x1-x2)*(x1-x2) != (y1-y2)*(y1-y2)){
            printf("-1");
            return 0;
        }
        else{
            printf("%d %d %d %d",x1,y2,x2,y1);
        }
    }
    else if(y1==y2){
        int length = x1-x2;
        printf("%d %d %d %d",x1,y1+length,x2,y2+length);
    }
    else if(x1==x2){
        int length = y1-y2;
        printf("%d %d %d %d",x1+length,y1,x2+length,y2);
    }
    
    
    return 0;
}
