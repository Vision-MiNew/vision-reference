#include <stdio.h>
#define scanf_s scanf

int main() {
    int score = 0;

    for(int i=0;i<3;i++) {
        printf("\n\nInput your score : ");
        scanf_s("%d", &score);

        if ( score <= 100 && score > 86) {
            printf("Your grade : A\n");
        }
        else if( score <= 86 && score > 73){
            printf("Your grade : B\n");
        }
        else if( score <=73 && score > 60) {
            printf("Your grade : C\n");
        }
        else if( score <=60 && score >=0){
            printf("Your grade : F\n");
        }
        else {
            printf("wrong input, check your value \n");
            i--;
        }
    }
    return 0;
}