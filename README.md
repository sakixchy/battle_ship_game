# Battleships Game
![an image of the initial terminal widnow](assets/images/battleships-mockup.png)
This is a Battleships game! You can play this game in the terminal, and it works like a charm! <br>
It was built using Python to showcase its capabilities with a gaming approach. <br>
The game allows users to interact within the terminal and provide appropriate feedback based on their actions. <br>
The game itself is simplified, requiring players to guess the opponent's ships. To add challenge,
there's a limit to the number of wrong guesses allowed before losing. <br>
Sink your opponent's ship and sail away for victory! [play now](https://battleships-game-ci-6a2a2f14ab3d.herokuapp.com/)
___

# User Experience (UX)
## User stories
- As a player, I am greeted with the home screen of the game.
- As a player, I can type in required text to begin the game.
- As a player, I can read through the instructions of the game.
- As a player, I can type in my name to personalize my gaming experience.
- As a player, I can easily choose between different levels of difficulty.
- As a player, I can easily recognize and understamd the various aspects of the game.
- As a player, I can utilize vaious input methods to determine an outcome.
- As a player, I am given a game over or congratulatory message upon conditions being met.
___

# Game Logic Flowchart 
![an image of flowchart for game logic](assets/images/battle-ships-flowchart.png) 
The game development process was optimized using this flowchart, providing a strong foundation for the Battleships game logic.
___

# Features
## ASCII Images
![an image of ascii art](assets/images/ascii-art.png) <br>
These are ASCII art to give the start menu some visual flare. <br>
The title of the game and thr battleship art is written in ASCII format, therefore meeting the theme of this project.

## Game Interaction
![an image of play input field](assets/images/play-input.png) <br>
The user has to type in 'play' to enter into game state, <br>
otherwise the user can't start the game. This makes the the start menu less cluttered, <br>
while providing a seamless transition to game enviroment from start menu. <br>
The keyword 'play' can be typed in lowercase or uppercase, anything else will trigger an invalid input.

![an image of game instructions](assets/images/game-instructions.jpeg)<br>
The users are greeted with the game instructions displayed in the initila text box. <br>
This section serves as an introduction to the game, informing the users of objectives, rules and outcome.

![an image of name input field](assets/images/name-input.jpeg) <br>
Below the instructions section is the player name input field. The user may enter their name as they please,
but can't leave it empty or else a validation erorr triggers, asking users to enter a name.<br>

![an image of difficulty level](assets/images/difficulty-level.jpeg) <br>
After inputting their name, the user is greeted by their provided name. At this point, the user has the <br>
option to select their preferred difficulty level for gameplay. <br>
- 'e' for easy
- 'm' for medium
- 'h' for hard   <br>

Any other input will cause a validation error and requesting user to type again.

![an image of game interface](assets/images/game-interface.jpeg) <br>
This interface provides all the key elements essential for a intuitive battleships gaming experience. <br>
These include: 
- Game board : Visual representation of the battlefield where the player can track of hits or misses on ships.
- Coordinates label : Indicates the accurate coordinates for the players to make guesses.
- Wrong guesses counter : Decreases by 1 with each incorrect guesses until it reaches 0, then the game ends.
- Difficulty level: Reminds player of the chosen level.
- Player input field for guessing ships: Allows players to enter coordinates within the board's range.

![an image of ship being missed displayed](assets/images/ship-miss.jpeg) <br>
The player will be informed with a messsage on a ship being missed with the appropriate coordinates. <br>

![an image of ship being hit displayed](assets/images/ship-hit.jpeg) <br>
The player will be informed with a messsage on a ship being hit with the appropriate coordinates. <br>

![an image of ship being sunk displayed](assets/images/ship-sunk.jpeg) <br>
The player will be informed with a messsage on a ship being sunk. <br>

