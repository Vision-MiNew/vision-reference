#include <stdio.h>
#define scanf_s scanf

int main() {
    int age = 0;

    printf("Input your age : ");
    scanf_s("%d", &age);                   

    if (age >= 16) {                            //    > < >= <= ==   || : OR         && : AND         ! : not
        printf("You can get Driver licence");
    }
    else {
        printf("You are so young.");
    }
    return 0;

    // if (sex == 'male' && age > 35) {   
    // }
    // else if (sex = 'male' && (age > 21 && age <=35)) {
    // }
    // else if (sex = 'female' || (age > 32 && age <= 45)) {
    // }
    // else {
    // }
}