#include <stdio.h>
#define scanf_s scanf

int main() {

    int n = 0;
    printf("input a factoril number : ");
    scanf_s("%d", &n);

    for (int i=n-1 ; i>0; i--) {
        n *= i;
    }

    printf("Factorial Number is : %d", n);

    return 0;
}