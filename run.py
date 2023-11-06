import time
import random

def start_game ():
    def initialize_board(difficulty):

        board_size = 8

        if difficulty == 'e':
           difficulty_name = 'easy'
           board_size = 6
           num_ships = 2
        elif difficulty == 'h':
             difficulty_name = 'hard'
             board_size = 10
             num_ships = 4
        else:
             difficulty_name = 'medium'
             num_ships = 3

        board = []
        for _ in range(board_size):
            row = ['_'] * 8
            board.append(row)
        return board, difficulty_name, num_ships

    def print_board_with_coordinates(board):
        print("               A B C D E F G H")

        for i, row in enumerate(board):
            print(f"{' ' * 11}{i + 1:2}  " + " ".join(row))
    
    def place_ships(board, num_ships):
        for _ in range(num_ships):
            while True:
                  x = random.randint(0, len(board) - 1)
                  y = random.randint(0, len(board[0]) - 1)
                  direction = random.choice(['horizontal', 'vertical'])

                  if direction == 'horizontal':
                     if y <= len(board[0]) - 3 and all(board[x][y+i] == '_' for i in range(3)):
                        for i in range(3):
                            board[x][y+i] = 'U'
                        break
                  elif direction == 'vertical':
                     if x <= len(board) - 3 and all(board[x+i][y] == '_' for i in range(3)):
                        for i in range(3):
                            board[x+i][y] = 'U'
                        break

    def parse_input(input_str):
        while True:
           if (
            len(input_str) != 2 
            or not input_str[0].isalpha() 
            or not input_str[1].isdigit() 
            or not ('A' <= input_str[0].upper() <= 'H') 
            or not (1 <= int(input_str[1]) <= 6)
            ):
              print("Invalid input. Please enter a letter followed by a number within the range of board.")
              input_str = input("Enter your guess: ")
           else:
              col = ord(input_str[0].upper()) - ord('A')
              row = int(input_str[1]) - 1
              return row, col
    
    def check_guess(x, y, board):
        if 0 <= x < len(board) and 0 <= y < len(board[0]):
            if board[x][y] == 'U':
               return True
            else:
               return False
        else:
           return False
        

    print(place_ships)

    battleships_logo = """
            ___    ___  ______ ______   __    ____   ____   __ __   ____   ___    ____
            / _ )  / _ |/_  __//_  __/  / /   / __/  / __/  / // /  /  _/  / _ \\  / __/
           / _  | / __ | / /    / /    / /__ / _/   _\\ \\   / _  /  _/ /   / ___/ _\\ \\  
          /____/ /_/ |_|/_/    /_/    /____//___/  /___/  /_//_/  /___/  /_/    /___/  

         """
    print(battleships_logo)   
    game_instructions = """
                                     INSTRUCTIONS
          There will be randomly generated ships on the board, the number of ships
          as well as the board size will grow bigger depending on your  difficulty 
          level. You as the player will be given turns to sink the opponent's ship
          in an ultimate battle! You will have to guess where the opponent's ships
          are located on the board by entering the correct coordinates  to  either
          hit or be missed of hitting.The opponent gets to make their move and the
          same process repeats,until a player sinks all of their opponent's ships.
          The winner of the Battleships game is declared at the end.

         """     
    print(game_instructions)                                      
    player_name = input("Please, enter your name: ")
    print(f"Welcome {player_name}! \nPlease choose your difficulty level:\n"
            "Enter 'e' for easy, 'm' for medium, or 'h' for hard.\n")
    valid_difficluties = ['e', 'm', 'h']
    while True:
          game_difficulty = input("Your difficulty is: ")
          if game_difficulty in valid_difficluties:
              break
          else:
              print("Invalid input, please enter 'e' for easy, 'm' for medium  or 'h' for hard. ")


    print("Preparing the board...")
    time.sleep(2)
    print("""
                    BATTLESHIPS
            """)
    board, game_difficulty, num_ships = initialize_board(game_difficulty)

    place_ships(board, num_ships)
    print_board_with_coordinates(board)
    print(" " * 25)
    print("- " * 25)
    print(f"PLAYER: {player_name}                   Difficulty: {game_difficulty}")

    while True:
       guess_input = input("Enter your guess: ")
       guess_x, guess_y = parse_input(guess_input)
        
       if guess_x is not None and guess_y is not None:
          if check_guess(guess_x, guess_y, board):
               print(f'You hit a ship at ({guess_input})!')
          else:
               print(f'You missed at ({guess_input}).')
        

start_game()
