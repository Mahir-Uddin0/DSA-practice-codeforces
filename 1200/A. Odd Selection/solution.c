#include <stdio.h>

int main() {
    int t,temp,n,x,odd_count,even_count;
    scanf("%d",&t);
    for(int i=0; i<t; i++){
        scanf("%d %d",&n,&x);
        odd_count=0, even_count=0;
        for(int j=0; j<n; j++){
            scanf("%d",&temp);
            if(temp%2==0) even_count++;
            else odd_count++;
        }
        if (x<=even_count){
            if (odd_count>0) printf("YES\n");
            else printf("NO\n");
        }
        else{
            if ((x-even_count)%2!=0) printf("YES\n");
            else{
                if ((x-even_count)<odd_count && even_count>0) printf("YES\n");
                else printf("NO\n");
            }
        }
    }
    return 0;
}
