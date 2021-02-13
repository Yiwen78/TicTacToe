from enum import Enum

# use emoji to make the board enjoyable
X = '✕'
O = '❍'


class TicTacToe:
    class STATES(Enum):
        CROSS_TURN = 0
        NAUGHT_TURN = 1
        DRAW = 2
        CROSS_WON = 3
        NAUGHT_WON = 4

    def __init__(self):
        class STATES(Enum):
            CROSS_TURN = 0
            NAUGHT_TURN = 1
            DRAW = 2
            CROSS_WON = 3
            NAUGHT_WON = 4

        self.board = [[' ' for x in range(3)] for y in range(3)]
        self.counter = 0
        self.print_board()

    def place_marker(self, symbol, row, column):
        self.counter += 1
        self.board[row][column] = symbol

    def condition(self):
        # Rows
        if self.board[0][0] == self.board[0][1] == self.board[0][2] and self.board[0][0] != ' ':
            return self.board[0][0]
        if self.board[1][0] == self.board[1][1] == self.board[1][2] and self.board[1][0] != ' ':
            return self.board[1][0]
        if self.board[2][0] == self.board[2][1] == self.board[2][2] and self.board[2][0] != ' ':
            return self.board[2][0]

        # Columns
        if self.board[0][0] == self.board[1][0] == self.board[2][0] and self.board[0][0] != ' ':
            return self.board[0][0]
        if self.board[0][1] == self.board[1][1] == self.board[2][1] and self.board[0][1] != ' ':
            return self.board[0][1]
        if self.board[0][2] == self.board[1][2] == self.board[2][2] and self.board[0][2] != ' ':
            return self.board[0][2]

        # Diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != ' ':
            return self.board[0][2]

        return False

    def print_board(self):
        for i in range(0, 3):
            for j in range(0, 3):
                print(f'[{self.board[i][j]}]', end=' ')
            print()


class Game(TicTacToe):

    def start(self):
        class STATES(Enum):
            CROSS_TURN = 0
            NAUGHT_TURN = 1
            DRAW = 2
            CROSS_WON = 3
            NAUGHT_WON = 4

        row = None
        column = None
        input_number = None
        symbol = X

        if self.counter % 2 == 0:
            print(STATES(0))
        else:
            print(STATES(1))

        try:
            row = int(input('Input row number 0 to 2: '))
            if not 0 <= row <= 2:
                raise ValueError

        except ValueError:
            print('Please input a valid number')
            self.start()
            return

        try:
            column = int(input('Input column number 0 to 2: '))
            if not 0 <= column <= 2:
                raise ValueError

        except ValueError:
            print('Please input a valid number')
            self.start()
            return

        if (self.board[row][column] == X) or (self.board[row][column] == O):
            print('This place is already occupied')
            self.start()

        else:
            if self.counter % 2 == 0:
                symbol = X
            else:
                symbol = O
            self.place_marker(symbol, row, column)

        self.print_board()
        self.check()

    def check(self):
        class STATES(Enum):
            CROSS_TURN = 0
            NAUGHT_TURN = 1
            DRAW = 2
            CROSS_WON = 3
            NAUGHT_WON = 4

        winner = self.condition()

        if not winner:
            if self.counter != 9:
                self.start()
            else:
                print(STATES(2))

        if winner == X:
            print(STATES(3))

        if winner == O:
            print(STATES(4))


if __name__ == '__main__':
    obj = Game()
    obj.start()
