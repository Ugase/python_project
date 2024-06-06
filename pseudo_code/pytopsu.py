import argparse

pytopsu = argparse.ArgumentParser(description="Turns python to pseudo code")
pytopsu.add_argument("script", help="The script which to be turned to pseudo code")
parsed = pytopsu.parse_args()
file = parsed.script

with open(file) as python_file:
    psu = python_file.read()
    psu = psu.replace("def", "func")
    psu = psu.replace("return", "give")
    psu = psu.replace("import", "imp")
    psu = psu.replace("while", "loop")
    psu = psu.replace("for", "loopl")
with open(f"{file.replace(".py", ".pu")}", "w") as pu_file:
    pu_file.write(psu)