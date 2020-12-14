import hashlib

def zero_hash(secret: str, num_zeros: int):
    suffix = 0
    test_hash = ""
    while not test_hash.startswith('0' * num_zeros):
        suffix += 1
        test_hash = hashlib.md5(f'{secret}{suffix}'.encode()).hexdigest()

    return suffix

if __name__ == "__main__":

    with open('input.txt') as f:
        secret = f.readline().strip()

    suffix = zero_hash(secret, 5)
    print(f'Part One: {suffix}')

    suffix = zero_hash(secret, 6)
    print(f'Part Two: {suffix}')