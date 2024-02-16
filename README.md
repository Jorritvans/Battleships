# Battleships
Battleships is a classic two-player guessing game where opponents attempt to sink each other's fleet of ships.

![Am I Responsive Python](https://github.com/Jorritvans/Battleships/assets/146831899/641733b7-2143-4631-bfe7-6fb26942cff7)

### Portfolio Project 3 - Python Essentials
The purpose of this project was to build an interactive logic game for a user to play against the computer.

## Link to app

https://battleships-jorrit-1d65dbc636eb.herokuapp.com/ or press [link](https://battleships-jorrit-1d65dbc636eb.herokuapp.com/)

## How to Play

In Battleships, players take turns guessing the coordinates of their opponent's ships on a grid. The first player to sink all of their opponent's ships wins the game.

- __How to Play:__

- Each player places their ships on the grid without overlapping.
  
- Players take turns guessing coordinates to attack their opponent's ships.
  
- If a guess hits a ship, it's marked as a hit. Otherwise, it's a miss.
  
- The game continues until one player sinks all of their opponent's ships.

## Features
- __Ask players name__ : The game will ask for the player's name.

![player name](https://github.com/Jorritvans/Battleships/assets/146831899/252ac190-31b6-4f7d-977a-059746c8fd76)

- __Ask board size__ : Game will ask for a board size ranging from 4-8.
- __Game Initialization__ : Creates a game board and places ships randomly.

![board size](https://github.com/Jorritvans/Battleships/assets/146831899/b6179462-9593-4aa5-bd40-f9875f7335bb)

- __Player and Computer Turns__ : Allows players to guess coordinates on the opponent's board.

![first guess](https://github.com/Jorritvans/Battleships/assets/146831899/055e5854-7aae-4b9b-a972-3ae37a0be027)

- __Winning Conditions__ : Determines the winner based on the first player to sink all ships.
- __Game over__ : Displays the winner or a draw and allows players to play again or exit.

![play again yes or no](https://github.com/Jorritvans/Battleships/assets/146831899/53791ccf-b84e-44e0-af18-cd5204b5f4f3)

- __Computer's Strategy__ : Generates random guesses for the player's board.

![random guess computer](https://github.com/Jorritvans/Battleships/assets/146831899/b6825282-f96d-4151-b7bb-44b0c3cc65b1)

- __Error Handling__ : Handles errors for invalid inputs or out-of-bounds guesses.

![error handling](https://github.com/Jorritvans/Battleships/assets/146831899/efdfe534-aee8-4f88-b80d-44c5ac1b46ea)

- __Code Organization__ : Structured into modular functions for different game aspects.

- __Future Features__
- Get players to choose where to place their ships.
- Add a scoreboard.

## Technologies Used

- __Programming Languages:__
- Python
- __CodeAnywhere__
- CodeAnywhere was used for version control by utilizing the Codeanywhere terminal to commit and Push to GitHub.
- __Git__
- Git was used for version control by utilizing the GitPod terminal to commit to Git and Push to GitHub.
- __Github__
- GitHub is used to store the projects code after being pushed from Git.
- __VSCode__
- VSCode was used for version control by utilizing the VSCode terminal to commit and Push to GitHub.
- __Colorama__
- To get a colored output in some text.

## Development 

- I wanted the battleships to be placed randomly on the game board, so for that functionality I imported the random library.

## Data Model

- __The data model consists of:__

- Game board: Represented as a 2D grid where ships are placed.
- Ships: Varying sizes and symbols placed on the board.

## Testing 
-__I have manually tested this project by doing the following:__

- Passed the code through a PEP8 linter and confirmed there are no problems or errors.

- Given invalid inputs to check the error handling

- Tested it in my local terminal and the deployed version on Heroku.

## Bugs
- __No known bugs.__

- __PEP8__
- No errors returned from the PEP8 checker.

![no errors found](https://github.com/Jorritvans/Battleships/assets/146831899/d3745cd3-fd03-4da0-b15d-a1fc60402e0c)

## Deployment
This project was deployed using the Code Institute's mock terminal for Heroku.

- __Steps for deployment:__
- fork or clone this repository
- Create a new Heroku app
- Set the buildpacks to Python and NodeJS in the same order as i mentioned
- Link the Heroku app to the repository
- Click on DEPLOY

## Credits 
- __This project was developed by entirely by me.__
- Special thanks to the developers of Colorama for enhancing the user experience with colored output.
- Got my ideas from Stack Overflow: https://stackoverflow.com/questions/17952870/simple-python-battleship-game
- Not a single line of code has been copied within my knowledge.
- Code Institute for the deployment terminal.


## Advice and experience 
Have had a lot of issues with CodeAnywhere where the workspace would not open resulting in less commit messages as i would have wanted myself as i had to work on VSCode locally
until i contacted the tutor support so i could find out how to use GitPod, so i had to copy a lot of code from VSCode to GitPod and might have lost a few important commits because of that...
this is something i wanted to clarify as none of the code was taken from an external source what i know of, only took information from Stack Overflow.
![CODEANYWHERE SLOW](https://github.com/Jorritvans/Battleships/assets/146831899/442323b9-15a9-412d-a8d4-f0e9078aca70)

## Acknowledgements
A special thanks to my mentor for the advice on improving my game.
