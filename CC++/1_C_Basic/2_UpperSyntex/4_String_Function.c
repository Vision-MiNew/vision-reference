#include <stdio.h>
#define scanf_s scanf

int main() {
    
    char name[] = "minsoo";
    char temp[];
    
    strlen(name); // length of string
    strcat(name, temp); // union strings
    strcpy(name, temp); // copy
    strcmp(name, temp); // compare
    toupper(name); // convert to uppercase
    tolower(name); // convert to lowercase
    atoi(name)   ; // convert to number integer // atod() double
    printf(" %s \n ", strlen(name) );// length of string
    printf(" %s \n ", strcat(name) );// union strings
    printf(" %s \n ", strcpy(name) );// copy
    printf(" %s \n ", strcmp(name) );// compare
    printf(" %s \n ", toupper(name)); // convert to uppercase
    printf(" %s \n ", tolower(name)); // convert to lowercase
    printf(" %d \n ", atoi(name)   ); // convert to number integer // atod() double

    return 0;
}