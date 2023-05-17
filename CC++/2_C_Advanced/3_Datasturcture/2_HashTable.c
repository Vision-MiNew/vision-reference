#include <stdio.h>
#include <stdlib.h>

#define SIZE 10

// Step 1: Define the structure of a hash table and a node in C.

// Node structure for the hash table
struct Node {
    int key;
    int value;
    struct Node* next;
};

// Hash table structure
struct HashTable {
    struct Node* array[SIZE];
};

// Step 2: Create a hash function to map keys to an index in the hash table. Here's an example of a simple hash function that calculates the modulo of the key with the size of the hash table
int hashFunction(int key) {
    return key % SIZE;
}

// Step 3: Implement functions to insert and retrieve data from the hash table.
// Function to insert a key-value pair into the hash table
void insert(struct HashTable* hashtable, int key, int value) {
    int index = hashFunction(key);
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->key = key;
    newNode->value = value;
    newNode->next = NULL;

    // If the bucket is empty, insert the node as the head
    if (hashtable->array[index] == NULL) {
        hashtable->array[index] = newNode;
    }
    // If the bucket is not empty, append the node at the end
    else {
        struct Node* curr = hashtable->array[index];
        while (curr->next != NULL) {
            curr = curr->next;
        }
        curr->next = newNode;
    }
}

// Function to retrieve the value associated with a key from the hash table
int get(struct HashTable* hashtable, int key) {
    int index = hashFunction(key);
    struct Node* curr = hashtable->array[index];
    while (curr != NULL) {
        if (curr->key == key) {
            return curr->value;
        }
        curr = curr->next;
    }
    return -1;  // Key not found
}

// Step 4: Implement a main function to test the hash table.
int main() {
    struct HashTable hashtable;
    for (int i = 0; i < SIZE; i++) {
        hashtable.array[i] = NULL;  // Initialize all buckets to NULL
    }

    // Insert key-value pairs into the hash table
    insert(&hashtable, 10, 42);
    insert(&hashtable, 20, 66);
    insert(&hashtable, 30, 93);

    // Retrieve values from the hash table using keys
    int value1 = get(&hashtable, 10);
    int value2 = get(&hashtable, 20);
    int value3 = get(&hashtable, 30);

    printf("Value associated with key 10: %d\n", value1);
    printf("Value associated with key 20: %d\n", value2);
    printf("Value associated with key 30: %d\n", value3);

    return 0;
}
