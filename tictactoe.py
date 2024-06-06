class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def __str__(self):
        return '\n'.join([' '.join([str(self.data[i][j]) for j in range(self.cols)]) for i in range(self.rows)])

    def assign(self, values):
        if len(values)!= self.rows:
            raise ValueError("Number of rows in values does not match matrix")
        for i in range(self.rows):
            if len(values[i])!= self.cols:
                raise ValueError("Number of columns in values does not match matrix")
            for j in range(self.cols):
                self.data[i][j] = values[i][j]

    def get_value(self, row, col):
        if row < self.rows and col < self.cols:
            return self.data[row][col]
        raise IndexError("Index out of range")

    def set_value(self, row, col, data):
        if row < self.rows and col < self.cols:
            self.data[row][col] = data
        raise IndexError("Index out of range")


class Board:
    def __init__(self, board_height: int, board_length: int) -> None:
        self.board_height = board_height
        self.board_length = board_length
        self.board: Matrix = Matrix(self.board_length, self.board_height)
        self.last_move = None

    def translate(self, num: int):
        row = 0
        col = 0
        a = 0
        while a < num:
            a += 1
            col += 1
            if col > self.board_height:
                col = 0
                row += 1
        return row, col-1

    def make_move(self, player, num):
        row, col = self.translate(num-1)
        if self.board.get_value(row, col) != 0:
            raise ValueError("Invalid move, position already occupied")
        self.board.set_value(row, col, player)
        self.last_move = (row, col)

    def check_win(self):
        row, col = self.last_move
        player = self.board.get_value(row, col)
        # Check horizontal
        for i in range(self.board_height):
            if self.board.get_value(row, i) != player:
                break
            if i == self.board_height - 1:
                return True
        # Check vertical
        for i in range(self.board_length):
            if self.board.get_value(i, col) != player:
                break
            if i == self.board_length - 1:
                return True
        # Check diagonal (top-left to bottom-right)
        for i in range(1, min(self.board_length, self.board_height)):
            if self.board.get_value(row+i, col+i) != player:
                break
            if i == min(self.board_length, self.board_height) - 1:
                return True
        # Check diagonal (bottom-left to top-right)
        for i in range(1, min(self.board_length, self.board_height)):
            if self.board.get_value(row-i, col+i) != player:
                break
            if i == min(self.board_length, self.board_height) - 1:
                return True
        return False

t = Board(5, 5)
t.make_move()