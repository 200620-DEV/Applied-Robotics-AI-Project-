# Robotics and AI practice projects

Six small, self-contained projects covering core topics of a robotics and
AI degree. Each one is a single Python file that uses only the standard
library, so there is nothing to install. They are separate from the module
work in `main.py`.

| # | Project | Topic | What it shows |
|---|---------|-------|---------------|
| 01 | [A* path planning](01_astar_path_planning/astar.py) | Search / planning | The robot finds the shortest path to the goal around obstacles and turns it into up/down/left/right commands |
| 02 | [PID controller](02_pid_controller/pid.py) | Control systems | Driving a motor to a target speed; tune KP, KI and KD and watch the response |
| 03 | [Kalman filter](03_kalman_filter/kalman.py) | State estimation | Combining noisy sensor readings with motion to track position more accurately |
| 04 | [Robot arm kinematics](04_robot_arm_kinematics/arm.py) | Kinematics | Forward and inverse kinematics of a 2-link arm |
| 05 | [Q-learning](05_q_learning/q_learning.py) | Reinforcement learning | The robot learns a route to the goal by trial and error, with no map |
| 06 | [Neural network](06_neural_network/neural_net.py) | Machine learning | A network built from scratch learns a bump-sensor rule (XOR) using backpropagation |

## How to run

From inside a project folder:

    python astar.py

## Ideas for extending them

- 01: allow diagonal moves, or compare A* with breadth-first search and count the cells each one explores
- 02: add a disturbance (such as a hill) halfway through and see how the I term handles it
- 03: extend to 2D (x, y) using matrices, or replace it with a particle filter
- 04: add a third joint, or animate the arm with matplotlib
- 05: compare Q-learning with SARSA, or make the pits move
- 06: train on real sensor data, or rewrite it with NumPy and compare speed

## Note on academic integrity

These are learning and revision examples. If you use ideas from them in
assessed work, follow your university's rules on referencing and
acknowledging AI-assisted code.
