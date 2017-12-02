#!/usr/bin/env python3

from corruption_checksum import part_one, part_two


part_one_input = '''5 1 9 5
7 5 3
2 4 6 8'''.split('\n')

part_two_input = '''5 9 2 8
9 4 7 3
3 8 6 5'''.split('\n')


def test_part_one():
    assert part_one(part_one_input) == 18


def test_part_two():
    assert part_two(part_two_input) == 9
