from typing import List

def run_toboggan(map: List[str], x_movement: int, y_movement: int) -> int:
    trees_hit = 0
    x_index = 0
    max_x = len(map[0]) - 1
    for idx, line in enumerate(map):
        if idx % y_movement != 0:
            continue
        if line[x_index] == "#":
            trees_hit += 1
        x_index = (x_index + x_movement) % max_x

    return trees_hit

if __name__ == "__main__":
    with open("three_input.txt") as f:
        input = f.readlines()

    one_one = run_toboggan(input, 1, 1)
    three_one = run_toboggan(input, 3, 1)
    five_one = run_toboggan(input, 5, 1)
    seven_one = run_toboggan(input, 7, 1)
    one_two = run_toboggan(input, 1, 2)

    print(f'Right 1, down 1: {one_one}')
    print(f'Right 3, down 1: {three_one}')
    print(f'Right 5, down 1: {five_one}')
    print(f'Right 7, down 1: {seven_one}')
    print(f'Right 1, down 2: {one_two}')

    print(one_one * three_one * five_one * seven_one * one_two)