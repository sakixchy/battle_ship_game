def start_game ():
    battleships_logo = """
            ___  ___ ______________   __________ _________  ____  
            / _ )/ _ /_  __/_  __/ /  / __/ __/ // /  _/ _ \/ __/  
           / _  / __ |/ /   / / / /__/ _/_\ \/ _  // // ___/\ \    
          /____/_/ |_/_/   /_/ /____/___/___/_//_/___/_/  /___/    
                                                                                                           
     """
    print(battleships_logo)   
    game_instructions = """
                                     INSTRUCTIONS
          There will be randomly generated ships on the board, the number of ships
          as well as the board size will grow bigger depending on your difficulity level.
          You as the player will be given turns to sink the opponent's ship in an ultimate battle!
          You will have to guess where the opponent's ships are located on the board by
          entering the correct coordinates to either hit or be missed of hitting.
          The opponent gets to make their move and the same process repeats, until
          one player sinks all of their opponent's ships.\n
          The winner of the Battleships game is declared at the end.

    """     
    print(game_instructions)                                      
    player_name = input(str("Please, enter your name: "))
    print(f"                 Welcome {player_name}! \nPlease choose your difficulity level:\n"
    "Enter 'e' for easy, 'm' for medium, or 'h' for hard.\n")


start_game()