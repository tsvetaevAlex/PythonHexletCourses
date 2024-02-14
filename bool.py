
def has_upper_case(text: str) -> bool:
    #origin_text = str
    lowered_str = str.lower()
    return not lowered_str==text

has_upper_case('')  # False
has_upper_case('python')  # False
has_upper_case('pyThon')  # True



'''
assert has_upper_case("Hexlet")
assert has_upper_case("TIME")
assert has_upper_case("city of New York")
assert not has_upper_case("python")
assert not has_upper_case("")
'''