![an image of game winning's state](assets/images/game-won.jpeg) <br>
The player will be congratulated after sinking all the ships. This message marks the end of the game.

![an image of game in a losing state](assets/images/game-lost.jpeg) <br>
The player will be informed of losing the game, and given options to start over or exit out of the game. <br>

___

# Testing 
## Manual Testing
| Browser Testing | Supported |
|-----------------|-----------|
| Chrome          | &check;   |
| Firefox         | &check;   |
| Safari          | It doesn't contain the necessary js. script to run the app. |


### Validator Testing
![an image of pep8 validator](assets/images/pep-eight-validator.jpeg) <br>
There were some errors regarding whitespaces & length of code being over 79 characters long, <br>
fortunetely they have all been resolved.

### Gameplay
| Scenario | Action | Expected Outcome | Actual Outcome |
|----------|--------|------------------|----------------|
| Initialize of the game | Player types in the keyword 'play'| The game content is being displayed | True |
| Player Registration | Player enters their name | Welcome message with the player's name is displayed | True |
| Selecting Game Difficulty | Player enters a specific letter | The board initializes with a specific layout corresponding to the chosen difficulty | True |
| Guessing the ships | Player enters a set of coordinates | The board updates with the mark of 'U' if the coordinates correspond to a ship, otherwise 'X' as miss. | True |
| Reguessing the coordinates | Player enters the same coordinates multiple times | An invalid message triggers | True |
| Entering Far-Reaching coordinates | Player enters coordinates outside the game board | An invalid message triggers | True |
| Entering Invalid coordinates | Player enters just anything not related to game | An invalid message triggers | True |
| Ship sinks after 3rd hit | Player hits all three parts of the ship | Ship sunk message triggers | True |
| Game loss | Player uses all remaining wrong guesses | The game ends and displays a 'Game Over' message with options to start over or exit | True |
| Game win | Player successfully sinks all ships | The game ends with a congratulatory message and starts over the game | True |

## Bug
![an image of bug being  encountered](assets/images/bug-found.jpeg) <br>
While testing the game, i came across this bug. After successfully sinking all the ships, the game  still displays the board and allows further player input. I solved this issue by calling out `start_game` function to if statement.

# Deployment
This repository contains a Battleship game developed using Python. <br>
Follow these steps to deploy the game to Heroku.

1. Create an account on Heroku if you haven't already otherwise log into your account.
2. After logging in, you will be dierected to Heroku dashboard.
3. In the dashboard, locate the navigation menu on the top right corner. <br>
It looks like a "nine-dot" button.
4. Click on the "nine-dot" button to reveal a dropdown menu.
5. Click on the first button called "Dashboard".
6. Locate and click the "New" button to reveal the dropdown menu.
7. From the dropdown menu, click on "Create new app".
8. Give a unique name for your app and ensure it hasn't been used before.
9. Choose a region for your app based on your location.
10. Finally, click on "Create app". <br>
You have successfully created the app required for your deployment.
11. Now go to Settings from your app in the dashboard.
12. Scroll down untill "Config Vars" section appears, click on "reveal Config Vars".
13. Assign the key "PORT" with the value "8000" next to it.
14. Click on Add to save changes.
15. Scroll a bit further down until "Buildpacks" section appears.
16. Click on "Add Buildpack".
17. In the modal that appears subsequently, add the following buildpacks in these order:
   - Click "Python" to add the Python buildpack.
   - Click "Nodejs" to add the Nodejs buildpack.
18. Go to Deploy menu in frpm the dashboard
19. Scroll down to Deployment method section.
20. Click "Github" to connect the game with battleships repository with Heroku.
21. Once the repository is connected, you can choose to manually deploy from a branch <br> 
or enable automatic deployments from a specific branch. <br>
You have now successfully deployed the battleships game to Heroku.

# Technologies Used
- **Python** to develop the game.
- **Gitpod** to setup the coding enviroment
- **Github** for repository hosting.
- **Heroku** for deploying the game.
- **Lucidchart** for making the flowchart.
- **Pip Black** for formatting the code to meet pep8 sstandards.