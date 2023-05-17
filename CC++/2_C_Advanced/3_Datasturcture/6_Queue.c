#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 100

struct queue {
    int data[MAX_SIZE];
    int front, rear;
};

void init_queue(struct queue *q) {
    q->front = q->rear = -1;
}

int is_empty(struct queue *q) {
    return q->front == -1;
}

int is_full(struct queue *q) {
    return (q->rear + 1) % MAX_SIZE == q->front;
}

void enqueue(struct queue *q, int x) {
    if (is_full(q)) {
        printf("Error: Queue is full\n");
        return;
    }
    if (is_empty(q)) {
        q->front = q->rear = 0;
    } else {
        q->rear = (q->rear + 1) % MAX_SIZE;
    }
    q->data[q->rear] = x;
}

int dequeue(struct queue *q) {
    if (is_empty(q)) {
        printf("Error: Queue is empty\n");
        return -1;
    }
    int x = q->data[q->front];
    if (q->front == q->rear) {
        q->front = q->rear = -1;
    } else {
        q->front = (q->front + 1) % MAX_SIZE;
    }
    return x;
}

int peek(struct queue *q) {
    if (is_empty(q)) {
        printf("Error: Queue is empty\n");
        return -1;
    }
    return q->data[q->front];
}

int main() {
    struct queue q;
    init_queue(&q);

    enqueue(&q, 1);
    enqueue(&q, 2);
    enqueue(&q, 3);

    printf("Front element: %d\n", peek(&q));
    printf("Dequeued element: %d\n", dequeue(&q));
    printf("Dequeued element: %d\n", dequeue(&q));
    printf("Front element: %d\n", peek(&q));

    return 0;
}
