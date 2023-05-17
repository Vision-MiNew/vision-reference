#include <stdio.h>
#define scanf_s scanf

int main() {

    char num[20] = "";

    printf("Input numbers : ");
    scanf_s("%s", num);
    for (int i=19; i>=0; i--){
        printf("%c",num[i]);
    }

    return 0;
}