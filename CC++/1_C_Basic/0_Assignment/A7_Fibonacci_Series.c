#include <stdio.h>
#define scanf_s scanf

int main() {

    int prev = 0, next =1 , result = 1, n =0;

    printf("Enter number : ");
    scanf_s("%d", &n);

    do {
        printf("%d  ", result);
        result = prev + next;
        prev = next;
        next = result;
    }while(result <= n);

    return 0;

}