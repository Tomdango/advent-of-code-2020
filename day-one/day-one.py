# Advent of Code 2020
# Day One
# Thomas Judd-Cooper
from typing import List, Iterable, Tuple
from itertools import combinations
from math import prod

def read_file() -> List[int]:
    """ Read in all of the numbers from the input """
    with open("input.txt", "r") as input_file:
        all_numbers = input_file.read().split("\n")

        # Quite often, the auto-linting in IDEs and Git adds a trailing whitespace
        if all_numbers[len(all_numbers) - 1] == "":
            del all_numbers[len(all_numbers) - 1]

        return [int(n) for n in all_numbers]

def get_combinations(numbers: List[int], r: int):
    return combinations(numbers, r)

def find_combination(all_combinations: Iterable[Tuple[int, int]], target: int) -> Tuple[int, int]:
    for combination in all_combinations:
        if sum(combination) == target:
            return combination

    return None

def part_one() -> int:
    print("=== PART ONE ===")

    all_numbers = read_file()
    all_combinations = get_combinations(all_numbers, 2)

    target = 2020
    correct_combination = find_combination(all_combinations, target)

    if correct_combination is None:
        raise Exception(f"No Combinations found for target: {target}")

    multiple = prod(correct_combination)

    print(f"Combination Found: {correct_combination}")
    print(f"Multiple of Numbers: {multiple}")
    print("================\n")
    return multiple

def part_two() -> int:
    print("=== PART TWO ===")

    # It's not very efficient to read in all the numbers twice, but for the sake of two independent
    # examples, we're going to do it anyway
    all_numbers = read_file()
    all_combinations = get_combinations(all_numbers, 3)

    target = 2020
    correct_combination = find_combination(all_combinations, target)

    if correct_combination is None:
        raise Exception(f"No Combinations found for target: {target}")

    first, second, third = correct_combination
    multiple = prod(correct_combination)

    print(f"Combination Found: {correct_combination}")
    print(f"Multiple of Numbers: {multiple}")
    print("================\n")

if __name__ == "__main__":
    part_one()
    part_two()
