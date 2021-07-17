class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n
        self.hori = [0] * n
        self.vert = [0] * n
        self.diag = 0
        self.anti_diag = 0

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        move = 1
        if player == 2:
            move = -1
        self.vert[row] += move
        self.hori[col] += move
        if row == col:
            self.diag += move
        if row + col == self.n - 1:
            self.anti_diag += move
        if abs(self.vert[row]) == self.n or  abs(self.hori[col]) == self.n or  abs(self.diag) == self.n or abs(self.anti_diag) == self.n:
            return player
        return 0
    
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
