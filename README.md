# Grid Robot Simulator

A simple Python simulation of a robot moving around a 5x5 grid. The robot
follows a list of movement commands (up, down, left, right) and stops
when it would hit a wall or an obstacle.

## Features

- Robot class that tracks its position on the grid
- Text display of the grid after every move
- Wall detection (the robot can't leave the grid)
- Obstacle detection (the robot can't move into blocked squares)

## How to run

Make sure Python 3 is installed, then run:

    python main.py

## Grid key

| Symbol | Meaning        |
|--------|----------------|
| R      | Robot          |
| #      | Obstacle       |
| .      | Empty square   |

## Project status

Work in progress, built step by step as part of the Applied Robotics and AI
Project module at the University of Hertfordshire.

## Author

PUROHIT DEV PRAMOD
   - Goal square (G): the program prints "Goal reached!" when the robot gets there
   
## Branching strategy
- main: stable, tested code only
- Dev: development branch, new work is committed here first
- Changes reach main through a pull request from Dev
- Each change matches a Trello card and has a short commit message