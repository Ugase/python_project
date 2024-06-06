#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

typedef enum {
    GUESS_LOWER,
    GUESS_HIGHER,
    GUESS_CORRECT,
} GuessResult;

GuessResult evaluate_guess() {
    char result[80];
    while (1) {
        printf("Is your guess higher or lower than the secret number? (h/l) or 'c' to win: ");
        fgets(result, sizeof(result), stdin);
        result[strcspn(result, "\n")] = '\0';
        if (result[0] == 'h' || result[0] == 'l' || result[0] == 'c') {
            return result[0] == 'h' ? GUESS_HIGHER : (result[0] == 'l' ? GUESS_LOWER : GUESS_CORRECT);
        } else {
            printf("Invalid input. Please enter 'h' for higher, 'l' for lower, or 'c' if you think you've won.\n");
        }
    }
}

int binary_search_guess(int max_num) {
    int low = 0;
    int high = max_num;
    while (1) {
        int midpoint = (low + high) / 2;
        printf("My guess is: %d\n", midpoint);
        GuessResult res = evaluate_guess();
        if (res == GUESS_CORRECT) {
            printf("Yay! I won!\n");
            return midpoint;
        } else if (res == GUESS_HIGHER) {
            low = midpoint + 1;
        } else if (res == GUESS_LOWER) {
            high = midpoint - 1;
        }
    }
}

int main() {
    int max_num;
    printf("What is the max number? ");
    scanf("%d", &max_num);
    printf("Welcome to the number guessing game!\n");
    printf("Think of a number between 0 and %d, and I'll try to guess it.\n", max_num);
    int guessed_number = binary_search_guess(max_num);
    printf("I guessed it! The number was %d.\n", guessed_number);
    return 0;
}