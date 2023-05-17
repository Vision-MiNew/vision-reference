#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "student.h"


void deleteStudentByName(struct Student** head, const char* name) {
    if (*head == NULL) {
        printf("No students to delete.\n");
        return;
    }

    struct Student* current = *head;
    struct Student* previous = NULL;

    // Check if the first node is the one to be deleted
    if (strcmp(current->name, name) == 0) {
        *head = current->next;
        free(current);
        printf("Student with Name '%s' deleted successfully.\n", name);
        return;
    }

    while (current != NULL && strcmp(current->name, name) != 0) {
        previous = current;
        current = current->next;
    }

    if (current == NULL) {
        printf("Student with Name '%s' not found.\n", name);
        return;
    }

    previous->next = current->next;
    free(current);
    printf("Student with Name '%s' deleted successfully.\n", name);
}

void addStudent(struct Student** head) {
    struct Student* newStudent = (struct Student*)malloc(sizeof(struct Student));

    if (newStudent == NULL) {
        printf("Memory allocation failed.\n");
        return;
    }

    printf("Enter Roll Number: ");
    scanf("%d", &(newStudent->rollNumber));
    printf("Enter Name: ");
    scanf(" %[^\n]s", newStudent->name);
    printf("Enter Age: ");
    scanf("%d", &(newStudent->age));
    printf("Enter Marks: ");
    scanf("%f", &(newStudent->marks));

    newStudent->next = NULL;

    if (*head == NULL) {
        *head = newStudent;
    } else {
        struct Student* current = *head;
        while (current->next != NULL) {
            current = current->next;
        }
        current->next = newStudent;
    }

    printf("Student added successfully.\n");
}

void displayStudents(struct Student* head) {
    if (head == NULL) {
        printf("No students found.\n");
        return;
    }

    printf("Student Details:\n");
    struct Student* current = head;
    while (current != NULL) {
        printf("Roll Number: %d\n", current->rollNumber);
        printf("Name: %s\n", current->name);
        printf("Age: %d\n", current->age);
        printf("Marks: %.2f\n\n", current->marks);
        current = current->next;
    }
}

int compareRollNumber(const void* a, const void* b) {
    struct Student* studentA = *(struct Student**)a;
    struct Student* studentB = *(struct Student**)b;
    return studentA->rollNumber - studentB->rollNumber;
}

void sortStudents(struct Student** head) {
    if (*head == NULL) {
        printf("No students found.\n");
        return;
    }

    int count = 0;
    struct Student* current = *head;
    while (current != NULL) {
        count++;
        current = current->next;
    }

    struct Student** studentsArray = (struct Student**)malloc(count * sizeof(struct Student*));
    if (studentsArray == NULL) {
        printf("Memory allocation failed.\n");
        return;
    }

    int i = 0;
    current = *head;
    while (current != NULL) {
        studentsArray[i] = current;
        current = current->next;
        i++;
    }

    qsort(studentsArray, count, sizeof(struct Student*), compareRollNumber);

    *head = studentsArray[0];
    current = *head;
    for (i = 1; i < count; i++) {
        current->next = studentsArray[i];
        current = current->next;
    }
    current->next = NULL;

    free(studentsArray);

    printf("Students sorted successfully.\n");
}

int compareName(const void* a, const void* b) {
    struct Student* studentA = *(struct Student**)a;
    struct Student* studentB = *(struct Student**)b;
    return strcmp(studentA->name, studentB->name);
}

struct Student* binarySearch(struct Student* head, const char* name) {
    if (head == NULL) {
        return NULL;
    }

    struct Student* low = head;
    struct Student* high = NULL;

    while (low != high) {
        struct Student* mid = low;
        int count = 0;
        while (mid != high) {
            mid = mid->next;
            count++;
        }
        int midIndex = count / 2;

        while (midIndex > 0) {
            low = low->next;
            midIndex--;
        }

        int compareResult = strcmp(low->name, name);
        if (compareResult < 0) {
            low = low->next;
        } else if (compareResult == 0) {
            return low;
        } else {
            high = low;
            low = head;
        }
    }

    return NULL;
}

void searchStudent(struct Student* head, const char* name) {
    struct Student* result = binarySearch(head, name);
    if (result != NULL) {
        printf("Student Found:\n");
        printf("Roll Number: %d\n", result->rollNumber);
        printf("Name: %s\n", result->name);
        printf("Age: %d\n", result->age);
        printf("Marks: %.2f\n", result->marks);
    } else {
        printf("Student with Name '%s' not found.\n", name);
    }
}


