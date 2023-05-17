#ifndef STUDENT_H
#define STUDENT_H

struct Student {
    int rollNumber;
    char name[100];
    int age;
    float marks;
    struct Student* next;
};

void addStudent(struct Student** head);
void displayStudents(struct Student* head);
void sortStudents(struct Student** head);
struct Student* binarySearch(struct Student* head, const char* name);
void searchStudent(struct Student* head, const char* name);
void deleteStudentByName(struct Student** head, const char* name);

#endif  // STUDENT_H
