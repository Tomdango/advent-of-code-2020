# Advent of Code 2020
# Day Two - Part Two
# Thomas Judd-Cooper
from part_one import read_file

def is_valid(entry: dict) -> bool:
    password = entry.get("password")
    first_index = entry.get("min") - 1
    second_index = entry.get("max") - 1
    target_char = entry.get("letter")

    char_one = password[first_index]
    char_two = password[second_index]

    # XOR
    return bool(char_one == target_char) ^ bool(char_two == target_char)


if __name__ == "__main__":
    # DRY - Don't Repeat Yourself
    valid_passwords = [entry for entry in read_file() if is_valid(entry)]

    print(f"[PART TWO] Valid Password Count: {len(valid_passwords)}")
