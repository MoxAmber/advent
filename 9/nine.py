if __name__ == "__main__":
    prior_25 = []
    invalid_number = 0
    with open("input.txt") as f:
        ## Load preamble
        for _ in range(25):
            prior_25.append(int(f.readline()))

        for line in f:
            test_number = int(line)

            for number in prior_25:
                if test_number - number in prior_25:
                    break
            else:
                invalid_number = test_number
                break
                
            prior_25.pop(0)
            prior_25.append(test_number)
    print(f'Part One: {invalid_number}')

    with open("input.txt") as f:
        running_total = 0
        result = []
        for line in f:
            value = int(line)
            running_total += value
            result.append(value)

            while running_total > invalid_number:
                running_total -= result.pop(0)

            if running_total == invalid_number:
                print(f'Part Two Range: {result}')
                print(f'Part Two: {min(result) + max(result)}')
                break