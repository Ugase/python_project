from time import sleep
import chess
import random
import blessed
import chess.pgn


def unicode_chess(board:chess.Board):
    sym = chess.UNICODE_PIECE_SYMBOLS
    return "".join(
        sym[i]
        if i in ["k", "q", "n", "b", "r", "p", "K", "Q", "N", "B", "R", "P"]
        else i
        for i in str(board)
    )
moves = []
t = blessed.Terminal()
board =  chess.Board()
while not board.is_game_over():
    move = random.choice(list(board.generate_legal_moves()))
    if board.is_fifty_moves() or board.is_insufficient_material() or board.is_fivefold_repetition():
        break
    board.push(move)
    print(t.clear)
    print(unicode_chess(board))

moves = board.move_stack

pgn = chess.pgn.Game()
pgn.setup(board)

for move in moves:
    board.push(move)
    pgn.add_variation(move)
    board.pop()

pgn_str = str(pgn)