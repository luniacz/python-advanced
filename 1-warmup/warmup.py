def read_input(filename: str) -> list:
    with open(filename, 'r') as read_file:
        lines = read_file.readlines()

    numbers = []
    for line in lines:
        numbers.append(int(line))
    return numbers


def get_result(numbers: list) -> int:
    year_to_compare = 2020
    for value1 in numbers:
        for value2 in numbers:
            if value1 + value2 == year_to_compare:
                return value1 * value2
        numbers.pop(0)


numbers = read_input('input.txt')
print(get_result(numbers))
