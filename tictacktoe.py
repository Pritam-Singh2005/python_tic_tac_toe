import os
import random
import time
from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

INDENT = " " * 10  # consistent left padding for alignment


class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None
        
    def print_board(self):
        """Display the game board neatly aligned"""
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print(f"\n{Fore.CYAN}{'='*40}")
        print(f"{Fore.CYAN}{' '*12}TIC TAC TOE")
        print(f"{Fore.CYAN}{'='*40}\n")
        
        for row_index, row in enumerate([self.board[i*3:(i+1)*3] for i in range(3)]):
            print(INDENT, end="")
            for i, cell in enumerate(row):
                if cell == 'X':
                    print(f"{Back.BLUE}{Fore.WHITE} {cell} {Style.RESET_ALL}", end="")
                elif cell == 'O':
                    print(f"{Back.RED}{Fore.WHITE} {cell} {Style.RESET_ALL}", end="")
                else:
                    print(f"{Fore.YELLOW} {cell} {Style.RESET_ALL}", end="")
                
                if i < 2:
                    print(f"{Fore.WHITE}|{Style.RESET_ALL}", end="")
            print()
            if row_index < 2:
                print(INDENT + f"{Fore.WHITE}---+---+---{Style.RESET_ALL}")
        print()
    
    def print_board_nums(self):
        """Show available positions"""
        print(f"\n{Fore.GREEN}Available positions:{Style.RESET_ALL}")
        for i in range(3):
            print(INDENT, end="")
            print(f" {i*3} | {i*3 + 1} | {i*3 + 2}")
            if i < 2:
                print(INDENT + "---+---+---")
        print()
    
    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        # Row check
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([s == letter for s in row]):
            return True
        
        # Column check
        col_ind = square % 3
        column = [self.board[col_ind + i*3] for i in range(3)]
        if all([s == letter for s in column]):
            return True
        
        # Diagonals
        if square % 2 == 0:
            if all([self.board[i] == letter for i in [0,4,8]]):
                return True
            if all([self.board[i] == letter for i in [2,4,6]]):
                return True
        return False


class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass


class HumanPlayer(Player):
    def get_move(self, game):
        valid = False
        val = None
        while not valid:
            square = input(f"{Fore.CYAN}Your turn ({self.letter}). Enter position (0-8): {Style.RESET_ALL}")
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid = True
            except ValueError:
                print(f"{Fore.RED}Invalid input. Try again.{Style.RESET_ALL}")
        return val


class ComputerPlayer(Player):
    """Unbeatable AI using Minimax"""
    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())  # first move random
        else:
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        max_player = self.letter  # AI
        other_player = 'O' if player == 'X' else 'X'

        # Base cases
        if state.current_winner == other_player:
            return {
                'position': None,
                'score': 1 * (state.num_empty_squares() + 1)
                if other_player == max_player else -1 * (state.num_empty_squares() + 1)
            }

        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -float('inf')}
        else:
            best = {'position': None, 'score': float('inf')}

        for possible_move in state.available_moves():
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player)

            # Undo move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move

            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best


def play(game, x_player, o_player, print_game=True):
    letter = 'X'
    if print_game:
        game.print_board_nums()
    
    while game.empty_squares():
        if letter == 'O':
            player = o_player
        else:
            player = x_player

        square = player.get_move(game)
        if game.make_move(square, letter):
            if print_game:
                print(f"{Fore.GREEN}{letter} makes move to position {square}{Style.RESET_ALL}")
                game.print_board()

            if game.current_winner:
                print(f"{Fore.YELLOW}{'='*40}")
                print(f"{Back.BLUE if letter=='X' else Back.RED}{Fore.WHITE} {letter} WINS! 🎉 {Style.RESET_ALL}")
                print(f"{Fore.YELLOW}{'='*40}")
                return letter

            letter = 'O' if letter == 'X' else 'X'

        if letter == 'O' and isinstance(o_player, ComputerPlayer):
            time.sleep(0.4)
    
    print(f"{Fore.MAGENTA}{'='*40}")
    print(f"{Fore.MAGENTA}   IT'S A TIE! 🤝")
    print(f"{Fore.MAGENTA}{'='*40}")


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{Fore.CYAN}{Style.BRIGHT}")
    print("╔════════════════════════════════════════╗")
    print("║                                        ║")
    print("║         TIC TAC TOE GAME               ║")
    print("║                                        ║")
    print("╚════════════════════════════════════════╝")
    print(f"{Style.RESET_ALL}")
    
    while True:
        print(f"\n{Fore.YELLOW}Choose game mode:{Style.RESET_ALL}")
        print(f"{Fore.GREEN}1.{Style.RESET_ALL} Player vs Player")
        print(f"{Fore.GREEN}2.{Style.RESET_ALL} Player vs Computer (Easy)")
        print(f"{Fore.GREEN}3.{Style.RESET_ALL} Player vs Computer (Impossible)")
        print(f"{Fore.RED}4.{Style.RESET_ALL} Quit")
        
        choice = input(f"\n{Fore.CYAN}Enter your choice (1-4): {Style.RESET_ALL}")
        
        if choice == '4':
            print(f"\n{Fore.YELLOW}Thanks for playing! Goodbye! 👋{Style.RESET_ALL}\n")
            break
        
        if choice in ['1', '2', '3']:
            t = TicTacToe()
            x_player = HumanPlayer('X')
            
            if choice == '1':
                o_player = HumanPlayer('O')
            elif choice == '2':
                # Easy AI: random moves
                o_player = Player('O')
                o_player.get_move = lambda game: random.choice(game.available_moves())
            else:
                # Impossible AI (Minimax)
                o_player = ComputerPlayer('O')
            
            play(t, x_player, o_player, print_game=True)
            
            play_again = input(f"{Fore.CYAN}Play again? (y/n): {Style.RESET_ALL}").lower()
            if play_again != 'y':
                print(f"\n{Fore.YELLOW}Thanks for playing! Goodbye! 👋{Style.RESET_ALL}\n")
                break
        else:
            print(f"{Fore.RED}Invalid choice. Please try again.{Style.RESET_ALL}")


if __name__ == '__main__':
    main()