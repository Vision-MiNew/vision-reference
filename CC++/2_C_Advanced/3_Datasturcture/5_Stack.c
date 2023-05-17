#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 100

struct stack {
    int data[MAX_SIZE];
    int top;
};

void init_stack(struct stack *s) {
    s->top = -1;
}

int is_empty(struct stack *s) {
    return s->top == -1;
}

int is_full(struct stack *s) {
    return s->top == MAX_SIZE - 1;
}

void push(struct stack *s, int x) {
    if (is_full(s)) {
        printf("Error: Stack is full\n");
        return;
    }
    s->data[++s->top] = x;
}

int pop(struct stack *s) {
    if (is_empty(s)) {
        printf("Error: Stack is empty\n");
        return -1;
    }
    return s->data[s->top--];
}

int peek(struct stack *s) {
    if (is_empty(s)) {
        printf("Error: Stack is empty\n");
        return -1;
    }
    return s->data[s->top];
}

int main() {
    struct stack s;
    init_stack(&s);

    push(&s, 1);
    push(&s, 2);
    push(&s, 3);

    printf("Top element: %d\n", peek(&s));
    printf("Popped element: %d\n", pop(&s));
    printf("Popped element: %d\n", pop(&s));
    printf("Top element: %d\n", peek(&s));

    return 0;
}
