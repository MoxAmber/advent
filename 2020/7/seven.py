import re
from collections import defaultdict
from typing import Dict, Set

name_regex = r'^(.+?) bags'
name_matcher = re.compile(name_regex)

rule_regex = r'(\d+) (\D+) bag(?:s?)'
rule_matcher = re.compile(rule_regex)

def count_bag_contents(bag_name: str, bags: Dict[str, Dict[str, int]]):
    bag = bags[bag_name]
    total = 1 # The bag itself counts as a bag
    for target_bag_name, number in bag.items():
        bag_count = count_bag_contents(target_bag_name, bags)
        total += (number * bag_count)

    return total

if __name__ == "__main__":
    bags: Dict[str, Dict[str, int]] = {}
    with open("input.txt") as f:
        for line in f:
            name_match = name_matcher.match(line)

            if name_match:
                name = name_match[1]
                bags[name] = {}
            else:
                continue

            rule_match = rule_matcher.findall(line)

            if rule_match:
                for match in rule_match:
                    bags[name][match[1]] = int(match[0])
    
    bags_by_containers: Dict[str, Dict[str, int]] = {}
    for name, contents in bags.items():
        bags_by_containers[name] = {}
        for outer_name, outer_contents in bags.items():
            if name in outer_contents:
                bags_by_containers[name][outer_name] = outer_contents[name]

    targets = {'shiny gold'}
    matches: Set[str] = set()
    while targets:
        new_targets: Set[str] = set()
        for target in targets:
            new_targets.update(bags_by_containers[target].keys())

        matches.update(new_targets)
        targets = new_targets

    print(f'Part one: {len(matches)}')
    print(f'Part two: {count_bag_contents("shiny gold", bags) - 1}')

