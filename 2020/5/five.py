from typing import Dict

def parse_seat(seat: str) -> Dict[str, int]:
    row = int(seat[:7].replace('F', '0').replace('B', '1'), 2)
    column = int(seat[-3:].replace('L', '0').replace('R', '1'), 2)

    return {"row": row, "column": column, "seat_id": row * 8 + column}

if __name__ == "__main__":
    seats = set()
    highest_id = 0
    lowest_id = 99999
    with open("input.txt") as f:
        for line in f:
            seat = parse_seat(line.strip())
            seat_id = seat['seat_id']
            if seat_id > highest_id:
                highest_id = seat_id
            if seat_id < lowest_id:
                lowest_id = seat_id
            seats.add(seat_id)

    print(set(range(lowest_id, highest_id)).difference(seats))
