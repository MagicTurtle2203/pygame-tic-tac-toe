class SpotAlreadyTaken(Exception):
    pass


class TicTacToe:
    def __init__(self):
        self.board = self._create_board()
        self.turn = 'x'
        self.winner = None

    def add_move(self, move: int):
        row, col = divmod(move, 3)

        if self.board[row][col] == ' ':
            self.board[row][col] = self.turn
        else:
            raise SpotAlreadyTaken(f"spot already taken by {self.board[row][col]}")

        self.find_winner()

        if self.turn == 'x':
            self.turn = 'o'
        else:
            self.turn = 'x'

    def find_winner(self):
        for col in range(3):
            for row in range(3):
                for coldelta in [-1, 0, 1]:
                    for rowdelta in [-1, 0, 1]:
                        if coldelta != 0 or rowdelta != 0:
                            if self._three_in_a_row(col, row, coldelta, rowdelta):
                                self.winner = self.turn

        if all(self.board[row][col] != ' ' for row in range(3) for col in range(3)) and self.winner is None:
            self.winner = 'tie'

    def display_board(self) -> None:
        for row in range(len(self.board)):
            print('|'.join([self.board[row][col] for col in range(len(self.board[row]))]))

    def _three_in_a_row(self, col: int, row: int, coldelta: int, rowdelta: int) -> bool:
        start_cell = self.board[col][row]

        if start_cell == ' ':
            return False
        else:
            for i in range(1, 3):
                if not 0 <= (col + coldelta * i) < 3 \
                        or not 0 <= (row + rowdelta * i) < 3 \
                        or self.board[col + coldelta *i][row + rowdelta * i] != start_cell:
                    return False
            return True

    @staticmethod
    def _create_board() -> [[str]]:
        new_board = []

        for _ in range(3):
            new_board.append([])
            for _ in range(3):
                new_board[-1].append(' ')

        return new_board


if __name__ == '__main__':
    _ttt = TicTacToe()
    print("Type the number of the cell you wish to place your piece\n"
          "1 is the top left cell and 9 is the bottom right cell")
    while _ttt.winner is None:
        print(f"\n{_ttt.turn}'s turn")
        try:
            _ttt.add_move(int(input("Move: ")) - 1)
        except SpotAlreadyTaken:
            print("pick another spot")
            continue
        _ttt.display_board()
    if _ttt.winner == 'tie':
        print("\nit's a tie!")
    else:
        print(f"\n{_ttt.winner} won!")
