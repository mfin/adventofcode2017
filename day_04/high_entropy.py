#!/usr/bin/env

with open('day_04/input.txt') as file:
    puzzle_input = [line.strip() for line in file]


def passphrase_check(passphrase):
    word_list = passphrase.split()

    for word in word_list:
        if word_list.count(word) > 1:
            return False

    return True


def anagram_check(passphrase):
    split_passphrase = [sorted(list(word)) for word in passphrase.split()]
    sorted_passphrase = ' '.join([''.join(word) for word in split_passphrase])

    if not passphrase_check(sorted_passphrase):
        return True

    return False


def part_one(passphrases):
    return sum(1 for passphrase in passphrases if passphrase_check(passphrase))


def part_two(passphrases):
    return sum(1 for passphrase in passphrases if passphrase_check(passphrase) and not anagram_check(passphrase))


print(f'day_04: Solution for the first part is {part_one(puzzle_input)} and {part_two(puzzle_input)} for the second part.')
