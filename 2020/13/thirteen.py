from functools import reduce

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

def part1():
    with open('input.txt') as f:
        current_time = int(f.readline().strip())
        buses = [int(x) for x in f.readline().strip().split(',') if x != "x"]

    results = {}
    for bus in buses:
        results[bus] = bus - (current_time % bus)

    nearest_bus = min(results, key=results.get)
    print(f'Part One: {nearest_bus * results[nearest_bus]}')

def part2():
    with open('input.txt') as f:
        current_time = int(f.readline().strip())
        buses = f.readline().strip().split(',')

    dividers = [int(bus) for bus in buses if bus != 'x']
    remainders = [int(bus) - i for i, bus in enumerate(buses) if bus != 'x']

    result = chinese_remainder(dividers, remainders)
    print(f'Part Two: {result}')

if __name__ == "__main__":
    part1()
    part2()
