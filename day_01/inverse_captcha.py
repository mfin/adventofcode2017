#!/usr/bin/env python3

with open('day_01/input.txt') as file:
    puzzle_sequence = file.readline()


def part_one(sequence):
    result = sum(int(char) for i, char in enumerate(sequence) if char == sequence[i-1])
    
    return result


def part_two(sequence):
    step = int(len(sequence)/2)
    result = sum(int(char) for i, char in enumerate(sequence) if char == sequence[i-step])
    
    return result


print(f'day_01: Solution for the first part is {part_one(puzzle_sequence)} and {part_two(puzzle_sequence)} for the second part.')
