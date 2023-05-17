#include <stdio.h>

int main() {
    int i;
    int j;

    for(i=1;i<10;i++){
        for(j=2;j<10;j++){
            printf("%d * %d = %d \t", j, i, i*j);
        }
        printf("\n");
    }

    return 0;
}