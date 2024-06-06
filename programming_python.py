import calendar as cd
import sys
import time
from pydoc import help
from string import ascii_lowercase as ALPHABET_LOWERCASE
from string import ascii_uppercase as ALPHABET_UPPERCASE
from time import strftime as st

import mathematics as math


def time_date_and_weekday():
    while True:
        try:
            dynamic_typing(st("Date: %B %d %Y, Day: %A, Time: %I:%M:%S %p"))
        except KeyboardInterrupt:
            print("\n")
            break


def get_day(day: int, month: int, year: int):
    r"""Prints out the week day of year-month-day"""
    week_numbers = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saterday",
        6: "Sunday",
    }
    week_num = cd.weekday(year, month, day)
    week_name = week_numbers[week_num]
    print(f"It's {week_name}!")


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


def create_varibles(how_many: int, name, storage):
    for i in range(1, how_many + 1):
        globals()[f"{name}_{i}"] = storage


def dynamic_typing(str):
    sys.stdout.write(f"\r{str}")
    sys.stdout.flush()


def slow_typing(str):
    for letters in str:
        dynamic_typing(letters)
        time.sleep(0.1)


def remove(string: str, what_to: str):
    return string.replace(what_to, "")


def load_word_list(file_path: str) -> list:
    """Load the word list from a file."""
    try:
        with open(file_path) as f:
            return f.read().split()
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        return []


def debug(*var, file="debug.txt"):
    file = open(file, "w")
    for i in var:
        print(i, file=file)
