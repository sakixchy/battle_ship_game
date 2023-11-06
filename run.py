import time # Thi was used for loading effect when initialising the board.
import random # This was used to generate random ships

def start_game (): # This starts the game
    def initialize_board(difficulty): # This sets the board 

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
          board_size = 8

        board = []
        for _ in range(board_size):
          row = ['_'] * board_size 
          board.append(row)

        return board, difficulty_name, num_ships, board_size

    def print_board_with_coordinates(board): # This places coordinates aligned with the board
        col_labels = " ".join(chr(i) for i in range(ord('A'), ord('A') + len(board[0])))
        print(f"               {col_labels}")

        for i, row in enumerate(board):
           print(f"{' ' * 11}{i + 1:2}  " + " ".join(row))

    
    def place_ships(board, num_ships): # This places random ships onto the board
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

    def parse_input(input_str, board_size): # This checks the player input and validates in a loop into row and colum coordinates on game board
     while True:
        if (
            len(input_str) < 2 
            or not input_str[0].isalpha() 
            or not input_str[1:].isdigit() 
            or not ('A' <= input_str[0].upper() <= chr(ord('A') + board_size - 1)) 
            or not (1 <= int(input_str[1:]) <= board_size)
        ):
            print("Invalid input. Please enter a letter followed by a number within the range of board.")
            input_str = input("Enter your guess: ")
        else:
            col = ord(input_str[0].upper()) - ord('A')
            row = int(input_str[1:]) - 1
            return row, col
    
    def check_guess(x, y, board):  # This checks if a guess matches a ship on the board
        if 0 <= x < len(board) and 0 <= y < len(board[0]):
            if board[x][y] == 'U':
               return True
            else:
               board[x][y] = 'X'
               return False
        else:
           return False
   
    def updated_board(board):
      print("               A B C D E F G H")
      for i, row in enumerate(board):
        print(f"{' ' * 11}{i + 1:2}  " + " ".join(row))



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
    player_name = input("Please, enter your name: ") # Player name is typed here
    print(f"Welcome {player_name}! \nPlease choose your difficulty level:\n"
            "Enter 'e' for easy, 'm' for medium, or 'h' for hard.\n")
    valid_difficluties = ['e', 'm', 'h']
    while True:
          game_difficulty = input("Your difficulty is: ") # Player difficulty is chosen here
          if game_difficulty in valid_difficluties:
              break
          else:
              print("Invalid input, please enter 'e' for easy, 'm' for medium  or 'h' for hard. ")


    print("Preparing the board...") # The board is being loaded here
    time.sleep(2)
    print("""
                    BATTLESHIPS
            """)
    board, game_difficulty, num_ships, board_size = initialize_board(game_difficulty)

    def player_interface():

         print(" " * 25)
         print("- " * 25)
         print(f"PLAYER: {player_name}                   Difficulty: {game_difficulty}")

    place_ships(board, num_ships)
    print_board_with_coordinates(board)
    player_interface()

    while True: # This loop allows player to keep guessing to either hit or miss a ship and give feedback
       guess_input = input("Enter your guess: ")
       guess_x, guess_y = parse_input(guess_input, board_size)
        
       if guess_x is not None and guess_y is not None:
          if check_guess(guess_x, guess_y, board):
             print(f'You hit a ship at ({chr(guess_y + ord("A"))}{guess_x + 1})!')
          else:
             print(f'You missed at ({chr(guess_y + ord("A"))}{guess_x + 1}).')

             updated_board(board)
          

start_game()
