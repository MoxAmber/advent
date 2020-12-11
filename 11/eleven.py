from typing import List, Tuple, Union, Dict, cast
from collections import defaultdict
from itertools import product


directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
def get_adjacent_seats(x: int, y: int, seat_map: List[List[str]]) -> List[Tuple[int, int]]:
    adjacent_seats: List[Tuple[int, int]] = []
    if seat_map[y][x] == '.':
        return adjacent_seats
    for dx, dy in directions:
        if y + dy >= 0 and y + dy < len(seat_map) and x + dx >= 0 and x + dx < len(seat_map[0]):
            adjacent_seats.append((x+dx, y+dy))

    return adjacent_seats

ray_cache: Dict[Tuple[int, int], Dict[Tuple[int, int], Union[Tuple[int,int], None]]] = defaultdict(dict)
def trace_ray(dx: int, dy: int, x: int, y: int, seat_map: List[List[str]]) -> Union[Tuple[int,int], None]:
    if (x, y, dx, dy) in ray_cache:
        pass
    elif x + dx < 0 or x + dx >= len(seat_map[0]) or y + dy < 0 or y + dy >= len(seat_map):
        ray_cache[(x,y)][(dx,dy)] = None
    elif seat_map[y+dy][x+dx] in ('#', 'L'):
        ray_cache[(x,y)][(dx,dy)] = (x+dx, y+dy)
    else:
        ray_cache[(x,y)][(dx,dy)] = trace_ray(dx, dy, x+dx, y+dy, seat_map)
    return ray_cache[(x,y)][(dx,dy)]

def get_visible_seats(x: int, y: int, seat_map: List[List[str]]) -> List[Tuple[int,int]]:
    visible_seats: List[Tuple[int, int]] = []
    if seat_map[y][x] == '.':
        return visible_seats
    for dx, dy in directions:
        seat = trace_ray(dx, dy, x, y, seat_map)
        if seat:
            visible_seats.append(seat)

    return visible_seats

def get_values(coords: List[Tuple[int, int]], seat_map: List[List[str]]) -> List[str]:
    return [seat_map[y][x] for x, y in coords]

def run_automata(neighour_map: List[List[List[Tuple[int, int]]]], seat_map: List[List[str]], occupied_threshold = 4) -> List[List[str]]:
    changed_seats = True
    while changed_seats:
        changed_seats = False
        updated_seat_map: List[List[str]] = []
        for y, row in enumerate(seat_map):
            updated_seat_map.append([])
            for x, seat in enumerate(row):
                updated_seat_map[y].append(seat)
                if seat == '.':
                    continue
                neighbours = get_values(neighbour_map[y][x], seat_map)
                if seat == 'L':
                    if not any(i == '#' for i in neighbours):
                        updated_seat_map[y][x] = '#'
                        changed_seats = True
                elif seat == '#':
                    if neighbours.count('#') >= occupied_threshold:
                        updated_seat_map[y][x] = 'L'
                        changed_seats = True
        seat_map = updated_seat_map
        # for line in seat_map:
        #     print(''.join(line))
        # print('\n')
    
    return seat_map


if __name__ == "__main__":
    with open('input.txt') as f:
        seat_map = [list(x.strip()) for x in f.readlines()]

    neighbour_map = [[get_adjacent_seats(x, y, seat_map) for x in range(0, len(row))] for y, row in enumerate(seat_map)]
    seat_map = run_automata(neighbour_map, seat_map)

    print(f'Part One: {sum(seat_map, cast(List[str], [])).count("#")}')

    with open('input.txt') as f:
        seat_map = [list(x.strip()) for x in f.readlines()]

    neighbour_map = [[get_visible_seats(x, y, seat_map) for x in range(0, len(row))] for y, row in enumerate(seat_map)]
    seat_map = run_automata(neighbour_map, seat_map, 5)
    print(f'Part Two: {sum(seat_map, cast(List[str], [])).count("#")}')

