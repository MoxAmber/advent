from typing import List, Tuple, Union


def find_pair(input: List[int], total: int) -> Union[Tuple[int, int], None]:
    """Find pair from input that adds up to total."""

    input_set = set(input)

    for x in input:
        if total - x in input_set:
            return (x, total - x)

    return None

    # sorted_input = sorted(input)

    # for idx, x in enumerate(sorted_input):
    #     for y in reversed(sorted_input[idx + 1:]):
    #         if x + y == total:
    #             return (x, y)
    # return None


def find_triplet(input: List[int], total: int) -> Union[Tuple[int, int, int], None]:
    """Find triplet from input that adds up to total."""

    sorted_input = sorted(input)

    for idx, x in enumerate(sorted_input):
        if pair := find_pair(sorted_input[idx + 1:], total - x):
            return (x, pair[0], pair[1])

    return None


if __name__ == "__main__":
    with open("one_input.txt") as f:
        input = [int(x) for x in f.readlines()]

    pair = find_pair(input, 2020)
    if pair:
        print(pair[0] * pair[1])

    triplet = find_triplet(input, 2020)
    if triplet:
        print(triplet[0] * triplet[1] * triplet[2])
