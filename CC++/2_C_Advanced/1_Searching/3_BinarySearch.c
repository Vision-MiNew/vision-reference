#include <stdio.h>

int binarySearch(int arr[], int key, int start, int end) {
    if (start > end) {
        return -1;  // Key not found
    }

    int mid = (start + end) / 2;

    if (arr[mid] == key) {
        return mid;  // Key found at mid index
    } else if (arr[mid] > key) {
        return binarySearch(arr, key, start, mid - 1);  // Search in the left half
    } else {
        return binarySearch(arr, key, mid + 1, end);  // Search in the right half
    }
}

int main() {
    int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    int n = sizeof(arr) / sizeof(arr[0]);

    int key = 6;
    int index = binarySearch(arr, key, 0, n - 1);

    if (index != -1) {
        printf("Key found at index %d\n", index);
    } else {
        printf("Key not found\n");
    }
    

    return 0;
}
