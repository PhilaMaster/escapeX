# Escape X - Game Overview

Escape X is a game where the objective is to complete X (10) levels.

Each level challenges the player to reach the exit point before time runs out while avoiding walls and dangerous enemies.

## Level Design & Structure

The levels are generated using character matrices (implemented as lists of strings), such as the following example:
<pre>
livello = [  # 2
    "WWWWWWWWWWWWWWWWWW",
    "W    EE         EW",
    "W   EE       E  2W",
    "WWWWWWWWPPWWWWWWWW",
    "W 1              W",
    "W       KK       W",
    "W           1    W",
    "WH      WW      HW",
    "W  1             W",
    "W               1W",
    "WWWWWWWWWWWWWWWWWW",
    "                  ",
]
</pre>

(This represents Level 2 in the game—progress past the first level to see how it corresponds.)

Each character in the matrix has a specific role, defined in the legend below:

### Legend

- W = Wall (Obstacle)

- E = Exit (Level completion point)

- K = Key (Unlocks doors)

- I = Invisible Wall (Hidden obstacle)

- P = Door (Can be unlocked with a key)

- H = Horizontal Enemy (Moves side-to-side)

- V = Vertical Enemy (Moves up and down)

- 1 = Star Level 1 (+50 points)

- 2 = Star Level 2 (+500 points)

## Gameplay & Scoring System

### Controls

Players can navigate using the WASD keys.

### Scoring

Points are awarded as follows:

- Unlocking a door: +25 points

- Collecting a Level 1 star: +50 points

- Collecting a Level 2 star: +500 points

- Remaining time at the end of a level: +25 points per second

- Death penalty: -100 points (All points collected during the current level will be lost upon death.)

### Objective

The goal of Escape X is to complete all levels with the highest possible score—which means playing efficiently and minimizing time spent on each level.

## Technologies Used

Escape X is developed using Python and the Pygame library for handling graphics, animations, and game logic. The game features:

- Pygame for rendering: Handles sprites, animations, and collisions.

- Object-Oriented Programming (OOP): Implements classes for game entities like walls, keys, enemies, and the player.

- Event-driven mechanics: Uses keyboard input for movement and interaction.

- Sound and visual effects: Includes music, sound effects, and sprite animations for an engaging experience.

## How to Run the Game

Install Python (if not already installed):
```
sudo apt install python3  # Linux
brew install python  # macOS
winget install Python.Python.3  # Windows
```
Install Pygame:
```
pip install pygame
```
Run the game script:
```
python Escape_X.py
```
