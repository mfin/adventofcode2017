#!/usr/bin/env python3

with open('day_02/input.txt') as file:
    puzzle_input = file.readlines()


def part_one(sequence):
    result = 0

    for line in sequence:
        numbers = [int(number) for number in line.split()]
        numbers.sort()

        result += numbers[-1] - numbers[0]
    
    return result


def part_two(sequence):
    result = 0

    for line in sequence:
        numbers = [int(number) for number in line.split()]

        for number in numbers:
            for divider in numbers:
                if not number % divider and number is not divider:
                    result += number / divider
                    break

    return int(result)


print(f'day_02: Solution for the first part is {part_one(puzzle_input)} and {part_two(puzzle_input)} for the second part.')
