#include <stdio.h>
#include <stdlib.h>


// Step 1: Define the structure of a hash table and a node in C.

#define ALPHABET_SIZE 26

struct TrieNode {
    struct TrieNode* children[ALPHABET_SIZE];
    int isEndOfWord;
};


// Step 2: Create a new trie node and initialize its members.

struct TrieNode* createNode() {
    struct TrieNode* newNode = (struct TrieNode*)malloc(sizeof(struct TrieNode));
    newNode->isEndOfWord = 0;

    for (int i = 0; i < ALPHABET_SIZE; i++) {
        newNode->children[i] = NULL;
    }

    return newNode;
}

// Step 3: Implement functions to insert and search words in the trie.

void insert(struct TrieNode* root, const char* word) {
    struct TrieNode* curr = root;

    for (int i = 0; word[i] != '\0'; i++) {
        int index = word[i] - 'a';

        if (curr->children[index] == NULL) {
            curr->children[index] = createNode();
        }

        curr = curr->children[index];
    }

    curr->isEndOfWord = 1;
}

int search(struct TrieNode* root, const char* word) {
    struct TrieNode* curr = root;

    for (int i = 0; word[i] != '\0'; i++) {
        int index = word[i] - 'a';

        if (curr->children[index] == NULL) {
            return 0;  // Word not found
        }

        curr = curr->children[index];
    }

    return (curr != NULL && curr->isEndOfWord);
}

// Step 4: Implement a main function to test the trie.

int main() {
    struct TrieNode* root = createNode();

    // Insert words into the trie
    insert(root, "apple");
    insert(root, "banana");
    insert(root, "orange");

    // Search for words in the trie
    printf("Search result for 'apple': %s\n", search(root, "apple") ? "Found" : "Not Found");
    printf("Search result for 'banana': %s\n", search(root, "banana") ? "Found" : "Not Found");
    printf("Search result for 'orange': %s\n", search(root, "orange") ? "Found" : "Not Found");
    printf("Search result for 'grape': %s\n", search(root, "grape") ? "Found" : "Not Found");

    return 0;
}

