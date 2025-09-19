#include <stdio.h>

int main() {
    int n, i;
    unsigned long long fact = 1;  // Use long long to handle large factorials

    printf("Enter a number: ");
    scanf("%d", &n);

    if (n < 0) {
        printf("Factorial of a negative number doesn't exist.\n");
    } else {
        for (i = 1; i <= n; i++) {
            fact *= i;
        }
        printf("Factorial of %d = %llu\n", n, fact);
    }

    return 0;
}
