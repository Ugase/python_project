import random
import blessed

term = blessed.Terminal()


def live(func):
    with term.cbreak():
        val = ""
        o = ""
        while True:
            val = term.inkey(
                timeout=99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            )
            if val.is_sequence:
                if val.code == 361:
                    break
                if val.code == 263:
                    if temp := list(o):
                        del temp[-1]
                        o = "".join(temp)
                        del temp
                    print(term.clear)
                    print(f"{o}\n\n")
                    continue
                if val.code == 343:
                    o += "\n"
                    print(term.clear)
                    print(f"{o}\n\n")
                if val.code == 512:
                    o += "\t"
                    print(term.clear)
                    print(f"{o}\n\n")
                try:
                    if not o:
                        print()
                    else:
                        o = func(o)
                        print(o)
                except Exception:
                    print(o)
            elif val:
                print(term.clear)
                o += val
                print(f"{o}\n\n")
                try:
                    if not o:
                        print(term.clear)
                    else:
                        o = func(o)
                        print(o)
                except:
                    print(term.clear)
                    print(o)
                    continue


def load_word_list(file_path: str) -> list:
    """Load the word list from a file."""
    try:
        with open(file_path) as f:
            return f.read().split()
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        return []

word_list = load_word_list("E:\\Coding_Projects\\Python\\fuzz\\word_list.txt")

def replace(letter: str):
    return random.choice(word_list) + " "

live(replace)
