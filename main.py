GRID_SIZE = 5

class Robot:
    def __init__(self):
        self.x = 0
        self.y = 0

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
robot.show()
