from typing import List, TypedDict, Set
import time

Line = TypedDict("Line", {'op': str, 'arg': str})
def run_code(code: List[Line], idx = 0, initial_acc = 0):
    acc = initial_acc
    visited_lines: Set[int] = set()

    line_idx = idx
    while line_idx not in visited_lines and line_idx < len(operations):
        visited_lines.add(line_idx)
        op = code[line_idx]['op']
        try:
            arg = int(code[line_idx]['arg'])
        except ValueError:
            raise ValueError(f'Invalid argument in line {line_idx}')

        if op == 'nop':
            line_idx += 1
        elif op == 'acc':
            acc += arg
            line_idx += 1
        elif op == 'jmp':
            line_idx += arg
    
    if line_idx in visited_lines:
        raise RuntimeError(f'Infinite loop detected', {'acc': acc, 'line': line_idx, 'visited_lines': visited_lines})
    
    return {'acc': acc, 'visited_lines': visited_lines}

if __name__ == "__main__":
    operations: List[Line] = []
    with open('input.txt') as f:
        for line in f:
            op, arg = line.strip().split(maxsplit=1)
            operations.append({'op': op, 'arg': arg})

    try:
        run_code(operations)
    except RuntimeError as e:
        first_failure = e.args[1]

    print(f'Part One: {first_failure["acc"]}')


    result = None
    for visited_line in first_failure['visited_lines']:
        if operations[visited_line]['op'] == "jmp":
            operations[visited_line]['op'] = "nop"
        elif operations[visited_line]['op'] == "nop":
            operations[visited_line]['op'] = 'jmp'
        else:
            continue

        try:
            result = run_code(operations)
            break
        except RuntimeError as e:
            if operations[visited_line]['op'] == "jmp":
                operations[visited_line]['op'] = "nop"
            elif operations[visited_line]['op'] == "nop":
                operations[visited_line]['op'] = 'jmp'
    
    if result:
        print(f'Part Two: {result["acc"]}')
