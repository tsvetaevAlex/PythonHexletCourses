from random import randint

def choice_from_range(word: str, begin: int, end: int) -> str:
    print("__________Arguments__________")
    print(f"word: {word}")
    print(f"range begin: {begin}")
    print(f"range end: {end}")
    random_index = randint(begin, end)
    print("return value: {word[random_index]}")
    return word[random_index]


text = "abcdef"
choice_from_range(text, 3, 5)  # d
choice_from_range(text, 3, 5)  # f
choice_from_range(text, 3, 5)  # e

# диапазон включает начальный и конечный индексы
choice_from_range(text, 2, 2)  # c