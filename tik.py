import random
import copy


def grid(board):
    print(" ---" * 3)
    for i in range(3):
        print(f"| {board[i][0]} | {board[i][1]} | {board[i][2]} |")
        print(" ---" * 3)


def check_win(board, symbol):
    for i in range(3):
        if [board[i][j] for j in range(3)] == [symbol, symbol, symbol]:
            return True
    for j in range(3):
        if [board[i][j] for i in range(3)] == [symbol, symbol, symbol]:
            return True
    if [board[i][i] for i in range(3)] == [symbol, symbol, symbol]:
        return True
    if board[2][0] == board[1][1] == board[0][2] == symbol:
        return True
    return False


def standoff(now_board):
    space = ' '
    for row in now_board:
        if space in row:
            return False
    return True


def evaluate_score(now_board, first_player):
    if first_player == 'computer':
        if check_win(now_board, symbol='X'):
            return 1
        if check_win(now_board, symbol='O'):
            return -1
    if first_player == 'human':
        if check_win(now_board, symbol='O'):
            return 1
        if check_win(now_board, symbol='X'):
            return -1
    return 0
        

def start_game():
    board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]
    players = ['human', 'computer']
    first_player = random.choice(players)
    if first_player == 'human':
        while True:

            human_turn(board, symbol='X')
            if check_win(board, symbol='X'):
                grid(board)
                print('Победа человека')
                break
            if standoff(board):
                grid(board)
                print('Ничья')
                break
            
            computer_turn(board, first_player, symbol='O')
            if check_win(board, symbol='O'):
                grid(board)
                print('Победа компьютера')
                break
    else:
        while True:

            computer_turn(board, first_player, symbol='X')
            if check_win(board, symbol='X'):
                grid(board)
                print('Победа компьютера')
                break 
            if standoff(board):
                grid(board)
                print('Ничья')
                break

            human_turn(board, symbol='O')
            if check_win(board, symbol='O'):
                grid(board)
                print('Победа человека')
                break


def human_turn(board, symbol):
    grid(board)
    while True:
        try:
            row = int(input('Введите номер строчки: ')) - 1
            column = int(input('Введите номер колонки: ')) - 1
            if row not in range(3) or column not in range(3):
                print('Введите значение от 1 до 3!\n')
                continue
            elif board[row][column] != ' ':
                print('Выберите пустую клетку!\n')
                continue
            else:
                board[row][column] = symbol
                return board
        except ValueError:
            print('Введите корректное значение!\n')


def computer_turn(board, first_player, symbol):
    row, column = minimax(board, first_player, True, symbol, depth=6)[1]
    board[row][column] = symbol
    return board


def minimax(now_board, first_player, is_maximizing, symbol, depth):
    if check_win(now_board, symbol) or standoff(now_board) or depth == 0:
        return [evaluate_score(now_board, first_player), '']
    best_move = 'a   a'
    if is_maximizing == True and first_player == 'computer':
        best_score = -float('inf')
        symbol = 'X'
    elif is_maximizing == True and first_player == 'human':
        best_score = -float('inf')
        symbol = 'O'
    if is_maximizing == False and first_player == 'computer':
        best_score = float('inf')
        symbol = 'O'
    elif is_maximizing == False and first_player == 'human':
        best_score = float('inf')
        symbol = 'X'
    for i in range(3):
        for j in range(3):
            if now_board[i][j] == ' ':
                new_board = copy.deepcopy(now_board)
                new_board[i][j] = symbol
                predicted_score = minimax(new_board, first_player, not is_maximizing, symbol, depth-1)[0]
                if is_maximizing == True and predicted_score > best_score:
                    best_score = predicted_score
                    best_move = [i, j]

                if is_maximizing == False and predicted_score < best_score:
                    best_score = predicted_score
                    best_move = [i, j]

    return [best_score, best_move]


if __name__ == '__main__':
    start_game()