# Advent of Code 2020
# Day Two - Part One
# Thomas Judd-Cooper
from typing import Iterable
from functools import reduce

def parse_line(line: str):
    min_max, letter, password = line.split(" ")

    min_count, max_count = [int(n) for n in min_max.split("-")]

    return {
        "min": min_count,
        "max": max_count,
        "letter": letter.replace(":", ""),
        "password": password
    }

def read_file() -> Iterable[str]:
    with open("input.txt", "r") as input_file:
        for line in input_file:
            yield parse_line(line.replace("\n", ""))

def is_valid(entry: dict):
    letter_count = entry["password"].count(entry["letter"])

    if letter_count >= entry["min"] and letter_count <= entry["max"]:
        return True
    return False

def part_one():
    validation_result = [entry for entry in read_file() if is_valid(entry)]

    print(f"[PART ONE] Valid Password Count: {len(validation_result)}")


if __name__ == "__main__":
    part_one()


