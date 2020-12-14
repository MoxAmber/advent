if __name__ == "__main__":
    visited = {(0,0)}

    x=0
    y=0

    with open("input.txt") as f:
        while char := f.read(1):
            if char == "^":
                y += 1
            elif char == "v":
                y -= 1
            elif char == ">":
                x += 1
            elif char == "<":
                x -= 1

            visited.add((x, y))

    print(f'Part One: {len(visited)}')

    santa_visited = {(0,0)}
    robot_visited = {(0,0)}
    santa = {'x': 0, 'y': 0}
    robot = {'x': 0, 'y': 0}
    with open("input.txt") as f:
        index = 0
        while char := f.read(1):
            if index % 2 == 0:
                visited = santa_visited
                coords = santa
            else:
                visited = robot_visited
                coords = robot
            if char == "^":
                coords['y'] += 1
            elif char == "v":
                coords['y'] -= 1
            elif char == ">":
                coords['x'] += 1
            elif char == "<":
                coords['x'] -= 1

            visited.add((coords['x'], coords['y']))
            index += 1

    print(f'Part Two: {len(santa_visited.union(robot_visited))}')