#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

struct people
{
    char *name;         // char name[];
    char *number;
};


int main() {
    struct people person[4];

    person[0].name = "KIM";
    person[0].number = "778-320-0000";

    person[1].name = "BRION";
    person[1].number = "664-320-0000";
    
    person[2].name = "DAVID";
    person[2].number = "778-540-0000";
    
    person[3].name = "EMMA";
    person[3].number = "771-110-0000";

    for (int i = 0; i < 4; i++) {
        if(strcmp(person[i].name, "EMMA") == 0) {          
            printf("Found : %s\n", person[i].number);
            return 0;
        }
    }
    printf("Not Found \n");
    return 1;
}