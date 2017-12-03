#!/usr/bin/env python3

puzzle_input = 312051


def part_one(input_square):
    x = y = dx = step = 0
    dy = -1

    while True:
        step += 1

        if step == input_square:
            return abs(x) + abs(y)
        
        if (x == y) or (x < 0 and x == -y) or (x > 0 and x == 1 - y):
            dx, dy = -dy, dx
        
        x, y = x + dx, y + dy


def part_two(last_square):
    x = y = dx = 0
    dy = -1
    coordinates = {(0, 0): 1}

    while True:
        if coordinates[(x,y)] > last_square:
            result = 0

            for position in [(x+1, y), (x, y+1), (x+1, y+1), (x-1, y), (x, y-1), (x-1, y-1), (x-1, y+1), (x+1, y-1)]:
                try:
                    result += coordinates[position]
                except Exception as e:
                    pass
                    
            return result

        if (x == y) or (x < 0 and x == -y) or (x > 0 and x == 1 - y):
            dx, dy = -dy, dx
        
        x, y = x + dx, y + dy
        
        current_sum = 0

        for position in [(x+1, y), (x, y+1), (x+1, y+1), (x-1, y), (x, y-1), (x-1, y-1), (x-1, y+1), (x+1, y-1)]:
            try:
                current_sum += coordinates[position]
            except Exception as e:
                pass
        
        coordinates[(x, y)] = current_sum


print(f'day_03: Solution for the first part is {part_one(puzzle_input)} and {part_two(puzzle_input)} for the second part.')
