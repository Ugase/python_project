import hashlib

def hash(string:str):
    string = string.encode(errors="ignore")
    return hashlib.sha512(string).hexdigest()