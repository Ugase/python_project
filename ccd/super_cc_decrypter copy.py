from random import randint
from string import ascii_lowercase as ALPHABET_LOWERCASE
from string import ascii_uppercase as ALPHABET_UPPERCASE
from time import sleep

import fuzzywuzzy
import fuzzywuzzy.fuzz
import fuzzywuzzy.process
import fuzzywuzzy.StringMatcher
import pdb

SHIFT_RANGE = range(1, 27)


def encode_letters(string: str, shift: int = 1) -> str:
    """Encode letters in the string by shifting them by the given shift."""
    trans_table = str.maketrans(
        ALPHABET_LOWERCASE + ALPHABET_UPPERCASE,
        ALPHABET_LOWERCASE[shift:]
        + ALPHABET_LOWERCASE[:shift]
        + ALPHABET_UPPERCASE[shift:]
        + ALPHABET_UPPERCASE[:shift],
    )
    return string.translate(trans_table)


def decode_letters(string: str, shift: int = 1) -> str:
    """Decode letters in the string by shifting them by the given shift."""
    trans_table = str.maketrans(
        ALPHABET_LOWERCASE + ALPHABET_UPPERCASE,
        ALPHABET_LOWERCASE[-shift:]
        + ALPHABET_LOWERCASE[:-shift]
        + ALPHABET_UPPERCASE[-shift:]
        + ALPHABET_UPPERCASE[:-shift],
    )
    return string.translate(trans_table)


def prune_word_list(words: list[str], word_list: list) -> list:
    """Prune the word list to only include words of the same length as the given word."""
    pruned_word_lists = []
    for word in words:
        pruned_word_lists.append([w for w in word_list if len(w) == len(word)])
    return pruned_word_lists


def sum_of_ratios(split_up_words: list[str], words: list) -> float:
    """Calculate the sum of ratios for the given words."""
    ratios = []
    for word in split_up_words:
        pruned_list = prune_word_list([word], words)[0]
        ratios.append(
            fuzzywuzzy.fuzz.ratio(
                word, fuzzywuzzy.process.extractOne(word, pruned_list)
            )
        )
    return sum(ratios)


def find_shift(encrypted_text: str, dictionary: list) -> int:
    """Find the shift value that decrypts the encrypted text."""
    decryption_list = [decode_letters(encrypted_text, i) for i in SHIFT_RANGE]
    ratios = [sum_of_ratios(t.split(), dictionary) for t in decryption_list]
    return SHIFT_RANGE[ratios.index(max(ratios))]


def load_word_list(file_path: str) -> list:
    """Load the word list from a file."""
    try:
        with open(file_path) as f:
            return f.read().split()
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        return []


def main():
    word_list = load_word_list("E:\\Coding_Projects\\Python\\ccd\\word_list.txt")
    shift = randint(1, 26)
    text = encode_letters(
        """
Hello, Sniper John
Go to Port 45 to snipe their commander

- Commander Mark
""",
        shift,
    )
    print("We've Intercepted their text Mr. Commander, but its's encrypted :")
    sleep(2)
    print("Here it is:")
    sleep(2)
    print(text)
    sleep(2)
    print("Oh no the text is encrypted")
    sleep(2)
    print("I have a way")
    sleep(2)
    shift_found = find_shift(text, word_list)
    print(decode_letters(text, shift_found))
    sleep(1)
    print("There we go! now we know to guard port 45")


if __name__ == "__main__":
    main()
