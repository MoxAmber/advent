import functools

cache = {}
def paths_to_end(node, adaptors):
    if node == max(adaptors):
        return 1
    elif node in cache:
        return cache[node]
    paths = 0
    for i in range(1, 4):
        if node+i in adaptors:
            paths += paths_to_end(node+i, adaptors)
    cache[node] = paths
    return paths

if __name__ == "__main__":
    with open("input.txt") as f:
        adaptors = [int(x) for x in f]

    adaptors.append(0)

    sorted_adaptors = sorted(adaptors)

    differences = [sorted_adaptors[x] - sorted_adaptors[x-1] for x in range(1, len(sorted_adaptors))]

    print(f'Part One: {differences.count(1) * (differences.count(3) + 1)}')

    print(f'Part Two: {paths_to_end(0, set(sorted_adaptors))}')


