#include <stdio.h>

// Function prototypes
void displayMenu();
int addition(int num1, int num2);
int subtraction(int num1, int num2);
int multiplication(int num1, int num2);
int division(int num1, int num2);

int main() {
    int choice;
    int num1, num2;
    int result;
    
    do {
        displayMenu();
        
        // user input your choice
        printf("Enter your choice: ");
        scanf("%d", &choice);
        
        // user choice and perform operation
        switch(choice) {
            case 1: 
                printf("Enter first number: ");
                scanf("%d", &num1);
                printf("Enter second number: ");
                scanf("%d", &num2);
                result = addition(num1, num2);
                printf("Addition = %d\n", result);
                break;
            case 2:
                printf("Enter first number: ");
                scanf("%d", &num1);
                printf("Enter second number: ");
                scanf("%d", &num2);
                result = subtraction(num1, num2);
                printf("Subtraction = %d\n", result);
                break;
            case 3:
                printf("Enter first number: ");
                scanf("%d", &num1);
                printf("Enter second number: ");
                scanf("%d", &num2);
                result = multiplication(num1, num2);
                printf("Multiplication = %d\n", result);
                break;
            case 4:
                printf("Enter first number: ");
                scanf("%d", &num1);
                printf("Enter second number : ");
                scanf("%d", &num2);
                result = division(num1, num2);
                printf("Division = %d\n", result);
                break;
            case 5:
                printf("Exiting program. Thank you!\n");
                break;
            default:
                printf("Invalid choice\n");
        }
        
    } while (choice != 5);
    
}

// Function definitions
void displayMenu() {
    printf("---------- Menu ----------\n");
    printf("1. Addition\n");
    printf("2. Subtraction\n");
    printf("3. Multiplication\n");
    printf("4. Division\n");
    printf("5. Exit\n");
}

int addition(int num1, int num2) {
    return num1 + num2;
}

int subtraction(int num1, int num2) {
    return num1 - num2;
}

int multiplication(int num1, int num2) {
    return num1 * num2;
}

int division(int num1, int num2) {
    return num1 / num2;
}

