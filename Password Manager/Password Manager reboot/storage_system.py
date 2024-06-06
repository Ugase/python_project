import encryption as e


def ex():
    try:
        with open("passwords.json", "r") as f:
            if not f.read():
                with open("passwords.json", "w") as f:
                    f.write("{}")
    except FileNotFoundError:
        with open("passwords.json", "w") as f:
                f.write("{}")
    try:
        with open("masterpassword.txt") as f:
            if not f.read():
                return 2
            if f.read():
                return 0
    except FileNotFoundError:
        return 1


def create_master_password(password: str):
    with open("masterpassword.txt", "w") as f:
        f.write(e.hash(password))


def verify_master_password(password: str):
    with open("masterpassword.txt", "r") as y:
        return y.read() == e.hash(password)

def ask_master_password():
    return input("Master password: ")

