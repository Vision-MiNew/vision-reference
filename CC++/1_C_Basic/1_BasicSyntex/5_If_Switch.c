#include <stdio.h>
#define scanf_s scanf


int main() {
    int run = 0;    // 0 : false   /   else : true

    // If statement
    if (run) {
        printf("True");
    }

    if(run) {
        printf("one more true");
    }
    else if(run) {
        printf("false");
    }
    else {
        printf("error");
    }

    // Switch statement
    printf("\n--------------");
    printf("\n- [1] Cola ---");
    printf("\n- [2] Milkis -");
    printf("\n- [3] Cider --");
    printf("\n- [4] Coffee -");
    printf("\n--------------\n");

    int select = 0;
    scanf_s("%d", &select);
    
    switch (select) {
        case 1:
            printf("\nHere a can of Cola");
            break;
        case 2:
            printf("\nHere a can of Milkis");
            break; 
        case 3:
            printf("\nHere a can of Cider");
            break;
        case 4:
            printf("\nHere a can of Coffee");
            break;   
        default:
            printf("\nInput error");
            break;
    }

    // if statement : range        ex) age
    // switch statement : point    ex) button

    return 0;
}