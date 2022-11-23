# Bataille navale

This is an implementation of the [Battleship](https://en.wikipedia.org/wiki/Battleship_(game)) game in python with a graphical interface.


## Table of Contents
  - [Code execution](#code-execution)
  - [Creating the game grid](#creating-the-game-grid)
  - [Creation of boats](#creation-of-boats)
  - [Leaderboard](#leaderboard)

## Code execution

To launch the game, you have to launch the program `battelship.py`. When the program is launched, a window appears asking you for your identity. This will be used to store your result in the game (number of moves played and time played). Then, a window with blue gride appears. You can click on a square to shoot it. If the square turns white, there are no ships on it. If it turns yellow, you have hit a ship. If it turns red, you have sunk a ship. The goal of the game is to sink all the boats in a minimum number of moves. At the end of your game, you will see your score under the grid.

You can find your results by running the program `leaderboards.py`. This program will show you the top 5 players (ranked by number of moves and time).

## Creating the game grid
By default the grid size is set to 10 but you can change it, by changing the parameter n in the program `battelship.py`.

## Creation of boats
The creation of the boats is done in 2 steps: the determination of the number of boats and the determination of the lengths of each boat. These two parameters cannot be fixed because we can change n, the length of the grid. We choose the number of boats being equal to $n/2$. The length of the boats is chosen according to a Gaussian law of mean of $\sqrt n$ and standard deviation of $1.5$. To avoid the case where the length of a boat is too big or too small, we define a min size of $n/5$ and a max size of $n$.

## Leaderboard
You can display the scores of any game played by running the program `leaderboard.py`. This program will display the 5 best scores on the number of moves and on the time on each size of grids played.
