# Tic Tac Toe Game

For this challenge, you will write a tic tac toe game. The board will be 3x3. There will be instructions to guide the user through.

### 1. Basics
First, think of a data structure to represent the board. For example, we can use a 2d array. Initialize each value with 0 (which could mean no inputs yet). Let's say 1 means player 1 placed there and 2 for player 2. Then at first the array would look like `[[0,1,1], [0,2,2], [0, 0, 0]]`.

Let's say `x` is for player 1 and `o` means player 2. The board would look like:

```
| |x|x|
| |o|o|
| | | |
```

You first step would be to write a function to print the board given the array.

### 2. Game Setup

Use a `while True:`, have a `input()` to take user input in the while loop. Let's say we take inputs from 1-9 representing the 9 positions on the board. If the position is taken, you print and say invalid input.


### 3. How to clear the board?

You could keep printing new board, but I think it's better if we clear all the prints and print a new board.

```
import os

os.system("clear")
```

### 4. Putting everything together

1-3 are just some free tips. Feel free to design the game in any way you want. The end result should be a playable tic tac toe game.
