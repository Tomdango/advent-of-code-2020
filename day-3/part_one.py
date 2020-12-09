# Advent of Code 2020
# Day Three - Part One
# Thomas Judd-Cooper

class Toboggan:
    TREE = "#"
    OPEN = "."

    def __init__(self):
        self.tree_count = 0
        self.x = 0
        self.y = 0

    def ride(self):
        for pattern in self.patterns:
            self._check_is_tree(pattern)
            self._move()

    def _check_is_tree(self, pattern):
        if pattern[self.x] == self.TREE:
            self.tree_count += 1

    def _move(self):
        self.x += 3
        self.y += 1

    @property
    def patterns(self):
        for pattern in open("input.txt"):
            stripped_pattern = pattern.rstrip()
            repeat_count = self.x // len(stripped_pattern) + 1
            yield stripped_pattern * repeat_count

if __name__ == "__main__":
    vehicle = Toboggan()
    vehicle.ride()
    print(f"Tree Count: {vehicle.tree_count}")
