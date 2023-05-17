#include <stdio.h>

void merge(int arr[], int left[], int leftSize, int right[], int rightSize) {
    int i = 0; // Index for the left subarray
    int j = 0; // Index for the right subarray
    int k = 0; // Index for the merged array

    while (i < leftSize && j < rightSize) {
        if (left[i] <= right[j]) {
            arr[k] = left[i];
            i++;
        } else {
            arr[k] = right[j];
            j++;
        }
        k++;
    }

    // Copy the remaining elements of the left subarray
    while (i < leftSize) {
        arr[k] = left[i];
        i++;
        k++;
    }

    // Copy the remaining elements of the right subarray
    while (j < rightSize) {
        arr[k] = right[j];
        j++;
        k++;
    }
}

void mergeSort(int arr[], int n) {
    if (n <= 1) {
        return;
    }

    int mid = n / 2;
    int left[mid];
    int right[n - mid];

    // Divide the array into two halves
    for (int i = 0; i < mid; i++) {
        left[i] = arr[i];
    }
    for (int i = mid; i < n; i++) {
        right[i - mid] = arr[i];
    }

    // Recursively sort the two halves
    mergeSort(left, mid);
    mergeSort(right, n - mid);

    // Merge the sorted halves
    merge(arr, left, mid, right, n - mid);
}

int main() {
    int arr[] = {5, 2, 8, 12, 3};
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("Array before sorting:\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    mergeSort(arr, n);

    printf("Array after sorting in ascending order:\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}
