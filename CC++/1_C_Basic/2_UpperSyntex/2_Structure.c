#include <stdio.h>
#define scanf_s scanf

struct students {
    int stdid;
    char name[20];
    int score_eng;
    int score_math;
};

struct teacher {
    int tcid;
    char name[20];
    int score_eng;
    int score_math;
};


int main() {

    struct students son;
    struct students kang;
    struct teacher kim;

    son.stdid = 1;
    printf("\nInput son's fullname : ");
    scanf_s("%s", son.name);
    printf("\nInput son's eng, math score : ");
    scanf_s("%d %d", &son.score_eng, &son.score_math);


    kang.stdid = 2;
    printf("\nInput kang's fullname : ");
    scanf_s("%s", kang.name);
    printf("\nInput kang's eng, math score : ");
    scanf_s("%d %d", &kang.score_eng, &kang.score_math);

    kim.tcid = 31;
    printf("\nInput kim's fullname : ");
    scanf_s("%s", kim.name);
    printf("\nInput kim's eng, math score : ");
    scanf_s("%d %d", &kim.score_eng, &kim.score_math);

    printf("\nson's info - id : %d \t fullname : %s \t eng score : %d \t Math score : %d ", son.stdid, son.name, son.score_eng, son.score_math);
    printf("\nkang's info - id : %d \t fullname : %s \t eng score : %d \t Math score : %d ", kang.stdid, kang.name, kang.score_eng, kang.score_math);
    printf("\nkim's info - id : %d \t fullname : %s \t eng score : %d \t Math score : %d ", kim.tcid, kim.name, kim.score_eng, kim.score_math);

    return 0;
}