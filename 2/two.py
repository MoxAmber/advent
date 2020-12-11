import re


def check_password(
    position_one: int, position_two: int, character: str, password: str
) -> bool:
    try:
        return (password[position_one - 1] == character) ^ (
            password[position_two - 1] == character
        )
    except IndexError:
        return False
    # count = password.count(character)
    # return range_lower <= count <= range_upper


if __name__ == "__main__":
    with open("two_input.txt") as f:
        input = f.readlines()

    rule_regex = r"(\d+)-(\d+) (\w): (\w+)"
    matcher = re.compile(rule_regex)

    valid_passwords = 0
    for line in input:
        match = matcher.match(line)
        if match:
            position_one = int(match.group(1))
            position_two = int(match.group(2))
            character = match.group(3)
            password = match.group(4)
            if check_password(position_one, position_two, character, password):
                valid_passwords += 1

    print(valid_passwords)
