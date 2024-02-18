
def has_char(text: str, symbol: str) -> bool:
    print(f"arguments received: text[{text}] | symol to search '{symbol}'")
    i: int = 0
    print(f"index 'i' before loop: {i}")
    l: int = len(text)
    print(f"Len' before loop: {l}")
    while i < l:
        print (f"index[{i}] | char '{text[i]}'")
        if text[i].lower() == symbol.lower():
            print("--> return True")
            return True
        else:
            i += 1
    del i
    print("-->Return False")
    return False

print(has_char('Hexlet', 'H'))  # => True
print(has_char('Hexlet', 'h'))  # => True
print(has_char('Awesomeness', 'd'))  # => False


has_char('Hexlet', 'H')
has_char('Hexlet', 'h')
has_char('Awesomeness', 'm')
has_char('Awesomeness', 'S')
has_char('Awesomeness', 'd')
has_char('', 'r')
