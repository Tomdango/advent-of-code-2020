# Advent of Code 2020
# Day Five - Part Two
# Thomas Judd-Cooper

from part_one import get_seats, calculate_column, calculate_row, calculate_seat_id

def get_missing_seat(seat_ids):
    last_index = len(seat_ids) - 1

    for index, seat_id in enumerate(seat_ids):
        if index == 0 or index == last_index:
            continue

        prev_seat_id = seat_ids[index - 1]
        if seat_id - prev_seat_id == 2:
            return seat_id - 1

    return None

def part_two():
    seat_ids = []

    for seat in get_seats():
        row, col = calculate_row(seat), calculate_column(seat)
        seat_ids.append(calculate_seat_id(row, col))

    seat_ids.sort()

    return get_missing_seat(seat_ids)

if __name__ == "__main__":
    missing_seat_id = part_two()
    print(f"Missing Seat ID: {missing_seat_id}")
