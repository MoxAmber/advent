import re

part_1_rules = [
    lambda x: len(re.findall(r'[aeiou]', x)) >= 3,
    lambda x: re.search(r'(.)\1', x) != None,
    lambda x: re.search(r'ab|cd|pq|xy', x) == None
]

part_2_rules = [
    lambda x: re.search(r'(..).*\1', x) != None,
    lambda x: re.search(r'(.).\1', x) != None
]

if __name__ == "__main__":
    nice_part_1 = 0
    nice_part_2 = 0
    with open('input.txt') as f:
        for line in f:
            if all(rule(line.strip()) for rule in part_1_rules):
                nice_part_1 += 1
            if all(rule(line.strip()) for rule in part_2_rules):
                nice_part_2 += 1

    print(f'Part One: {nice_part_1}')
    print(f'Part One: {nice_part_2}')