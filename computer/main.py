import bitwise as bw

class WireList:
    def __init__(self):
        self.wires:list[bw.wire.Wire] = []
    def getitem(self, index:int):
        return self.wires[index]
    def setitem(self, index:int, value:int):
        self.wires[index] = value
    def add_item(self, value=0):
        self.wires.append(bw.wire.Wire(value=value))

class TempWires(WireList):
    def __init__(self, aow):
        self.wires:list[bw.wire.Wire] = []
        for i in range(aow):
            self.add_item()
output_wires = TempWires(3)
a = bw.wire.Wire()
b = bw.wire.Wire()
cin = bw.wire.Wire()
s = bw.wire.Wire()
count = bw.wire.Wire()

def adder(*inputs):
    bw.gate.XORGate2(a, b, output_wires.wires[0])
    bw.gate.XORGate2(output_wires.wires[0], cin, s)
    bw.gate.ANDGate2(cin, output_wires.wires[0], output_wires.wires[1])
    bw.gate.ANDGate2(a, b, output_wires.wires[2])
    bw.gate.ORGate2(output_wires.wires[1], output_wires.wires[2], count)
    return s, count

def create_truth_table(logic_gates_function):
    for a_val in range(2):
        for b_val in range(2):
            for cin_val in range(2):
                a.value = a_val
                b.value = b_val
                cin.value = cin_val
                logic_gates_function()
                print(f"{a.value} {b.value} {cin.value}  {s} {count}")


create_truth_table(adder)