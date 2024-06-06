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
            if f.read() and f.read >= 64:
                return 0
    except FileNotFoundError:
        return 1

def pad(string:str, num:int):
    if len(string) % num:
        return string
    for i in range(len(string)//2):
        if i*num > len(string):
            high = num*i
            break
        continue
    string2 = string+"x"*(high-len(string))
    return string2


def create_master_password(password: str):
    password = pad(password, 32)
    with open("masterpassword.txt", "wb") as f:
        f.write(e.encrypt(password, bytes(password.encode("utf-8"))))


def verify_master_password(password: str):
    password = pad(password, 32)
    key = bytes(password.encode("utf-8", "ignore"))
    with open("masterpassword.txt", "rb") as f:
        encrypted_master_password = f.read()
    decrypted_master_password = e.decrypt(encrypted_master_password, key)

    return password == decrypted_master_password

def ask_master_password():
    return input("Master password: ")

