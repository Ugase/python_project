from cmd import Cmd

class CodeInterface:
    def __init__(self, vir_arr_size = int) -> None:
        self.arr = [[0] * vir_arr_size]
    def create_array(self, vir_arr_size: int):
        self.arr.append([0] * vir_arr_size)
    
    def flip(self, bit: int, array_index=0):
        match self.arr[array_index][bit]:
            case 0: self.arr[array_index][bit] = 1
    
    def and_op(self, b1: int, b2: int, out: int, array_index=0):
        self.arr[array_index][out] = self.arr[array_index][b1] & self.arr[array_index][b2]
    
    def or_op(self, b1: int, b2: int, out: int, array_index=0):
        self.arr[array_index][out] = self.arr[array_index][b1] | self.arr[array_index][b2]
    
    def xor_op(self, b1: int, b2: int, out: int, array_index=0):
        self.arr[array_index][out] = self.arr[array_index][b1] ^ self.arr[array_index][b2]
    
    def not_op(self, bit: int, array_index=0):
        match self.arr[array_index][bit]:
            case 0: self.arr[array_index][bit] = 1
            case 1: self.arr[array_index][bit] = 0
    
    def adder(self, a: int, b: int, cin: int, output_indexs: tuple, array_index=0):
        self.arr[array_index][output_indexs[0]] = self.arr[array_index][a] ^ self.arr[array_index][b] ^ self.arr[array_index][cin]
        self.arr[array_index][output_indexs[1]] = (self.arr[array_index][a] & self.arr[array_index][b]) | (self.arr[array_index][a] & self.arr[array_index][cin]) | (self.arr[array_index][b] & self.arr[array_index][cin])

class Interface(Cmd):
    """
    A command-line interface for interacting with a virtual array.
    """
    prompt = "(array) "

    def __init__(self):
        """
        Initialize the interface with a virtual array of a specified size.
        """
        super().__init__()
        self.main_var = CodeInterface(vir_arr_size=int(input("Size of array: ")))

    def do_and(self, line: str):
        """
        Perform a bitwise AND operation on two bits and store the result in a third bit.

        Usage: and <bit1> <bit2> <output_bit>
        """
        a, b, out = map(int, line.split())
        self.main_var.and_op(a, b, out)

    def do_or(self, line: str):
        """
        Perform a bitwise OR operation on two bits and store the result in a third bit.

        Usage: or <bit1> <bit2> <output_bit>
        """
        a, b, out = map(int, line.split())
        self.main_var.or_op(a, b, out)

    def do_xor(self, line: str):
        """
        Perform a bitwise XOR operation on two bits and store the result in a third bit.

        Usage: xor <bit1> <bit2> <output_bit>
        """
        a, b, out = map(int, line.split())
        self.main_var.xor_op(a, b, out)

    def do_not(self, line: str):
        """
        Perform a bitwise NOT operation on a single bit.

        Usage: not <bit>
        """
        bit = int(line)
        self.main_var.not_op(bit)

    def do_flip(self, line: str):
        """
        Flip the value of a single bit.

        Usage: flip <bit>
        """
        bit = int(line)
        self.main_var.flip(bit)

    def do_adder(self, line: str):
        """
        Perform a full adder operation on two bits and a carry-in bit, storing the result in two output bits.

        Usage: adder <bit1> <bit2> <carry_in> <output_bit1> <output_bit2>
        """
        a, b, cin, out1, out2 = map(int, line.split())
        self.main_var.adder(a, b, cin, (out1, out2))

    def do_create_array(self, line: str):
        """
        Create a new virtual array of a specified size.

        Usage: create_array <size>
        """
        vir_arr_size = int(line)
        self.main_var.create_array(vir_arr_size)

    def do_print(self, line: str):
        """
        Print the contents of a virtual array.

        Usage: print [<array_index>]
        """
        array_index = int(line) if line else 0
        print(self.main_var.arr[array_index])

if __name__ == "__main__":
    Interface().cmdloop()