from fuzzywuzzy import process
from os import listdir, getcwd
import blessed

term = blessed.Terminal()
def lfs(func):
    with term.cbreak(), term.fullscreen():
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
                if val.code == 343:
                    o += "\n"
                    print(term.clear)
                    print(f"{o}\n\n")
                    continue
                if val.code == 512:
                    o += "\t"
                    print(term.clear)
                    print(f"{o}\n\n")
                try:
                    if not o:
                        print(term.clear)
                    else:
                        print(func(o))
                except:
                    print(term.clear)
                    print(o)
            elif val:
                print(term.clear)
                o += val
                print(f"{o}\n\n")
                try:
                    if not o:
                        print(term.clear)
                    else:
                        print(func(o))
                except:
                    print(term.clear)
                    print(o)
                    continue


def search(query:str, choices):
    if not query:
        return ""
    totwbp = process.extractBests(query, choices, score_cutoff=50, limit=10000000000000000000000000000)
    lon = []
    for i in totwbp:
        lon.append(i[0])
    return lon

def main(nma):
    files = listdir(getcwd())
    lofs = search(nma, files)
    if not lofs:
        for l in files:
            lofsr += f"{l}\n"
    lofsr = ""
    for l in lofs:
        lofsr += f"{l}\n"
    return lofsr

lfs(main)