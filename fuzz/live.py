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
                        print(term.clear)
                    else:
                        print(func(o))
                except Exception:
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


def live_fullscreen(func):
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


def live_no_key(func):
    while True:
        print(func())
        print(term.clear)
