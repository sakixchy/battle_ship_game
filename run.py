import time # This was used for loading effect when initialising the board.
import random # This was used to generate random ships

def initialize_board(difficulty): # This sets the board 
      
        board_size = 8
        ships = []

        if difficulty == 'e':
           difficulty_name = 'easy'
           board_size = 6
           num_ships = 4
        elif difficulty == 'h':
           difficulty_name = 'hard'
           board_size = 10
           num_ships = 4
        else:
          difficulty_name = 'medium'
          num_ships = 4
          board_size = 8

        board = []
        for _ in range(board_size):
          row = ['_'] * board_size 
          board.append(row)

        return board, difficulty_name, num_ships, board_size, ships 

def print_board_with_coordinates(board): # This places coordinates aligned with the board
        col_labels = " ".join(chr(i) for i in range(ord('A'), ord('A') + len(board[0])))
        print(f"               {col_labels}")

        for i, row in enumerate(board):
          modified_row = ['_' if cell == 'S' else cell for cell in row]
          print(f"{' ' * 11}{i + 1:2}  " + " ".join(modified_row))

def place_ships(board, num_ships, ships): # This places random ships onto the board
      for _ in range(num_ships):
          while True:
                  x = random.randint(0, len(board) - 1)
                  y = random.randint(0, len(board[0]) - 1)
                  direction = random.choice(['horizontal', 'vertical'])

                  if direction == 'horizontal':
                     if y <= len(board[0]) - 3 and all(board[x][y+i] == '_' for i in range(3)) and all((x, y+i) not in ship['positions'] for ship in ships):
                        for i in range(3):
                            board[x][y+i] = 'S'
                            ships.append({'positions': [(x, y+i) for i in range(3)], 'hits': 0})
                        break
                  elif direction == 'vertical':
                       if x <= len(board) - 3 and all(board[x+i][y] == '_' for i in range(3)) and all((x+i, y) not in ship['positions'] for ship in ships):
                        for i in range(3):
                            board[x+i][y] = 'S'
                            ships.append({'positions': [(x+i, y) for i in range(3)], 'hits': 0})
                        break

def parse_input(input_str, board_size): # This checks the player input and validates in a loop into row and colum coordinates on game board
     while True:
        if (
            len(input_str) < 2 
            or not input_str[0].isalpha() 
            or not input_str[1:].isdigit() 
            or not ('A' <= input_str[0].upper() <= chr(ord('A') + board_size - 1)) and not ('a' <= input_str[0].lower() <= chr(ord('a') + board_size - 1))
            or not (1 <= int(input_str[1:]) <= board_size)
        ):
            print("Invalid input. Please enter a letter followed by a number within the range of board.")
            input_str = input("Enter your guess: ")
        else:
            col = ord(input_str[0].upper()) - ord('A')
            row = int(input_str[1:]) - 1
            return row, col
    
def check_guess(x, y, board, ships):  # This checks if a guess matches a ship on the board
        if 0 <= x < len(board) and 0 <= y < len(board[0]):
          if board[x][y] == 'S':
            for ship in ships:
                if (x, y) in ship['positions'] and board[x][y] == 'S':
                    board[x][y] = 'U'
                    ship['hits'] += 1
                    if ship['hits'] == len(ship['positions']):
                        print("You sunk a ship!")
                        return True
                    else:
                        return True
          elif board[x][y] == '_':
            board[x][y] = 'X'
            return False
        return False

def check_if_ship_sunk(ship, board): # This checks if a ship has sunk
     return all(board[x][y] == 'U' for x, y in ship['positions'])
    
def check_if_all_ships_sunk(ships, board): # This check if all ships have sunk
     return all(check_if_ship_sunk(ship, board) for ship in ships)

def updated_board(board, board_size): # This iterates a new board after each guess
      print("""
      """)
      col_labels = " ".join(chr(i) for i in range(ord('A'), ord('A') + board_size))
      print(f"               {col_labels} ")
      for i, row in enumerate(board):
        print(f"{' ' * 11}{i + 1:2}  " + " ".join('_' if cell == 'S' else cell for cell in row))

