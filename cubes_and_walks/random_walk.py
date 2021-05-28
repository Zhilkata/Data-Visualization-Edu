from random import choice


def get_step():
    direction = choice([1, -1])
    distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
    return direction * distance


class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points=5000):
        """Init attributes of walk"""
        self.num_points = num_points

        # All walks begin at (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk."""

        # Keep taking steps until the limit is reached.
        while len(self.x_values) < self.num_points:

            # Decide direction & steps

            x_step = get_step()

            y_step = get_step()

            # Skip not-taken steps
            if x_step == 0 and y_step == 0:
                continue

            # Calculate new position.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
