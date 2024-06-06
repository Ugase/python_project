import fuzzywuzzy.process
from programming_python import load_word_list, slow_typing

def search(query: str, search_list: list):
    """
    This function searches for a word in a given list using the fuzzywuzzy library.
    It normalizes the query and returns the best match based on the score_cutoff and limit parameters.
    If no results are found, it returns None.
    """
    # Normalize the query
    query = query.lower()
    bests = fuzzywuzzy.process.extractBests(query, search_list, score_cutoff=80, limit=50)
    b = []
    for words in bests:
        b.append(words[0])
    if len(bests) == 0:
        return None
    bests_lengths = list(map(lambda x: len(x), b))
    longest = b[bests_lengths.index(max(bests_lengths))]
    return longest

word_list = load_word_list("word_list.txt")
"""
This line loads a word list from a file named 'word_list.txt' using the load_word_list function from the programming_python module.
"""

while True:
    query = input("Enter a word to search for: ")
    if query == "quit":
        break
    else:
        result = search(query, word_list)
        if result is None:
            print("No results found")
        else:
            print(f"{result}")
