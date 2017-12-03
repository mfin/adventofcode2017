#!/usr/bin/env python3

from spiral_memory import part_one, part_two


def test_part_one():
    assert part_one(1) == 0
    assert part_one(12) == 3
    assert part_one(23) == 2
    assert part_one(1024) == 31


def test_part_two():
    assert part_two(1) == 2
    assert part_two(2) == 4
    assert part_two(4) == 5
    assert part_two(11) == 23
    assert part_two(122) == 133
    assert part_two(147) == 304
