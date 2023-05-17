#include <stdio.h>
#define scanf_s scanf

int main() {
    int score[4]; // eng mat soci scie
    int i = 0;

    printf("input your scores\n");

    printf("English : ");
    scanf_s("%d", &score[i++]);

    printf("Math : ");
    scanf_s("%d", &score[i++]);

    printf("Social : ");
    scanf_s("%d", &score[i++]);

    printf("Science : ");
    scanf_s("%d", &score[i]);

    for(i=0; i<4; i++) {
        printf("%d\t", score[i]);
    }
    return 0;
}