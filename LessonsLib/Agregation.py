def join_numbers_from_range(s: int, f: int):  # (range) s - start value | f - finish vValue
    result: str = ""
    while s <= f:

        result += str(s)
        s += 1

    print(result)

join_numbers_from_range(2, 2)
join_numbers_from_range(1, 5)
join_numbers_from_range(10, 12)
