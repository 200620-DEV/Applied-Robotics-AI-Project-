GRID_SIZE = 5

class Robot:
    def __init__(self):
        self.x = 0
        self.y = 0

    def move(self, direction):
        dx, dy = {"up": (0, -1), "down": (0, 1),
                  "left": (-1, 0), "right": (1, 0)}[direction]
        nx = self.x + dx
        ny = self.y + dy
        if not (0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE):
            print("Wall ahead, can't move", direction)
        else:
            self.x = nx
            self.y = ny

    def show(self):
        for y in range(GRID_SIZE):
            row = ""
            for x in range(GRID_SIZE):
                if (x, y) == (self.x, self.y):
                    row += "R "
                else:
                    row += ". "
            print(row)
        print()

robot = Robot()
for step in ["right", "right", "down", "down", "down", "down", "down"]:
    robot.move(step)
    robot.show()
