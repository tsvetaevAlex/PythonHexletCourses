
# BEGIN (write your solution here)

def letter_multiply(text: str, char: str, character_repeat_count: int)->str:
    #print (f"text: {text} | char: {char} | QTY: {echo}")
    result = text.replace(char, char*character_repeat_count)
    #print(f"result text: {result}")
    return result
# END
s

assert letter_multiply('python', 'p', 3) == 'pppython'
assert letter_multiply('python', 'o', 4) == 'pythoooon'
assert letter_multiply('java', 'a', 2) == 'jaavaa'
assert letter_multiply('java', 'a', 0) == 'jv'