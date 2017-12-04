#!/usr/bin/env python3

from high_entropy import passphrase_check, anagram_check


def test_passphrase_check():
    assert passphrase_check('aa bb cc dd ee')
    assert not passphrase_check('aa bb cc dd aa')
    assert passphrase_check('aa bb cc dd aaa')


def test_anagram_check():
    assert not anagram_check('abcde fghij')
    assert anagram_check('abcde xyz ecdab')
    assert not anagram_check('a ab abc abd abf abj')
    assert not anagram_check('iiii oiii ooii oooi oooo')
    assert anagram_check('oiii ioii iioi iiio')
