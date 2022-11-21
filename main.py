rint("Игра крестики-нолики. Добро пожаловать!")

board = list(range(1, 10))
token = 'X'
step = None


def print_board():
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])


def check_draw():
    if str(board[0]) not in '123456789' and str(board[1]) not in '123456789' and str(board[2]) not in '123456789' and str(board[3]) not in '123456789' and str(board[4]) not in '123456789' and str(board[5]) not in '123456789' and str(board[6]) not in '123456789' and str(board[7]) not in '123456789' and str(board[8]) not in '123456789':
        return True


def check_win():
    if board[0] == board[1] == board[2] or board[3] == board[4] == board[5] or board[6] == board[7] == board[8]:
        return True
    elif board[0] == board[3] == board[6] or board[1] == board[4] == board[7] or board[2] == board[5] == board[8]:
        return True
    elif board[0] == board[4] == board[8] or board[2] == board[4] == board[6]:
        return True


def ask_player():
    global token
    if token == 'X':
        good = False
        while not good:
            print("Куда ходит X?: ")
            step = input()
            try:
                int(step)
            except:
                print("Некорректный ввод. Необходимо выбрать клетку от 0 до 9")
                continue
            if 1 <= int(step) <=9:
                if str(board[int(step)-1]) not in "XO":
                    if int(step) == 1:
                        board[0] = 'X'
                        good = True
                    if int(step) == 2:
                        board[1] = 'X'
                        good = True
                    if int(step) == 3:
                        board[2] = 'X'
                        good = True
                    if int(step) == 4:
                        board[3] = 'X'
                        good = True
                    if int(step) == 5:
                        board[4] = 'X'
                        good = True
                    if int(step) == 6:
                        board[5] = 'X'
                        good = True
                    if int(step) == 7:
                        board[6] = 'X'
                        good = True
                    if int(step) == 8:
                        board[7] = 'X'
                        good = True
                    if int(step) == 9:
                        board[8] = 'X'
                        good = True
                else:
                    print("Клетка занята!")
            else:
                print("Некорректный ввод. Введите число от 1 до 9.")
    else:
        good = False
        while not good:
            print("Куда ходит O?: ")
            step = input()
            try:
                int(step)
            except:
                print("Некорректный ввод. Необходимо выбрать клетку от 0 до 9")
                continue
            if 1 <= int(step) <= 9:
                if str(board[int(step) - 1]) not in "XO":
                    if int(step) == 1:
                        board[0] = 'O'
                        good = True
                    if int(step) == 2:
                        board[1] = 'O'
                        good = True
                    if int(step) == 3:
                        board[2] = 'O'
                        good = True
                    if int(step) == 4:
                        board[3] = 'O'
                        good = True
                    if int(step) == 5:
                        board[4] = 'O'
                        good = True
                    if int(step) == 6:
                        board[5] = 'O'
                        good = True
                    if int(step) == 7:
                        board[6] = 'O'
                        good = True
                    if int(step) == 8:
                        board[7] = 'O'
                        good = True
                    if int(step) == 9:
                        board[8] = 'O'
                        good = True
                else:
                    print("Клетка занята!")
            else:
                print("Некорректный ввод. Введите число от 1 до 9.")


def game():
    global token
    if token == 'X':
        ask_player()
        token = 'O'
    elif token == 'O':
        ask_player()
        token = 'X'


while True:
    if not check_draw():
        if not check_win():
            print_board()
            game()
        else:
            if token == 'O':
                print_board()
                print("X WINS!!!")
                break
            else:
                print_board()
                print("O WINS!!!")
                break
    else:
        print_board()
        print("Ничья!")
        break








