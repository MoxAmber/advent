from typing import List
from itertools import chain, combinations

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(1, len(s)+1))


def replace_index(value: str, idx: int, char: str) -> str:
    if idx + 1 < len(value):
        return value[:idx] + char + value[idx + 1:]
    return value[:idx] + char
    

def apply_mask(mask: str, value: int) -> int:
    binary_str = str(bin(value))[2:]

    pad_len = len(mask) - len(binary_str)
    binary_str = '0'*pad_len + binary_str
    for idx, char in enumerate(mask):
        if char == 'X':
            continue
        else:
            binary_str = replace_index(binary_str, idx, char)

    return int(f'{binary_str}', base=2)

def floating_mask(mask: str, value: int) -> List[int]:
    binary_str = str(bin(value))[2:]
    results: List[int] = []

    pad_len = len(mask) - len(binary_str)
    binary_str = '0'*pad_len + binary_str
    first_result = binary_str[:]
    additives = []
    for idx, char in enumerate(reversed(mask)):
        if char == '1':
            first_result = replace_index(first_result, len(mask) - 1 - idx, char)
        elif char == 'X':
            first_result = replace_index(first_result, len(mask) - 1 - idx, '0')
            additives.append(2**idx)

    results.append(int(first_result, base=2))

    for addition_set in powerset(additives):
        results.append(results[0] + sum(addition_set))
        
    return results

if __name__ == "__main__":
    mask = ""
    part1_memory = {}
    part2_memory = {}
    with open('input.txt') as f:
        for line in f:
            var, _, value = line.strip().split(maxsplit=2)
            if var == "mask":
                mask = value
            else:
                base_location = int(var[4:-1])
                part1_memory[base_location] = apply_mask(mask, int(value))
                locations = floating_mask(mask, base_location)
                for location in locations:
                    part2_memory[location] = int(value)

    print(max(part1_memory.values()))
    print(f'Part One: {sum(part1_memory.values())}')
    print(max(part2_memory.values()))
    print(f'Part Two: {sum(part2_memory.values())}')