from typing import Set

if __name__ == "__main__":
    with open('input.txt') as f:
        groups = f.read().split('\n\n')

    total = 0
    for group in groups:
        answers: Set[str] = set()
        for idx, line in enumerate(group.splitlines()):
            if idx == 0:
                answers = set(line)
            else:
                answers = answers.intersection(set(line))
        total += len(answers)

    print(total)