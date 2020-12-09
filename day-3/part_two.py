# Advent of Code 2020
# Day Three - Part One
# Thomas Judd-Cooper
from part_one import Toboggan


class ConfigurableToboggan(Toboggan):
    def __init__(self, x_delta, y_delta):
        super().__init__()
        self.x_delta = x_delta
        self.y_delta = y_delta

    def _move(self):
        self.x += self.x_delta
        self.y += self.y_delta

    @property
    def patterns(self):
        for index, pattern in enumerate(open("input.txt")):
            if index != self.y:
                continue

            stripped_pattern = pattern.rstrip()
            repeat_count = self.x // len(stripped_pattern) + 1
            yield stripped_pattern * repeat_count


if __name__ == "__main__":
    all_routes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    ]

    # Start with 1 tree, so that we get the original number for the first
    # multiplication.
    multiplied_tree_count = 1

    for x_delta, y_delta in all_routes:
        vehicle = ConfigurableToboggan(x_delta, y_delta)
        vehicle.ride()
        multiplied_tree_count = multiplied_tree_count * vehicle.tree_count

    print(f"Multiplied Tree Count: {multiplied_tree_count}")
