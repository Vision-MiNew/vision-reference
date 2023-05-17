#include <stdio.h>
#define scanf_s scanf

int main() {
    for(int i=1;i<10;i++){
        for(int j=2; j<10; j++){
            printf("%d * %d = %d\t", j, i, i*j);
        }
        printf("\n");
    }
    return 0;
}