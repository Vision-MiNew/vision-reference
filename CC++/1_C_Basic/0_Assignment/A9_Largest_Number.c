#include <stdio.h>
#define scanf_s scanf

int main() {

    int num[5];
    int result = 0;

    printf("Input 5 diffrent numbers : ");
    for (int i=0; i<5; i++) {
        scanf_s("%d", &num[i]);
    }

    result = num[0];

    for (int i=0; i<5; i++) {
        if (result < num[i]){
            result = num[i];
        }
    }

    printf("The Lagest number is : %d", result);
    return 0;
}