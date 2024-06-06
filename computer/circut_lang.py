def parse_code(code: str):
    code_lines = code.split("\n")
    del code_lines[0]
    del code_lines[-1]
    var = {}
    max_index = 0
    wire_list = []
    functions = {}
    current_function = None
    function_lines = []

    for line in code_lines:
        line = line.split()
        if line[0] == "wire":
            var.update({line[1]:max_index})
            max_index += 1
            wire_list.append(0)
        if line[0] == "et":
            if int(line[2]) > 1:
                print("Error: Can only set 0 or 1")
                quit(1)
            try:
                wire_list[var[line[1]]] = int(line[2])
            except IndexError:
                print(f"Wire {line[1]} does'nt exist")
                quit(1)
        if line[0] == "gate":
            gate = line[1]
            aoi = 2
            if gate == "and":
                aoo = 1
            elif gate == "or":
                aoo = 1
            elif gate == "xor":
                aoo = 1
            elif gate == "not":
                aoi = 1
                aoo = 0
            inputs = line[2:]
            if len(inputs) > (aoo + aoi) or len(inputs) < (aoo + aoi):
                print("Too much or too little inputs or outputs")
                quit(1)
            for input_var in inputs:
                if input_var not in var:
                    var.update({input_var:max_index})
                    max_index += 1
                    wire_list.append(0)
            if gate == "and":
                output = inputs.pop(-1)
                wire_list[var[output]] = int(wire_list[var[inputs[0]]] and wire_list[var[inputs[1]]])
            if gate == "or":
                output = inputs.pop(-1)
                wire_list[var[output]] = int(wire_list[var[inputs[0]]] or wire_list[var[inputs[1]]])
            if gate == "xor":
                output = inputs.pop(-1)
                wire_list[var[output]] = int(wire_list[var[inputs[0]]] ^ wire_list[var[inputs[1]]])
            if gate == "not":
                output = inputs.pop(-1)
                wire_list[var[output]] = int(not wire_list[var[output]])
        if line[0] == "print":
            try:
                print(wire_list[var[line[1]]])
            except IndexError:
                print("Variable does not exist")
        if line[0] == "func":
            current_function = line[1]
            functions[current_function] = {"inputs": line[2:], "lines": []}
        if current_function:
            functions[current_function]["lines"].append(line)
        if line[0] == "end":
            current_function = None
        if line[0] == "call":
            func_name = line[1]
            inputs = line[2:]
            if func_name not in functions:
                print(f"Function {func_name} does not exist")
                quit(1)
            if len(inputs) != len(functions[func_name]["inputs"]):
                print(f"Function {func_name} expects {len(functions[func_name]['inputs'])} inputs, but got {len(inputs)}")
                quit(1)
            func_vars = {}
            for i, input_var in enumerate(functions[func_name]["inputs"]):
                func_vars[input_var] = var[inputs[i]]
            for func_line in functions[func_name]["lines"]:
                if func_line[0] == "wire":
                    var.update({func_line[1]:max_index})
                    max_index += 1
                    wire_list.append(0)
                if func_line[0] == "et":
                    if int(func_line[2]) > 1:
                        print("Error: Can only set 0 or 1")
                        quit(1)
                    try:
                        wire_list[func_vars[func_line[1]]] = int(func_line[2])
                    except IndexError:
                        print(f"Wire {func_line[1]} does'nt exist")
                        quit(1)
                if func_line[0] == "gate":
                    gate = func_line[1]
                    aoi = 2
                    if gate == "and":
                        aoo = 1
                    elif gate == "or":
                        aoo = 1
                    elif gate == "xor":
                        aoo = 1
                    elif gate == "not":
                        aoi = 1
                        aoo = 0
                    inputs = func_line[2:]
                    if len(inputs) > (aoo + aoi) or len(inputs) < (aoo + aoi):
                        print("Too much or too little inputs or outputs")
                        quit(1)
                    if gate == "and":
                        output = inputs.pop(-1)
                        wire_list[func_vars[output]] = int(wire_list[func_vars[inputs[0]]] and wire_list[func_vars[inputs[1]]])
                    if gate == "or":
                        output = inputs.pop(-1)
                        wire_list[func_vars[output]] = int(wire_list[func_vars[inputs[0]]] or wire_list[func_vars[inputs[1]]])
                    if gate == "xor":
                        output = inputs.pop(-1)
                        wire_list[func_vars[output]] = int(wire_list[func_vars[inputs[0]]] ^ wire_list[func_vars[inputs[1]]])
                    if gate == "not":
                        output = inputs.pop(-1)
                        wire_list[func_vars[output]] = int(not wire_list[func_vars[output]])
                if func_line[0] == "print":
                    try:
                        print(wire_list[func_vars[func_line[1]]])
                    except IndexError:
                        print("Variable does not exist")

code = """
func full_adder a b cin
wire sum
wire cout
gate and t1 a b
gate and t2 a cin
gate and t3 b cin
gate or sum a b cin
gate or cout t1 t2 t3
end

call full_adder 0 0 0
print sum
print cout

call full_adder 0 0 1
print sum
print cout

call full_adder 0 1 0
print sum
print cout

call full_adder 0 1 1
print sum
print cout

call full_adder 1 0 0
print sum
print cout

call full_adder 1 0 1
print sum
print cout

call full_adder 1 1 0
print sum
print cout

call full_adder 1 1 1
print sum
print cout
"""

parse_code(code)