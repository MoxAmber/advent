from typing import Dict, List, Tuple
from collections import defaultdict
from functools import reduce

def check_tickets(rules: Dict[str, List[List[int]]], tickets: List[List[int]]) -> Tuple[int, List[List[int]]]:
    error_total = 0 
    bad_tickets = []
    for ticket in tickets:
        bad_ticket = False
        for value in ticket:
            if not any(x[0] <= value <= x[1] for ranges in rules.values() for x in ranges):
                error_total += value
                bad_ticket = True
        if bad_ticket:
            bad_tickets.append(ticket)

    return error_total, bad_tickets

def map_ticket(ticket: List[int], good_tickets: List[List[int]], rules: Dict[str, List[List[int]]]) -> Dict[str, int]:
    valid_fields: Dict[int, List[str]] = defaultdict(list)
    for i in range(0, len(ticket)):
        for field, ranges in rules.items():
            if all(any(x[0] <= ticket[i] <= x[1] for x in ranges) for ticket in good_tickets):
                valid_fields[ticket[i]].append(field)

    mapped_ticket: Dict[str, int] = {}
    while len(mapped_ticket) < len(ticket):
        for value, fields in valid_fields.items():
            if len(fields) == 1:
                mapped_ticket[fields[0]] = value
        new_valid_fields = {value: [x for x in fields if x not in mapped_ticket.keys()] for value, fields in valid_fields.items()}
        valid_fields = new_valid_fields
    return mapped_ticket


if __name__ == "__main__":
    with open('input.txt') as f:
        # Parse rules
        rules: Dict[str, List[List[int]]] = {}
        while (line := f.readline()) != '\n':
            field, range_part = line.strip().split(':', maxsplit=1)
            rules[field] = []
            for rule_range in range_part.split():
                if rule_range != 'or':
                    rules[field].append([x for x in sorted(int(y) for y in rule_range.split('-'))])

        # Discard 'your ticket' line
        f.readline()

        my_ticket = [int(x) for x in f.readline().strip().split(',')]

        # Discard blank line and 'nearby tickets'
        f.readline()
        f.readline()

        tickets: List[List[int]] = []
        for line in f:
            tickets.append([int(x) for x in line.strip().split(',')])

    error_total, bad_tickets = check_tickets(rules, tickets)
    print(f'Part One: {error_total}')

    good_tickets = [x for x in tickets if x not in bad_tickets]

    mapped_ticket = map_ticket(my_ticket, good_tickets, rules)
    print(mapped_ticket)
    print(f'Part Two {reduce(lambda x, y: x*y, (value for field, value in mapped_ticket.items() if field.startswith("departure")))}')