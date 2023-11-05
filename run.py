import time

def start_game ():
    def initialize_board(difficulty):

        board_size = 8

        if difficulty == 'e':
           difficulty_name = 'easy'
           board_size = 6
        elif difficulty == 'h':
             difficulty_name = 'hard'
             board_size = 10
        else:
             difficulty_name = 'medium'

        board = []
        for _ in range(board_size):
            row = ['_'] * 8
            board.append(row)
        return board, difficulty_name

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
    board, game_difficulty = initialize_board(game_difficulty)
 
    for row in board:
        print("              " + " ".join(row))
    print(" " * 25)
    print("- " * 25)
    print(f"PLAYER: {player_name}                   Difficulty: {game_difficulty}")


start_game()
