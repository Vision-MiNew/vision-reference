#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_SIZE 100

struct entry {
    char key[50];
    int value;
};

struct dictionary {
    struct entry data[MAX_SIZE];
    int count;
};

void init_dictionary(struct dictionary *d) {
    d->count = 0;
}

int is_empty(struct dictionary *d) {
    return d->count == 0;
}

int is_full(struct dictionary *d) {
    return d->count == MAX_SIZE;
}

void insert(struct dictionary *d, const char *key, int value) {
    if (is_full(d)) {
        printf("Error: Dictionary is full\n");
        return;
    }
    strcpy(d->data[d->count].key, key);
    d->data[d->count].value = value;
    d->count++;
}

int search(struct dictionary *d, const char *key) {
    for (int i = 0; i < d->count; i++) {
        if (strcmp(d->data[i].key, key) == 0) {
            return d->data[i].value;
        }
    }
    return -1; // Key not found
}

int main() {
    struct dictionary d;
    init_dictionary(&d);

    insert(&d, "apple", 42);
    insert(&d, "banana", 66);
    insert(&d, "orange", 93);

    printf("Value associated with key 'apple': %d\n", search(&d, "apple"));
    printf("Value associated with key 'banana': %d\n", search(&d, "banana"));
    printf("Value associated with key 'orange': %d\n", search(&d, "orange"));
    printf("Value associated with key 'grape': %d\n", search(&d, "grape"));

    return 0;
}
