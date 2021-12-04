import day4.puz1 as help
import numpy as np

def solve():
    file = open("input4.txt")
    lines = file.read()
    lines = lines.split('\n')
    draws = lines.pop(0).split(',')
    boards = []
    results = []
    for x in range(0, len(lines), 6):
        board = lines[x+1:x+6]
        boards += [board]

    for board in boards:
        for i in range(len(board)):
            line = []
            for s in board[i].split(' '):
                if len(s) > 0:
                    line += [int(s)]
            board[i] = line
        results += [board]

    scores = []
    won_boards = []
    for draw in draws:
        for board in results:
            if won_boards.__contains__(board):
                continue
            for n in range(5):
                for i in range(5):
                    if int(draw) == board[n][i]:
                        board[n][i] = -1
            if help.check_win(board):
                scores += [help.calc_board(board) * int(draw)]
                won_boards += [board]
    return scores[-1]

if __name__ == '__main__':
    print(solve())