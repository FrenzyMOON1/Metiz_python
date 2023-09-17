from random import choice


class RandomWalk:
    def __init__(self, num_points=50000):
        self.num_points = num_points
        self.x_value = [0]
        self.y_value = [0]

    def fill_walk(self):
        while len(self.x_value) < self.num_points:
            x_step = choice(list(range(1, 51)))
            y_step = choice(list(range(1, 51)))
            if x_step == 0 and y_step == 0:
                continue
            next_x = self.x_value[-1] + x_step
            next_y = self.y_value[-1] + y_step
            self.x_value.append(next_x)
            self.y_value.append(next_y)
