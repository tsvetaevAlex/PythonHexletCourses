from symbols import is_vowel


def count_vowels(message: str) -> int:
    count = 0
    for s in message:
        if is_vowel(s):
            count += 1

    return count
