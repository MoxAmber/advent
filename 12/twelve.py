from typing import TextIO, Tuple

def follow_directions(f: TextIO) -> Tuple[int, int]:
    east = 0
    north = 0
    facing = 90

    for instruction in f:
        operation = instruction[0]
        arg = int(instruction[1:])

        if operation == 'N':
            north += arg
        elif operation == 'S':
            north -= arg
        elif operation == 'E':
            east += arg
        elif operation == 'W':
            east -= arg
        elif operation == 'R':
            facing = (facing + arg) % 360
        elif operation == 'L':
            facing = (facing - arg) % 360
        elif operation == 'F':
            if facing == 0:
                north += arg
            elif facing == 90:
                east += arg
            elif facing == 180:
                north -= arg
            elif facing == 270:
                east -= arg
    
    return (east, north)


def follow_waypoint(f: TextIO) -> Tuple[int, int]:
    ship_east = 0
    ship_north = 0
    
    waypoint_east = 10
    waypoint_north = 1

    for instruction in f:
        operation = instruction[0]
        arg = int(instruction[1:])

        if operation == 'N':
            waypoint_north += arg
        elif operation == 'S':
            waypoint_north -= arg
        elif operation == 'E':
            waypoint_east += arg
        elif operation == 'W':
            waypoint_east -= arg
        elif operation == 'R':
            rotations = int(arg / 90)
            for _ in range(0, rotations):
                new_east = waypoint_north
                new_north = -waypoint_east
                waypoint_east = new_east
                waypoint_north = new_north
        elif operation == 'L':
            rotations = int(arg / 90)
            for _ in range(0, rotations):
                new_east = -waypoint_north
                new_north = waypoint_east
                waypoint_east = new_east
                waypoint_north = new_north
        elif operation == 'F':
            ship_east += arg * waypoint_east
            ship_north += arg * waypoint_north
    
    return (ship_east, ship_north)


if __name__ == "__main__":
    with open('input.txt') as f:
        east, north = follow_directions(f)

    print(f'Part One: East {east}, North {north}, Distance {abs(east)+abs(north)}')

    with open('input.txt') as f:
        east, north = follow_waypoint(f)

    print(f'Part Two: East {east}, North {north}, Distance {abs(east)+abs(north)}')
        