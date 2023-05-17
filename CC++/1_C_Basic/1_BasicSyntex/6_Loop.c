#include <stdio.h>
#define scanf_s scanf

// while(conditional) { }   during conditional == true
// for(i=0; i<n; i++) { }   Looping nth

int main() {

    // printf("\n--------------");
    // printf("\n- [1] Cola ---");
    // printf("\n- [2] Milkis -");
    // printf("\n- [3] Cider --");
    // printf("\n- [4] Coffee -");
    // printf("\n- [5] exit ---");
    // printf("\n--------------\n\n");

    // int select = 0;        // input right side to left side
    
    // while(select != 5) {   // != : not equal to
        
    //     scanf_s("%d", &select);
    //     switch (select) {
    //         case 1:
    //             printf("\nHere a can of Cola\n");
    //             break;
    //         case 2:
    //             printf("\nHere a can of Milkis\n");
    //             break; 
    //         case 3:
    //             printf("\nHere a can of Cider\n");
    //             break;
    //         case 4:
    //             printf("\nHere a can of Coffee\n");
    //             break;   
    //         case 5:
    //             printf("\nexit\n");
    //             break;  
    //         default:
    //             printf("\nInput error\n");
    //             break;
    //     }
    // }

    int i = 5;
    // for( initializing ; conditional ; how to change )
    // + - / * % ^ +=  -=  /=
    // i += 6 ;    // i : 11
    // i++;
    // i = i + 1;
    // i += 1;
    // i++;
    // i--;

    for(i=0 ; i<5; i++) {
        // printf("hello");
        printf("%d\n", i); // 01234
    }
    i = 0;

    while (i < 5) {
        printf("\n%d\n\n", i); 
        i++;
    }


    // while    ex) gameover   Hp <= 0          Until when?
    // for      ex) 9 x 9      matrix[i][j]     How many times?
    


    return 0;
}