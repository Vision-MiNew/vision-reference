#include <stdio.h>
#define scanf_s scanf

int main() {

    int mat[2][2];

    printf("Input 4 numbers : ");
    for (int i=0; i<2; i++) {
        for (int j=0; j<2; j++){
            scanf_s("%d", &mat[i][j]); // num[0][0] 00 01 10 11 num[1][1]
        }
    }
    for (int i=0; i<2; i++) {
        for (int j=0; j<2; j++){
            printf("%d\t", mat[i][j]); // num[0][0] 00 01 10 11 num[1][1]
        }
        printf("\n");
    }


    return 0;
}