import collections

the = "The quick brown fox jumps over the lazy dog"

def count(thing):
    return dict(collections.Counter(the))

print(count(the))