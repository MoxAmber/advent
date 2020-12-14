if __name__ == "__main__":
    counter = 0
    first_basement = 0
    index = 0
    with open("input.txt") as f:
        while char := f.read(1):
            index += 1
            if char == '(':
                counter += 1
            elif char == ')':
                counter -= 1
            
            if counter == -1 and first_basement == 0:
                first_basement = index

    print(f'Part One: {counter}')
    print(f'Part Two: {first_basement}')