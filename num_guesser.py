def evaluate_guess():
    """Get the result of the current guess from the user."""
    while True:
        result = input(
            "Is your guess higher or lower than the secret number? (h/l) or 'c' to win: "
        ).strip().lower()
        if result in ["h", "l", "c"]:
            return result
        else:
            print(
                "Invalid input. Please enter 'h' for higher, 'l' for lower, or 'c' if you think you've won."
            )


def binary_search_guess(max_num: int) -> int:
    """Perform a binary search to guess the secret number."""
    low = 0
    high = max_num
    while True:
        midpoint = (low + high) // 2
        print(f"My guess is: {midpoint}")
        result = evaluate_guess()
        if result == "c":
            print("Yay! I won!")
            return midpoint
        elif result == "h":
            low = midpoint + 1
        elif result == "l":
            high = midpoint - 1


def main():
    max_num = int(input("What is the max number? "))
    print("Welcome to the number guessing game!")
    print(f"Think of a number between 0 and {max_num}, and I'll try to guess it.")
    guessed_number = binary_search_guess(max_num)
    print(f"I guessed it! The number was {guessed_number}.")


if __name__ == "__main__":
    main()
