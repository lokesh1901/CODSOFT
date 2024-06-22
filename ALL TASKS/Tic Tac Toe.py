import random

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'

    def print_board(self):
        print(f"{self.board[0]} | {self.board[1]} | {self.board[2]}")
        print("---+---+---")
        print(f"{self.board[3]} | {self.board[4]} | {self.board[5]}")
        print("---+---+---")
        print(f"{self.board[6]} | {self.board[7]} | {self.board[8]}")

    def is_valid_move(self, move):
        return self.board[move] == ' '

    def make_move(self, move):
        if self.is_valid_move(move):
            self.board[move] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        return False

    def check_win(self):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != ' ':
                return True
        return False

    def minimax(self, depth, is_maximizing):
        if self.check_win():
            if is_maximizing:
                return -1
            else:
                return 1
        if not any(cell == ' ' for cell in self.board):
            return 0

        if is_maximizing:
            best_score = -2
            for i in range(9):
                if self.is_valid_move(i):
                    self.make_move(i)
                    score = self.minimax(depth + 1, False)
                    self.undo_move(i)
                    best_score = max(best_score, score)
            return best_score

        else:
            best_score = 2
            for i in range(9):
                if self.is_valid_move(i):
                    self.make_move(i)
                    score = self.minimax(depth + 1, True)
                    self.undo_move(i)
                    best_score = min(best_score, score)
            return best_score

    def alphabeta(self, depth, is_maximizing, alpha, beta):
        if self.check_win():
            if is_maximizing:
                return -1
            else:
                return 1
        if not any(cell == ' ' for cell in self.board):
            return 0

        if is_maximizing:
            best_score = -2
            for i in range(9):
                if self.is_valid_move(i):
                    self.make_move(i)
                    score = self.alphabeta(depth + 1, False, alpha, beta)
                    self.undo_move(i)
                    best_score = max(best_score, score)
                    alpha = max(alpha, score)
                    if beta <= alpha:
                        break
            return best_score

        else:
            best_score = 2
            for i in range(9):
                if self.is_valid_move(i):
                    self.make_move(i)
                    score = self.alphabeta(depth + 1, True, alpha, beta)
                    self.undo_move(i)
                    best_score = min(best_score, score)
                    beta = min(beta, score)
                    if beta <= alpha:
                        break
            return best_score

    def undo_move(self, move):
        self.board[move] = ' '

    def play(self):
        while True:
            self.print_board()
            move = input("Enter your move (1-9): ")
            move = int(move) - 1
            if not self.make_move(move):
                print("Invalid move. Try again.")
                continue
            if self.check_win():
                self.print_board()
                print("You win!")
                break
            if all(cell != ' ' for cell in self.board):
                print("It's a tie!")
                break
            move = self.alphabeta(0, True, -2, 2)
            self.make_move(move)
            if self.check_win():
                self.print_board()
                print("AI wins!")
                break

if __name__ == "__main__":
    game = TicTacToe()
    game.play()

