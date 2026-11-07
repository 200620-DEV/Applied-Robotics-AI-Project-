"""Q-learning: a robot that learns to reach the goal by trial and error.

Unlike A* (project 01), the robot is not given a map. It tries moves,
gets rewards (+10 for the goal, -5 for a pit, -1 per step) and slowly
learns which move is best in each square.

Run:  python q_learning.py
"""
import random

random.seed(0)

GRID_SIZE = 5
OBSTACLES = {(1, 1), (2, 3), (3, 2)}
PITS = {(3, 1)}
START, GOAL = (0, 0), (4, 4)
ACTIONS = {"up": (0, -1), "down": (0, 1), "left": (-1, 0), "right": (1, 0)}

ALPHA = 0.1     # learning rate
GAMMA = 0.9     # how much future rewards matter
EPISODES = 2000


def step(state, action):
    dx, dy = ACTIONS[action]
    nx, ny = state[0] + dx, state[1] + dy
    if not (0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE) or (nx, ny) in OBSTACLES:
        return state, -1, False          # bumped: stay put
    nxt = (nx, ny)
    if nxt == GOAL:
        return nxt, 10, True
    if nxt in PITS:
        return nxt, -5, True
    return nxt, -1, False


def best_action(q, state):
    return max(ACTIONS, key=lambda a: q.get((state, a), 0.0))


def train():
    q = {}
    for episode in range(EPISODES):
        epsilon = max(0.05, 1.0 - episode / (EPISODES * 0.7))  # explore less over time
        state, done, moves = START, False, 0
        while not done and moves < 100:
            if random.random() < epsilon:
                action = random.choice(list(ACTIONS))
            else:
                action = best_action(q, state)
            nxt, reward, done = step(state, action)
            future = 0.0 if done else max(q.get((nxt, a), 0.0) for a in ACTIONS)
            old = q.get((state, action), 0.0)
            q[(state, action)] = old + ALPHA * (reward + GAMMA * future - old)
            state, moves = nxt, moves + 1
    return q


def show_policy(q):
    arrows = {"up": "^", "down": "v", "left": "<", "right": ">"}
    for y in range(GRID_SIZE):
        row = ""
        for x in range(GRID_SIZE):
            s = (x, y)
            if s == GOAL:
                row += "G "
            elif s in OBSTACLES:
                row += "# "
            elif s in PITS:
                row += "O "
            else:
                row += arrows[best_action(q, s)] + " "
        print(row)
    print()


if __name__ == "__main__":
    q = train()
    print("Learned policy (best move in each square, O = pit):")
    show_policy(q)
    state, path = START, [START]
    for _ in range(25):
        state, _, done = step(state, best_action(q, state))
        path.append(state)
        if done:
            break
    print("Greedy run:", " -> ".join(map(str, path)))
    print("Goal reached!" if state == GOAL else "Did not reach the goal.")
