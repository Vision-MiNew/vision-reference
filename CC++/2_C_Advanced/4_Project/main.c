#include <stdio.h>
#include "student.h"

int main() {
    struct Student* head = NULL;

    int choice;
    do {
        printf("\nStudent Management System\n");
        printf("1. Add Student\n");
        printf("2. Display Students\n");
        printf("3. Sort Students\n");
        printf("4. Search Student by Name\n");
        printf("5. Delete Student by Name\n");
        printf("6. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                addStudent(&head);
                break;
            case 2:
                displayStudents(head);
                break;
            case 3:
                sortStudents(&head);
                break;
            case 4:
                printf("Enter Name to search: ");
                char name[100];
                scanf(" %[^\n]s", name);
                searchStudent(head, name);
                break;
            case 5:
                printf("Enter Name to delete student: ");
                char delname[100];
                scanf(" %[^\n]s", delname);
                deleteStudentByName(&head, delname);
                break;
            case 6:
                printf("Exiting the program.\n");
                break;
            default:
                printf("Invalid choice. Please try again.\n");
                break;
        }
    } while (choice != 6);

    return 0;
}
