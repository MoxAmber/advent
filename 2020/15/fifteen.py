from typing import Dict, TypedDict, List

NumberData = TypedDict("NumberData", {'indexes': List[int], 'count': int})

if __name__ == "__main__":
    with open('input.txt') as f:
        for line in f:
            starting_numbers = line.strip().split(',')
            spoken_numbers: Dict[int, NumberData] = {int(x): {'indexes': [i+1], 'count': 1} for i, x in enumerate(starting_numbers)}

            index = len(starting_numbers)
            last_number = int(starting_numbers[-1])
            last = spoken_numbers[last_number]
            while index < 30000000:
                index += 1
                if last['count'] == 1:
                    new = 0
                else:
                    new = last['indexes'][0] - last['indexes'][1]
                
                if new in spoken_numbers:
                    spoken_numbers[new]['count'] += 1
                    try:
                        spoken_numbers[new]['indexes'][1] = spoken_numbers[new]['indexes'][0]
                    except IndexError:
                        spoken_numbers[new]['indexes'].append(spoken_numbers[new]['indexes'][0])
                    spoken_numbers[new]['indexes'][0] = index
                else:
                    spoken_numbers[new] = {'indexes': [index], 'count': 1}

                last_number = new
                last = spoken_numbers[new]

            print(f'Part One: {last_number}')