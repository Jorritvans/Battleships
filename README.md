# Battleships
Battleships is a classic two-player guessing game where opponents attempt to sink each other's fleet of ships.

### Portfolio Project 3 - Python Essemtials
The purpose of this project was to build an interactive logic game for a user to play against the computer.

## Link to app

## How to Play

In Battleships, players take turns guessing the coordinates of their opponent's ships on a grid. The first player to sink all of their opponent's ships wins the game.

- __How to play:__

- Each player places their ships on the grid without overlapping.
- Players take turns guessing coordinates to attack their opponent's ships.
- If a guess hits a ship, it's marked as a hit. Otherwise, it's a miss.
- The game continues until one player sinks all of their opponent's ships.

## Features

- __Game Initialization__ : Creates a game board and places ships randomly.
- __Player and Computer Turns__ : Allows players to guess coordinates on the opponent's board.
- __Winning Conditions__ : Determines the winner based on the first player to sink all ships.
- __Computer's Strategy__ : Generates random guesses for the player's board.
- __Game over__ : Displays the winner or a draw and allows players to play again or exit.
- __Error Handling__ : Handles errors for invalid inputs or out-of-bounds guesses.
- __Code Organization__ : Structured into modular functions for different game aspects.

## Technologies Used

- __Programming Languages:__
- Python
- __Codeanywhere__
- Codeanywhere was used for version control by utilizing the Codeanywhere terminal to commit and Push to GitHub.
- __Git__
- Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
- __Github__
- GitHub is used to store the projects code after being pushed from Git.
- __VSCode__
- VSCode was used for version control by utilizing the VSCode terminal to commit and Push to GitHub.
- __Colorama__
- To get a colored output in some text.

## Development 

-I wanted the battleship to be placed randomly on the game board, so for that functionality I imported the random library.

## Data Model

- __The data model consists of:__

- Game board: Represented as a 2D grid where ships are placed.
- Ships: Varying sizes and symbols placed on the board.

## Testing 
-__I have manually tested this project by doing the following:__

- Passed the code through a PEP8 linter and confirmed there are no problems or errors.

- Given invalid imputs to check the error handling

- Tested it in my local terminal and the deployed version on Heroku.

## Bugs
- __No known bugs.__

- __PEP8__
- No errors returned from the PEP8 checker.

## Deployment
This project was deployed using the Code Institute's mock terminal for Heroku.

- __Steps for deployment:__
- fork or clone this repository
- Create a new Heroku app
- Set the buildpacks to Python and NodeJS in the same order as i mentioned
- Link the Heroku app to the repository
- Click on DEPLOY

## Credits 
- __This project was developed by me.__
- Special thanks to the developers of Colorama for enhancing the user experience with colored output.
- Got my ideas from stackoverflow: https://stackoverflow.com/questions/17952870/simple-python-battleship-game
- Not a single line of code has been copied within my knowledge.
- Code institute for the deployment terminal.
## Advice and experience 

## Acknowledgements
