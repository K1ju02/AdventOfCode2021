def check_win(board):
    col_count = [0,0,0,0,0]
    for line in board:
        x = line.count(-1)
        if x == 5:
            return True
        for i in range(len(line)):
            if line[i] == -1:
                col_count[i] += 1
    for count in col_count:
        if count == 5:
            return True
    return False

def calc_board(board):
    sum = 0
    for line in board:
        for i in line:
            if i == -1:
                continue
            else:
                sum += i
    return sum

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

    for draw in draws:
        for board in results:
            for n in range(5):
                for i in range(5):
                    if int(draw) == board[n][i]:
                        board[n][i] = -1
            if check_win(board):
                return calc_board(board) * int(draw)

if __name__ == '__main__':
    print(solve())