def player_interface(player_name, game_difficulty, guesses_left): # This shows the player info

    print(" " * 25)
    print("- " * 30)
    print(f"PLAYER: {player_name}  Wrong Guesses left:{guesses_left}  Difficulty: {game_difficulty}")

def start_game (): # This starts the game

    guesses_left = 10 # A miss or wrong guess will decrement by 1 
    guessed_coordinates = [] # This keeps track of already entered coordinates.
    
    battleships_logo = """
             ____        _   _   _           _     _           
            | __ )  __ _| |_| |_| | ___  ___| |__ (_)_ __  ___ 
            |  _ \\ / _` | __| __| |/ _ \\/ __| '_ \\| | '_ \\/ __|
            | |_) | (_| | |_| |_| |  __/\\__ \\ | | | | |_) \\__ \\
            |____/ \\__,_|\\__|\\__|_|\\___||___/_| |_|_| .__/|___/
                                                    |_|               
    """
    print(battleships_logo) # This displays Battleships game logo
    battleship_ascii = """
                                        __/___            
                            _____/______|           
                    _______/_____\\_______\\_____     
                    \\              < < <       |    
                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """
    print(battleship_ascii)
    game_instructions = """
                             INSTRUCTIONS
    There will be randomly generated ships on the board, the number of ships
    as well as the board size will grow bigger depending on your  difficulty 
    level. You as the player will be given turns to sink the opponent's ship
    in an ultimate battle! You will have to guess where the opponent's ships
    are located on the board by entering the correct coordinates  to  either
    hit or be missed of hitting. After failing to sink all the ships  within
    the given guesses, you will lose!  So try to hit and sink all the ships!

         """     
    print(game_instructions) # This displays the game instructions     
    while True:                            
          player_name = input("Please, enter your name: ") # Player name is typed here
          if player_name:
             break
          else:
            print("You must enter a name.")
    print(f"Welcome {player_name}! \nPlease choose your difficulty level:\n"
            "Enter 'e' for easy, 'm' for medium, or 'h' for hard.\n")
    valid_difficulties = ['e', 'm', 'h']
    while True:
          game_difficulty = input("Your difficulty is: ") # Player difficulty is chosen here
          if game_difficulty in valid_difficulties:
              break
          else:
              print("Invalid input, please enter 'e' for easy, 'm' for medium  or 'h' for hard. ")


    print("Preparing the board...") # The board is being loaded here
    time.sleep(2)
    print("""

    """)

    board, game_difficulty, num_ships, board_size, ships = initialize_board(game_difficulty)

    place_ships(board, num_ships, ships)
    print_board_with_coordinates(board)
    player_interface(player_name, game_difficulty, guesses_left)

    while True: # This loop allows player to keep guessing to either hit or miss a ship and give feedback
       
         guess_input = input("Enter your guess: ")
         guess_x, guess_y = parse_input(guess_input, board_size)

         if (guess_x, guess_y) in guessed_coordinates:
            print("You have already guessed these coordinates. Please enter new ones.")
            continue

         guessed_coordinates.append((guess_x, guess_y))
        
         if guess_x is not None and guess_y is not None:
              if check_guess(guess_x, guess_y, board, ships):
                if not check_if_ship_sunk([ship for ship in ships if (guess_x, guess_y) in ship['positions']][0], board):
                    print(f'You hit a ship at ({chr(guess_y + ord("A"))}{guess_x + 1})!')
                else:
                    if check_if_all_ships_sunk(ships, board):
                       print("Congratulations! You sank all the ships. You won!")
                       return
              else:
                 guesses_left -= 1
                 print(f'You missed at ({chr(guess_y + ord("A"))}{guess_x + 1}).')
           
              if guesses_left == 0:
                 print("You ran out of guesses. Game Over! You lost. ")
                 play_again = input("Do you want to play again? (yes/no): ")
                 if play_again.lower() == "yes":
                    start_game()
                 else:
                     print(f"Thank you {player_name} for playing the Battleships game! ")
                     return
              updated_board(board, board_size)
              player_interface(player_name, game_difficulty, guesses_left)


start_game()
