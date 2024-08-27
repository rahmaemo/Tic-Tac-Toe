import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

class Player:
    def __init__(self):
        self.name = ""
        self.symbol = ""

    def choose_name(self):
        while True:
            name = input("Enter your name: ")
            if name.isalpha():
                self.name = name
                break
            else:
                print("Invalid name. Please use only alphabetic characters.")

    def choose_symbol(self):
        while True:
            symbol = input("Enter your symbol (single character): ")
            if symbol.isalpha() and len(symbol) == 1:
                self.symbol = symbol.upper()
                break
            else:
                print(f"Invalid symbol. {self.name}, please enter a valid single character.")

class Menu:
    def display_main_menu(self):
        print("Welcome to the Tic-Tac-Toe game!")
        print("1. Start Game")
        print("2. Quit Game")
        while True:
            choice = input("Enter your choice (1 or 2): ")
            if choice == "1" or choice == "2":
                return choice
            else:
                print("Invalid choice. Please enter 1 or 2.")

    def end_game_menu(self):
        choice = input("1. Restart Game\n2. Quit Game\nEnter your choice (1 or 2): ")
        return choice

class Board:
    def __init__(self):
        self.reset_board()

    def display_board(self):
        for i in range(0, 9, 3):
            print("|".join(self.board[i:i+3]))
            if i < 6:
                print("-----")

    def is_valid_move(self, choice):
        return self.board[choice - 1].isdigit()

    def update_board(self, choice, symbol):
        if self.is_valid_move(choice):
            self.board[choice - 1] = symbol
            return True
        return False

    def reset_board(self):
        self.board = [str(i) for i in range(1, 10)]

class Game:
    def __init__(self):
        self.players = [Player(), Player()]
        self.board = Board()
        self.menu = Menu()
        self.current_player_index = 0

    def start_game(self):
        choice = self.menu.display_main_menu()
        if choice == "1":
            self.set_up_player()
            self.play_game()
        else:
            self.quit_game()

    def set_up_player(self):
        for num, player in enumerate(self.players, start=1):
            print(f"Player {num}, enter your details:")
            player.choose_name()
            player.choose_symbol()
            clear_screen()

    def play_game(self):
        while True:
            self.play_turn()
            self.board.display_board()
            if self.check_win() or self.check_draw():
                choice = self.menu.end_game_menu()
                if choice == "1":
                    self.restart_game()
                else:
                    self.quit_game()
                    break

    def restart_game(self):
        self.board.reset_board()
        self.start_game()

    def play_turn(self):
        current_player = self.players[self.current_player_index]
        while True:
            try:
                move = int(input(f"{current_player.name}'s turn ({current_player.symbol}). Enter a move (1-9): "))
                if 1 <= move <= 9 and self.board.is_valid_move(move):
                    self.board.update_board(move, current_player.symbol)
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Please enter a number between 1 and 9.")

        self.current_player_index = 1 - self.current_player_index

    def check_win(self):
        lines = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)               # Diagonals
        ]
        for a, b, c in lines:
            if self.board.board[a] == self.board.board[b] == self.board.board[c] and self.board.board[a] in ['X', 'O']:
                winner_symbol = self.board.board[a]
                winner = next(player for player in self.players if player.symbol == winner_symbol)
                print(f"Player {winner.name} wins!")
                return True

        return False

    def check_draw(self):
        if all(cell in ['X', 'O'] for cell in self.board.board):
            print("It's a draw!")
            return True
        return False

    def quit_game(self):
        print("Thanks for playing!")
        exit()

if __name__ == "__main__":
    game = Game()
    game.start_game()





