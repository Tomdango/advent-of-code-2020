# Advent of Code 2020
# Day Five - Part One
# Thomas Judd-Cooper

from math import ceil

def get_seats():
    for row in open("input.txt"):
        yield row.strip()

calculate_row = lambda seat: int(seat[:7].replace("F", "0").replace("B", "1"), 2)

calculate_column = lambda seat: int(seat[-3:].replace("L", "0").replace("R", "1"), 2)

calculate_seat_id = lambda row, col: row * 8 + col

def part_one():
    highest_seat_id = -1

    for seat in get_seats():
        row = calculate_row(seat)
        col = calculate_column(seat)

        seat_id = calculate_seat_id(row, col)
        if seat_id > highest_seat_id:
            highest_seat_id = seat_id

    return highest_seat_id

if __name__ == "__main__":
    highest_id = part_one()
    print(f"Highest Seat ID: {highest_id}")
